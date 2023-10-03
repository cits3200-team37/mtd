FROM python:3.11-slim

# Allow statements and log messages to immediately appear in the logs
ENV PYTHONUNBUFFERED True

WORKDIR /server

COPY ./runtime.sh /runtime.sh

RUN chmod +x /runtime.sh

COPY ./ ./

RUN pip install -r requirements.txt

CMD [ "/runtime.sh" ]
