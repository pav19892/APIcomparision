FROM python:3.11-slim
MAINTAINER Pavankumar Panchal(pav19892@gmail.com)

WORKDIR /app

COPY ./apptask.py /app/apptask.py
COPY ./requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

EXPOSE 8013

ENTRYPOINT [ "python"]

CMD ["-u","apptask.py"]
