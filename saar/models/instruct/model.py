"""
This module provides utility functions for working with the 'peft' library and transformers models for sequence-to-sequence tasks. 
It includes functions for loading, saving, and merging models and tokenizers. 
The module also defines a class 'PeftModelUtils' with static methods for these operations.

Functions:
1. 'load_base_model':
   - Loads a base transformer model for sequence-to-sequence tasks from a specified model path.
   - Returns the loaded model and tokenizer.

2. 'load_from_peft_adapter':
   - Loads a model from a 'peft' adapter, optionally making it trainable.
   - Merges the adapter with the base model if specified.
   - Returns the loaded model and tokenizer.

3. 'save_peft_adapter':
   - Saves a 'peft' adapter model to a specified model path.

4. 'merge_peft_and_save':
   - Merges a 'peft' adapter with the base model, saving the merged model to a specified model path.

5. 'save_tokenizer':
   - Saves a tokenizer to a specified model path.

Class 'PeftModelUtils':
- This class encapsulates the utility functions for loading, saving, and merging 'peft' adapter models.
- It does not require instantiation and is intended to be used statically.

Parameters:
- 'model_path' (str): The path to the base transformer model or 'peft' adapter model.
- 'base_model_path' (str): The path to the base transformer model.
- 'peft_model_path' (str): The path to the 'peft' adapter model.
- 'train' (bool): If True, allows training of the 'peft' adapter model.
- 'merge_adapter' (bool): If True, merges the 'peft' adapter with the base model.

Example Usage:
1. Loading a base model:
   model, tokenizer = PeftModelUtils.load_base_model(model_path="google/flan-t5-base")

2. Loading a model from a 'peft' adapter:
   model, tokenizer = PeftModelUtils.load_from_peft_adapter(
       base_model_path="google/flan-t5-base",
       peft_model_path="./path/to/peft/adapter/model",
       train=True,
       merge_adapter=True
   )

3. Saving a 'peft' adapter model:
   PeftModelUtils.save_peft_adapter(model, model_path="./path/to/save/peft/adapter")

4. Merging a 'peft' adapter with the base model and saving:
   PeftModelUtils.merge_peft_and_save(model, model_path="./path/to/save/merged/model")

5. Saving a tokenizer:
   PeftModelUtils.save_tokenizer(tokenizer, model_path="./path/to/save/tokenizer")

Note:
- The 'peft' library and the 'transformers' library are required dependencies for this module to function properly.
"""


from peft import PeftModel
import torch

from transformers import (AutoModelForSeq2SeqLM, 
                          AutoTokenizer)


class PeftModelUtils:
    @staticmethod
    def load_base_model(model_path="google/flan-t5-base"):
        """
        Loads a base transformer model for sequence-to-sequence tasks from the specified model path.
        
        Parameters:
            model_path (str): The path or identifier of the base transformer model to load.
        
        Returns:
            model (PreTrainedModel): The loaded transformer model.
            tokenizer (PreTrainedTokenizer): The associated tokenizer for the model.
        """
        model = AutoModelForSeq2SeqLM.from_pretrained(
            model_path, torch_dtype=torch.bfloat16, device_map="auto"
        )
        tokenizer = AutoTokenizer.from_pretrained(model_path)
        return model, tokenizer

    @staticmethod
    def load_from_peft_adapter(
        base_model_path: str, peft_model_path: str, train: bool=False, merge_adapter: bool=False
    ):
        """
        Loads a model from a 'peft' adapter, optionally making it trainable and merging it with the base model.

        Parameters:
            base_model_path (str): The path or identifier of the base transformer model.
            peft_model_path (str): The path to the 'peft' adapter model.
            train (bool): If True, allows training of the 'peft' adapter model (default is False).
            merge_adapter (bool): If True, merges the 'peft' adapter with the base model (default is False).

        Returns:
            model (PeftModel): The loaded 'peft' model, optionally merged with the base model.
            tokenizer (PreTrainedTokenizer): The associated tokenizer for the model.
        """
        model, tokenizer = PeftModelUtils.load_base_model(base_model_path)
        model = PeftModel.from_pretrained(
            model, 
            peft_model_path, 
            torch_dtype=torch.bfloat16, 
            is_trainable=train,
            device_map="auto"
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