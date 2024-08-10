FROM python:3.10

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . /app

# Expose any necessary ports
EXPOSE 8080

# Run the Bittensor neuron
CMD ["python", "bittensor_integration/neuron.py"]