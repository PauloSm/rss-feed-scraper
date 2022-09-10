FROM python:3.8

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV PYTHONPATH "${PYTHONPATH}:../"

CMD ["python", "./system/main.py"]
