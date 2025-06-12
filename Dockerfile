# Base Python image
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy everything into the container
COPY . .

# Set PYTHONPATH for module resolution
ENV PYTHONPATH=/app

# Install dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Run tests with coverage
CMD ["pytest", "--cov=rcb_stats", "--cov-report=term", "tests/"]
