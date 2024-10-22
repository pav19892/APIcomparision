FROM python:3.11-slim
MAINTAINER Pavankumar Panchal(pav19892@gmail.com)

WORKDIR /app

COPY ./apptask.py /app/apptask.py
COPY ./requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

EXPOSE 8015

ENTRYPOINT [ "python", "-m","uvicorn"]

CMD ["apptask:app", "--host", "0.0.0.0", "--port", "8015", "--reload"]
