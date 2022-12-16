FROM python:3.10-alpine
ENV PYTHONUNBUFFERED=1
ENV PYTHONIOENCODING=UTF-8
WORKDIR /usr/src/app
COPY run.py .
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN mkdir /root/.aws
COPY credentials /root/.aws/credentials
CMD ["python", "run.py"]
