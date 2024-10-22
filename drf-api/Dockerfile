FROM python:3.11-slim
MAINTAINER Pavankumar Panchal(pav19892@gmail.com)

WORKDIR /app

COPY ./django_api/ /app/django_api/

COPY ./requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

EXPOSE 8014

ENTRYPOINT [ "python" ]

CMD ["/app/django_api/manage.py" ,"runserver" ,"0.0.0.0:8014"]

