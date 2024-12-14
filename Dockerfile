# Use Python as the base image...
FROM python:3.9-slim

# Set the working directory inside the container...
WORKDIR / app

# Setting up an environment...
ENV FAST_API = main.py
ENV API_PORT = 8000

# Copying al the file into / app
COPY . . 

# Install Python dependencies...
RUN pip install -r requirements.txt

# Expose the port for FastAPI...(container will listen to this port..)
EXPOSE 8000

# Default command: run FastAPI...
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]

