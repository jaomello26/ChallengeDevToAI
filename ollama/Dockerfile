FROM ubuntu:22.04

RUN apt-get update && apt-get install -y \
    curl \
    ca-certificates

RUN curl -o- https://ollama.ai/install.sh | bash

ENV PATH="/root/.ollama/bin:${PATH}"

# Inicia o Ollama e puxa o modelo após garantir que o serviço está ativo
CMD ["sh", "-c", "ollama serve & sleep 5 && ollama pull llama2 && tail -f /dev/null"]
