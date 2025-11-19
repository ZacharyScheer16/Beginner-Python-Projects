# Base Image: A lean version of Python 3.11
FROM python:3.11-slim

# Set Working Directory: /app is the standard place for application code
WORKDIR /app

# Matplotlib Fix: Use the 'Agg' backend to save plots as files (instead of showing a GUI)
ENV MPLBACKEND=Agg

# 1. CREATE requirements.txt inside the container and add packages
RUN echo "numpy" > requirements.txt && \
    echo "pandas" >> requirements.txt && \
    echo "matplotlib" >> requirements.txt

# 2. Install System and Python Dependencies
# We chain the system install (gcc), pip install, and cleanup steps together.
RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc && \
    pip install --no-cache-dir -r requirements.txt && \
    apt-get purge -y gcc && \
    apt-get autoremove -y && \
    rm -rf /var/lib/apt/lists/*

# 3. Copy Application Code: Copies all your .py files (respecting .dockerignore)
COPY . .

# 4. Default Command: Start the Python interpreter when the container runs
CMD ["python"]