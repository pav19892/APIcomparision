FROM python:3.11-slim
MAINTAINER Pavankumar Panchal(pav19892@gmail.com)

WORKDIR /app

COPY ./locustfile.py /app/locustfile.py
COPY ./requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

EXPOSE 8011

ENTRYPOINT [ "python","-m","locust"]

CMD ["-f" ,"/app/locustfile.py","--web-host","0.0.0.0","--web-port","8011"]

