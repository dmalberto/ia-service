from flask import Flask, jsonify, request

from app.infra.config import Config
from app.repositories import LogRepository, ModelRepository
from app.use_cases import PredictionUseCase

app = Flask(__name__)

model_repository = ModelRepository(Config.db_url)
log_repository = LogRepository(Config.db_url)


@app.route("/predict", methods=["POST"])
def predict():
    request_data = request.get_json()

    prediction_use_case = PredictionUseCase(model_repository, log_repository)

    try:
        response = prediction_use_case.execute(request_data)
        return jsonify(response), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
