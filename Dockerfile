FROM python:3.12

WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip && \
    pip cache purge && \
    echo "=== BEFORE INSTALL ===" && \
    pip list | grep redis || echo "Redis not found" && \
    echo "=== INSTALLING REQUIREMENTS ===" && \
    pip install --no-cache-dir -r requirements.txt && \
    echo "=== AFTER REQUIREMENTS ===" && \
    pip list | grep redis && \
    echo "=== FORCE REINSTALL REDIS ===" && \
    pip uninstall redis -y && \
    pip install --no-cache-dir redis==5.0.1 && \
    echo "=== FINAL STATE ===" && \
    pip list | grep redis && \
    echo "=== CHECKING REDIS VERSION ===" && \
    python -c "import redis; print(f'Redis version: {redis.__version__}'); print(f'Redis file: {redis.__file__}')"


COPY . .

ENV PYTHONPATH=/app:/app/app

CMD ["python", "app/main.py"]