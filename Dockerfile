FROM mcr.microsoft.com/playwright/python:v1.62.0-noble

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Default command: the smoke tests in Chromium (can be overridden at docker run)
CMD ["python", "-m", "pytest", "tests/test_1.py", "tests/test_2.py", "tests/test_3.py", \
     "-m", "smoke", "--browser", "chromium", "-v", "--tb=short"]