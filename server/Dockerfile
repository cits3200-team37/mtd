FROM python:3.11

WORKDIR /server

COPY ./runtime.sh /runtime.sh

RUN chmod +x /runtime.sh

COPY ./ ./

RUN pip install -r requirements.txt

CMD [ "/runtime.sh" ]
