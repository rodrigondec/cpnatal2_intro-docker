FROM python:3.7
ENV PYTHONUNBUFFERED 1

ADD server.py /main.py

RUN pip install flask

CMD [ "python", "./main.py" ]