# Use a imagem base Python
FROM python:3.9

# Defina o diretório de trabalho no contêiner
WORKDIR /app

# Copie o script Python para o contêiner
COPY src /app

# Instale as dependências do Python (incluindo pandas)
RUN pip install pandas sqlalchemy psycopg2-binary openpyxl

# Comando a ser executado quando o contêiner for iniciado
CMD ["python", "main.py"]