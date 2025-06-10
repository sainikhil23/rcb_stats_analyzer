# Base image with Python 3.12
FROM python:3.12-slim

# Set the working directory
WORKDIR /app

# Copy all files into the container
COPY . .

# Set PYTHONPATH so Python can find rcb_stats
ENV PYTHONPATH=/app

# Install dependencies
RUN pip install --upgrade pip && pip install pytest

# Default command to run tests
CMD ["pytest"]
