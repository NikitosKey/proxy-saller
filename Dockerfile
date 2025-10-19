FROM python:3.13-alpine
COPY --from=docker.io/astral/uv:latest /uv /uvx /bin/
WORKDIR /app
COPY . /app
CMD [ "uv", "run", "python", "-m", "bot.core.main" ]
