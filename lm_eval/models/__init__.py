from . import local

MODEL_REGISTRY = {
    "local": local.Local
}


def get_model(model_name):
    return MODEL_REGISTRY[model_name]
