from app.domain import MLModel, PredictionRequest, PredictionResponse
from app.repositories import LogRepository, ModelRepository


class PredictionUseCase:
    def __init__(
        self, model_repository: ModelRepository, log_repository: LogRepository
    ):
        self.model_repository = model_repository
        self.log_repository = log_repository

    def execute(self, request_data: dict) -> PredictionResponse:
        model = self.model_repository.get_model()
        ml_model = MLModel(model)

        request = PredictionRequest(**request_data)

        prediction_result = ml_model.predict({"Er": request.Er, "Sigma": request.Sigma})

        self.log_repository.log_request(request_data)
        self.log_repository.log_response({"result": prediction_result})

        return PredictionResponse(result=prediction_result)
