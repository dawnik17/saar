from typing import List, Dict
import re


def deduplicate_list_of_dicts(input_list: List[Dict], keys_to_check: List[str]) -> List[Dict]:
    """
    Remove duplicates from a list of dictionaries based on specified keys.

    This function takes a list of dictionaries and a list of keys to check for duplicates.
    It iterates through the list of dictionaries, keeping only the first occurrence of each
    dictionary with distinct values for the specified keys.

    Args:
        input_list (list[dict]): A list of dictionaries to deduplicate.
        keys_to_check (list[str]): A list of keys to check for duplicates. Only dictionaries
            with distinct values for these keys will be retained.

    Returns:
        list[dict]: A deduplicated list of dictionaries.

    Example:
        input_list = [
            {'id': 1, 'name': 'Alice', 'age': 30},
            {'id': 2, 'name': 'Bob', 'age': 25},
            {'id': 3, 'name': 'Alice', 'age': 30},
            {'id': 4, 'name': 'Carol', 'age': 28},
        ]
        keys_to_check = ['name', 'age']

        deduplicated = deduplicate_list_of_dicts(input_list, keys_to_check)

        Result:
        [
            {'id': 1, 'name': 'Alice', 'age': 30},
            {'id': 2, 'name': 'Bob', 'age': 25},
            {'id': 4, 'name': 'Carol', 'age': 28},
        ]

    Note:
        - The function preserves the order of dictionaries in the input list.
        - Dictionaries with the same values for all specified keys are considered duplicates
          and only the first occurrence is retained.
    """
    seen = set()
    deduplicated_list = []
    
    for d in input_list:
        dict_subset = {key: d[key] for key in keys_to_check if key in d}
        dict_tuple = tuple(dict_subset.items())
        
        if dict_tuple not in seen:
            seen.add(dict_tuple)
            deduplicated_list.append(d)
    
    return deduplicated_list


def clean_model_generated_text(text):
    """
    This function takes model-generated text as input and performs text cleaning operations to improve readability and remove redundancy. 
    It performs the following tasks:

    1. Removes extra whitespace and newline characters:
    - It splits the input text into words using whitespace as a separator.
    - It then joins these words back together with a single space as a separator, effectively removing extra whitespace.

    2. Removes repeated sentences:
    - It splits the input text into sentences based on common sentence-ending punctuation (periods, question marks, and exclamation points).
    - It identifies and retains only the unique sentences from the split text, removing any duplicate sentences.
    - It joins the unique sentences back together into a single string.

    Parameters:
        - text (str): The input text that requires cleaning.

    Returns:
        str: The cleaned text with extra whitespace removed and redundant sentences removed, resulting in improved readability.

    Example:
        >>> input_text = "This is an example. This is an example. This is an example?"
        >>> cleaned_text = clean_model_generated_text(input_text)
        >>> print(cleaned_text)
        "This is an example. This is an example?"
    """

    # Remove extra whitespace and newline characters
    text = ' '.join(text.split())

    # Remove repeated sentences
    sentences = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?|\!)\s', text)
    
    unique_sentences = []
    for sentence in sentences:
        if sentence not in unique_sentences:
            unique_sentences.append(sentence)
            
    cleaned_text = ' '.join(unique_sentences)
    return cleaned_text


def print_number_of_trainable_model_parameters(model):
    """
    Calculate and print the number of trainable parameters in a PyTorch model.

    Parameters:
    model (torch.nn.Module): The PyTorch model for which you want to count trainable parameters.

    Returns:
    str: A string containing information about the trainable and total parameters, 
         as well as the percentage of trainable parameters.

    Example:
    >>> model = YourPyTorchModel()
    >>> result = print_number_of_trainable_model_parameters(model)
    >>> print(result)
    trainable model parameters: 123456
    all model parameters: 789012
    percentage of trainable model parameters: 15.65%
    """
        
    trainable_model_params = 0
    all_model_params = 0
    
    for _, param in model.named_parameters():
        all_model_params += param.numel()
        
        if param.requires_grad:
            trainable_model_params += param.numel()
    
    return f"trainable model parameters: {trainable_model_params}\nall model parameters: {all_model_params}\npercentage of trainable model parameters: {100 * trainable_model_params / all_model_params:.2f}%"
