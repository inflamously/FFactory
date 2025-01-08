import ollama

from src.llm.llm import OllamaModelDescription


def list_models() -> list[OllamaModelDescription]:
    for key, models in ollama.list():
        return [OllamaModelDescription(model) for model in models]
    return []


def list_model_names() -> list[str]:
    return [model.name for model in list_models()]


def check_model(model):
    for model_description in list_models():
        existing_model_name, version = model_description.name.split(":")
        if model in existing_model_name: return True
    return False
