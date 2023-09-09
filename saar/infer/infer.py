"""
This script performs text summarization and title generation for a list of news articles using a pre-trained model. 
It leverages the 'PeftModelUtils' from the 'saar.models.instruct' module for these tasks. 
The script includes the following functions and operations:

1. 'GetTokens' Class:
   - Initializes with a tokenizer and determines the device (CPU or CUDA) for processing.
   - Sets up metadata and prompts for title and summary generation.
   - Provides methods to generate prompts for titles and summaries based on the input news articles.
   - Tokenizes the generated prompts for a specified mode ('summary' or 'title') and returns the tokenized input.

2. 'infer' Function:
   - Takes a pre-trained model, generation configuration, input data (news articles), and a mode ('summary' or 'title') as arguments.
   - Generates summaries or titles for the provided news articles using the specified model and configuration.
   - Cleans and decodes the model-generated text and adds it to the input data.
   - Returns the updated data with the generated summaries or titles.

3. The '__main__' block:
   - Imports necessary functions and modules from 'saar.utils' and 'saar.models.instruct'.
   - Retrieves a list of news articles from specified URLs and curates them.
   - Loads pre-trained models and tokenizers for both summary and title generation.
   - Configures generation settings for summaries and titles.
   - Invokes the 'infer' function to generate summaries and titles for the curated news articles.
   
Note:
- This script requires access to pre-trained models and tokenizers for text generation.
- The 'PeftModelUtils' class and 'GenerationConfig' are assumed to be defined elsewhere in the 'saar' module.

Example Usage:
1. Set the 'news' variable with a list of news articles (URLs).
2. Configure model and adapter paths.
3. Specify generation settings for summaries and titles.
4. Execute the script to generate summaries and titles for the provided news articles.
"""


import json
from saar.models.instruct import PeftModelUtils
import torch
import os
from saar.utils import clean_model_generated_text
from transformers import GenerationConfig


class GetTokens:
    def __init__(self, tokenizer):
        # device
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

        # tokenizer
        self.tokenizer = tokenizer

        # summary meta data
        summary_word_count = 60

        self.summary_start_prompt = (
            f"Summarize this news article in {summary_word_count} words.\n\n"
        )
        self.summary_end_prompt = "\n\nSummary: "

        # title meta data
        title_word_count = 5

        self.title_start_prompt = f"Give a title to the given news article in not more than {title_word_count} words.\n\n"
        self.title_mid_prompt = "\n\nSummary: "
        self.title_end_prompt = "\n\nTitle: "

    def get_title_prompt(self, news):
        return (
            self.title_start_prompt
            + news["full_text"]
            + self.title_mid_prompt
            + news["generated_summary"]
            + self.title_end_prompt
        )

    def get_summary_prompt(self, news):
        return self.summary_start_prompt + news["full_text"] + self.summary_end_prompt

    def tokenize(self, news: list, mode="summary"):
        prompt_func = getattr(self, f"get_{mode}_prompt")
        prompts = [prompt_func(news=new) for new in news]

        return self.tokenizer(
            prompts,
            return_tensors="pt",
            max_length=self.tokenizer.model_max_length,
            truncation=True,
            padding=True,
        ).input_ids.to(self.device)


class Infer:
    def __init__(
        self, summary_adapter_path: str = None, title_adapter_path: str = None
    ):
        # init
        self.summary_model, self.summary_tokenizer = None, None
        self.title_model, self.title_tokenizer = None, None
        self.get_summary_tokens, self.get_title_tokens = None, None

        # load summary adapter
        if summary_adapter_path is not None:
            (
                self.summary_model,
                self.summary_tokenizer,
            ) = PeftModelUtils.load_from_peft_adapter(
                adapter_path=summary_adapter_path, train=False, merge_adapter=False
            )
            self.get_summary_tokens = GetTokens(self.summary_tokenizer)

        # load title adapter
        if title_adapter_path is not None:
            (
                self.title_model,
                self.title_tokenizer,
            ) = PeftModelUtils.load_from_peft_adapter(
                adapter_path=title_adapter_path, train=False, merge_adapter=False
            )
            self.get_title_tokens = GetTokens(self.title_tokenizer)

        # summary generation config
        self.summary_generation_config = GenerationConfig(
            max_new_tokens=200,
            num_beams=8,
            do_sample=False,
            temperature=1.5,
            top_k=30,
            top_p=0.8,
        )

        # title generation config
        self.title_generation_config = GenerationConfig(
            max_new_tokens=25,
            num_beams=8,
            do_sample=False,
            temperature=1.5,
            top_k=30,
            top_p=0.8,
        )

    def __call__(self, data, mode="summary"):
        assert mode in ["summary", "title"]

        news = self.infer(
            model=self.__dict__[f"{mode}_model"],
            generation_config=self.__dict__[f"{mode}_generation_config"],
            mode=mode,
            data=data,
        )
        return news

    def infer(self, model, generation_config, data, mode):
        """
        for summary: data = [{"full_text": "..."}]
        for title: data = [{"full_text": "...", "summary": "..."}]
        """
        input_ids = self.__dict__[f"get_{mode}_tokens"].tokenize(news=data, mode=mode)

        # generate tokens
        peft_model_outputs = model.generate(
            input_ids=input_ids, generation_config=generation_config
        )

        # decode generated tokens
        for i in range(len(peft_model_outputs)):
            data[i][f"generated_{mode}"] = clean_model_generated_text(
                self.__dict__[f"{mode}_tokenizer"].decode(
                    peft_model_outputs[i], skip_special_tokens=True
                )
            )

        return data


if __name__ == "__main__":
    from saar.utils import get_full_news

    # fetch these urls using googlenews module
    # i.e saar.data.production.gnews
    news = [
        {
            "link": "https://www.ndtv.com/india-news/if-we-name-alliance-bharat-will-they-call-country-bjp-arvind-kejriwal-4361334"
        },
        {"link": "https://www.bbc.com/news/world-europe-66712477"},
        {
            "link": "https://www.the-independent.com/news/world/americas/us-politics/trump-mugshot-indictment-latest-news-b2404959.html"
        },
    ]

    news = [get_full_news(new) for new in news]

    # summary adapter, title adapter path
    summary_adapter_path = "./checkpoint/summary/"
    title_adapter_path = "./checkpoint/title/"

    infer = Infer(
        summary_adapter_path=summary_adapter_path, title_adapter_path=title_adapter_path
    )

    # generate summary
    news = infer(mode="summary", data=news)

    # generate title
    # NOTE: Title generation needs summary already generated as "generated_summary" key in the news dict
    news = infer(mode="title", data=news)
