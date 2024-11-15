FROM python
MAINTAINER ARUN <arunvela@cdac.in>
COPY . /tmp/app
RUN pip3 install flask
EXPOSE 5000
ENV FLASK_APP=app.py
#create a webserver and sleep forever
CMD ["python3","/tmp/app/app.py"]
