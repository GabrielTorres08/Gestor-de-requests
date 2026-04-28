FROM python:3.11-slim

# Evita gerar arquivos .pyc e buffer de logs
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Diretório de trabalho
WORKDIR /app

# Copia dependências primeiro (melhora cache)
COPY requirements.txt .

# Instala dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copia o resto do projeto
COPY . .

# Porta que o Flask vai rodar
EXPOSE 5000

# Comando para rodar o app
CMD ["gunicorn", "-b", "0.0.0.0:5000", "server:app"]