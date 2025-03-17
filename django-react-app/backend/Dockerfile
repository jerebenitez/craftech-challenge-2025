# Stage 1
FROM python:3.12-slim AS builder

RUN mkdir /app

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY requirements.txt entrypoint.sh /app/

RUN apt update && apt install -y libpq-dev python3-dev gcc && \
    pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Stage 2
FROM python:3.12-slim

RUN useradd -m -r appuser && \
    mkdir /app && \
    chown -R appuser /app && \
    apt update && apt install -y netcat-traditional libpq-dev

WORKDIR /app

COPY --from=builder /usr/local/lib/python3.12/site-packages/ /usr/local/lib/python3.12/site-packages/
COPY --from=builder /usr/local/bin/ /usr/local/bin/
COPY --chown=appuser:appuser . .

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

USER appuser

EXPOSE 8000

ENTRYPOINT ["./entrypoint.sh"]
