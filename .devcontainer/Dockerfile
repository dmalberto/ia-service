# .devcontainer/Dockerfile
FROM python:3.8

# Evita que Python escreva arquivos .pyc no disco (equivalente a python -B opção)
ENV PYTHONDONTWRITEBYTECODE 1

# Evita que Python armazene em buffer as saídas, imprimindo-as diretamente no terminal
ENV PYTHONUNBUFFERED 1

# Instala dependências do sistema
RUN apt-get update \
    && apt-get -y install libpq-dev gcc

# Instala dependências do Python
COPY requirements.txt /tmp/pip-tmp/
RUN pip --disable-pip-version-check --no-cache-dir install -r /tmp/pip-tmp/requirements.txt \
    && rm -rf /tmp/pip-tmp
