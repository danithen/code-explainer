FROM python:3.12-slim

WORKDIR /app

RUN pip install --no-cache-dir uv

COPY pyproject.toml uv.lock ./

RUN uv sync --frozen --no-dev --no-install-project

COPY app.py ./
COPY .streamlit ./.streamlit

EXPOSE 8501

CMD ["/app/.venv/bin/streamlit", "run", "app.py"]