# Usa uma imagem base oficial do Python.
# Estamos escolhendo uma versão Alpine, que é menor e mais leve.
FROM python:3.9-alpine

# Define o diretório de trabalho dentro do contêiner.
# Todos os comandos subsequentes (COPY, RUN, CMD) serão executados a partir deste diretório.
WORKDIR /app

# Copia o arquivo requirements.txt para o diretório de trabalho do contêiner.
# Isso é feito separadamente para aproveitar o cache de camadas do Docker:
# se requirements.txt não mudar, esta camada não precisará ser reconstruída.
COPY ../app/requirements.txt .

# Instala as dependências Python.
# O --no-cache-dir garante que não sejam criados arquivos de cache, economizando espaço.
# O --upgrade pip garante que o pip esteja atualizado.
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copia todo o restante do código da aplicação para o diretório de trabalho do contêiner.
# O primeiro '.' é o contexto de build no host (o diretório atual: docker/).
# O segundo '.' é o diretório de destino no contêiner (/app, definido por WORKDIR).
# A pasta 'app' do seu projeto no host vai ser copiada para '/app/app' no contêiner.
COPY ../app/ .

# Expõe a porta que a aplicação Flask vai usar.
# Isso apenas documenta a porta, não a mapeia para o host ainda.
EXPOSE 5000

# Comando para iniciar a aplicação quando o contêiner for executado.
# Executa o script app.py usando o interpretador python.
CMD ["python", "app.py"]
