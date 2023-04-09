FROM ubuntu:focal

RUN apt-get update
RUN apt-get install -y python3 python3-pip

RUN pip3 install flask
#RUN pip3 install flask-mysql

# set the working directory in the container
WORKDIR /opt/source-code
COPY . .


# run the command
CMD ["python3", "app.py"]
