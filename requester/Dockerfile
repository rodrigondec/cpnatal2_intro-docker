FROM python:3.7

WORKDIR /

ADD requester.py /main.py
ADD requirements.txt /requirements.txt

RUN pip install -r requirements.txt

CMD [ "python", "./main.py" ]