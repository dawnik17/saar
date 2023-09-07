from peft import PeftModel
import torch

from transformers import AutoModelForSeq2SeqLM, AutoTokenizer


class PeftModelUtils:
    @staticmethod
    def load_base_model(model_path="google/flan-t5-base"):
        model = AutoModelForSeq2SeqLM.from_pretrained(
            model_path, torch_dtype=torch.bfloat16, device_map="auto"
        )
        tokenizer = AutoTokenizer.from_pretrained(model_path)
        return model, tokenizer

    @staticmethod
    def load_from_peft_adapter(
        base_model_path, peft_model_path, train=False, merge_adapter=False
    ):
        model, tokenizer = PeftModelUtils.load_base_model(base_model_path)
        model = PeftModel.from_pretrained(
            model,
            peft_model_path,
            torch_dtype=torch.bfloat16,
            is_trainable=train,
            device_map="auto",
        )

        # merge the adapter to the main model
        if merge_adapter:
            model = model.merge_and_unload()

            if train:
                for param in model.parameters():
                    param.requires_grad = True

        return model, tokenizer

    @staticmethod
    def save_peft_adapter(model, model_path):
        model.save_pretrained(model_path)

    @staticmethod
    def merge_peft_and_save(model, model_path):
        model = model.merge_and_unload()
        model.save_pretrained(model_path)

    @staticmethod
    def save_tokenizer(tokenizer, model_path):
        tokenizer.save_pretrained(model_path)
