FROM ubuntu:latest
LABEL authors="zsche"

# Install Python and pip
RUN apt-get update && apt-get install -y python3 python3-pip && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy project files
COPY . .

# Install dependencies if requirements.txt exists
RUN if [ -f requirements.txt ]; then pip3 install --no-cache-dir -r requirements.txt; fi

# Install Jupyter
RUN pip3 install jupyter

# Run notebook via nbconvert
CMD ["jupyter", "nbconvert", "--to", "script", "Covid19.ipynb", "--execute"]
