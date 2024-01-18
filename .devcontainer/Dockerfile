# .devcontainer/Dockerfile
FROM python:3.8-slim

# Evita que Python escreva arquivos .pyc no disco (equivalente a python -B opção)
ENV PYTHONDONTWRITEBYTECODE 1

# Evita que Python armazene em buffer as saídas, imprimindo-as diretamente
ENV PYTHONUNBUFFERED 1

# Instala dependências de sistema
RUN apt-get update \
    && apt-get install -y --no-install-recommends build-essential libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Configura o diretório de trabalho
WORKDIR /workspace

# Copia o arquivo requirements.txt e instala as dependências do Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia o resto do seu código para o diretório de trabalho
COPY . .
