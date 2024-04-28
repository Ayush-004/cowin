FROM python:3.12




WORKDIR /

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "./state_wise_dose.py"]

