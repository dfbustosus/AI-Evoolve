# Start with Ubuntu base image
FROM ubuntu:latest

# Install necessary packages
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-venv \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Install Ollama
RUN curl https://ollama.com/install.sh | sh

# Set up a virtual environment
ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Install Python dependencies in the virtual environment
RUN pip install requests

# Set working directory
WORKDIR /app

# Copy Python script
COPY script.py .

# Expose Ollama port
EXPOSE 11434

# Create a startup script
RUN echo '#!/bin/bash\nollama serve &\nsleep 10\nollama pull phi\npython /app/script.py' > /app/start.sh && \
    chmod +x /app/start.sh

# Set the startup script as the entry point
CMD ["/app/start.sh"]