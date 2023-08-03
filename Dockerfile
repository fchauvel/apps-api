FROM python:3.10-alpine

WORKDIR apps-api
COPY ./setup.py ./
COPY ./src ./

RUN pip install --no-cache-dir .

CMD ["uvicorn", "--app-dir", "src", "appsapi.runner:app", "--host", "0.0.0.0", "--port", "8000"]
