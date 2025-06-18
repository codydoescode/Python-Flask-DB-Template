FROM python:3.11-slim AS builder

RUN useradd -m flaskuser

WORKDIR /app

USER root
RUN apt-get update && \
    apt-get install -y curl gnupg2 unixodbc-dev gcc g++ lsb-release git && \
    curl https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor -o /usr/share/keyrings/microsoft-archive-keyring.gpg && \
    echo "deb [signed-by=/usr/share/keyrings/microsoft-archive-keyring.gpg] https://packages.microsoft.com/debian/12/prod bookworm main" > /etc/apt/sources.list.d/mssql-release.list && \
    apt-get update && ACCEPT_EULA=Y apt-get install -y msodbcsql18 && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

RUN chown -R flaskuser:flaskuser /app

USER flaskuser

CMD ["sh", "-c", "gunicorn -b 0.0.0.0:${APP_PORT:-5000} app:app"]
