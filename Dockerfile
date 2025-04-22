# Base stage
# Use official Python runtime as the base image
FROM python:3.13-slim AS base

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set work directory
WORKDIR /app

# Install system dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    # postgresql-client \
    gcc \
    python3-dev \
    musl-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Expose port
EXPOSE 8000

# Development stage
FROM base AS development
ENV DJANGO_SETTINGS_MODULE=MenuBackend.settings.dev
# Copy project files
COPY . .
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

# Production stage

# Run migrations
RUN python manage.py migrate
FROM base AS production
ENV DJANGO_SETTINGS_MODULE=MenuBackend.settings.prod
# Copy project files
COPY . .
# Collect static files
RUN python manage.py collectstatic --noinput
# Start the application
CMD ["gunicorn", "MenuBackend.wsgi:application", "--bind", "0.0.0.0:8000"]
