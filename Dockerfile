# Use official Python image
FROM python:3.9-slim

# Set work directory
WORKDIR /app

# Copy project files
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the Flask port
EXPOSE 5000

# Run the app
CMD ["python", "app.py"]


VOLUME /app/app.log
