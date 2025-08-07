# Dockerfile
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    default-libmysqlclient-dev gcc \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy Django project (EXCLUDING static/)
COPY . .

# Expose port
EXPOSE 8000

# Run Django dev server (not for production!)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
