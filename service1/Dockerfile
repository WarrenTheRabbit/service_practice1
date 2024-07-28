FROM python:3.12-slim

WORKDIR /app

RUN ls
COPY poetry.lock pyproject.toml ./
RUN pip install poetry && poetry config virtualenvs.create false 
RUN poetry install --no-dev   

COPY . /app

CMD ["poetry", "run", "uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]