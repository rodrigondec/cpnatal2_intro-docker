FROM python:3.7
ENV PYTHONUNBUFFERED 1

WORKDIR /

ADD server.py /main.py
ADD requirements.txt /requirements.txt

RUN pip install -r requirements.txt

CMD [ "python", "./main.py" ]