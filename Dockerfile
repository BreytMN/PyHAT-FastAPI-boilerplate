FROM python:3.12.1-slim-bullseye

ENV PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=on \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    APP_PATH="/opt/app" \
    APP="app"

WORKDIR $APP_PATH

COPY requirements.txt ${APP_PATH}/
RUN pip install --root-user-action=ignore \
        -r requirements.txt; \
    rm requirements.txt; \
    tailwindcss_install;

COPY ${APP}/ *.env ${APP_PATH}/

ENTRYPOINT ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--lifespan", "on"]
