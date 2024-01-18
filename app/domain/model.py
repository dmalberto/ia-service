class MLModel:
    def __init__(self, model):
        self.model = model

    def predict(self, input_data):
        try:
            return self.model.predict([input_data])
        except Exception as e:
            raise ValueError(f"Erro ao realizar previsão: {e}")
