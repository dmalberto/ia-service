from pydantic import BaseModel, Field


class PredictionRequest(BaseModel):
    Er: float = Field(..., description="Descrição do campo Er")
    Sigma: float = Field(..., description="Descrição do campo Sigma")


class PredictionResponse(BaseModel):
    result: float = Field(..., description="Resultado da previsão")
