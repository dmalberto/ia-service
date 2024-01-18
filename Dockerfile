# Dockerfile
FROM python:3.8

# Configura o diretório de trabalho dentro do container
WORKDIR /app

# Copia os arquivos de requisitos e instala as dependências do Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia o resto do seu código para o diretório de trabalho
COPY . .

# Define a variável de ambiente para o Flask (ajuste conforme necessário)
ENV FLASK_APP=app/main.py
ENV FLASK_RUN_HOST=0.0.0.0

# Expõe a porta em que o Flask será executado
EXPOSE 5000

# Comando para iniciar a aplicação
CMD ["flask", "run"]
