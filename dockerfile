# Dockerfile
FROM python:3.10-slim

WORKDIR /app

# Copy files
COPY . /app

# Install dependencies
RUN pip install flask

# Expose port
EXPOSE 5000

# Run app
CMD ["python", "app.py"]



