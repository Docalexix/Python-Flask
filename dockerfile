FROM python:alpine

WORKDIR /app

COPY app.py ./
COPY templates templates/
COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5001

# Run app.py when the container launches forreal
CMD ["python", "app.py"]