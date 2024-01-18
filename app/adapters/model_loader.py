import pickle


class ModelLoader:
    @staticmethod
    def load_model(model_path):
        try:
            with open(model_path, "rb") as file:
                return pickle.load(file)
        except Exception as e:
            raise ValueError(f"Não foi possível carregar o modelo: {e}")
