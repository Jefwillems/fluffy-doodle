# Use the official Python base image
FROM python:3.12.4-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file to the container
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Python file to the container
COPY server.py .

# Set the command to run your Python file
CMD ["fastapi", "run", "server.py", "--port", "8080"]