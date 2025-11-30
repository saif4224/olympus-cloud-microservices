# 1. Use a lightweight Python base image
FROM public.ecr.aws/docker/library/python:3.9-slim

# 2. Set the working directory inside the container
WORKDIR /app

# 3. Copy dependencies and install them
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Copy the application code
COPY . .

# 5. Expose the port the app runs on
EXPOSE 8080

# 6. Command to run the app
CMD ["python", "main.py"]