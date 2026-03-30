# FROM apache/airflow:2.6.0
FROM apache/airflow:3.1.8
COPY requirements.txt /
RUN pip install --no-cache-dir -r /requirements.txt