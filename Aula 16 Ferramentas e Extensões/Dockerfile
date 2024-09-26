FROM python:3.11.0-slim

WORKDIR /app

# COPY . . (all files)
COPY pipeline.py . 
COPY listing_status.csv .

RUN pip install -r requirements.txt

CMD ["python", "pipeline.py"]