FROM python:3.11-slim

WORKDIR /app

# System dependencies (ffmpeg, aria2, mp4decrypt, wget, unzip)
RUN apt-get update && apt-get install -y \
    ffmpeg \
    aria2 \
    wget \
    unzip \
    && rm -rf /var/lib/apt/lists/*

# Install Bento4 (mp4decrypt)
RUN wget https://www.bento4.com/downloads/Bento4-SDK-1-6-0-641.x86_64-unknown-linux.zip && \
    unzip Bento4-SDK-1-6-0-641.x86_64-unknown-linux.zip && \
    cp Bento4-SDK-1-6-0-641.x86_64-unknown-linux/bin/mp4decrypt /usr/local/bin/ && \
    chmod +x /usr/local/bin/mp4decrypt

# Copy requirements file (rename sainibots.txt to requirements.txt)
COPY sainibots.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy all source code
COPY . .

# Start command: runs Flask (foreground) and bot (background thread inside app.py)
CMD ["python3", "app.py"]
