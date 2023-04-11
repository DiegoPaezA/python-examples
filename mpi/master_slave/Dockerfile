FROM ubuntu:focal-20230308

ENV USER mpitest
ENV HOME /home/$USER
ENV DEBIAN_FRONTEND noninteractive

RUN apt update && apt install -y tcl

RUN apt-get update && \
    apt-get install -y openmpi-bin libopenmpi-dev python3 python3-pip && \
    pip3 install mpi4py

COPY requirements.txt $HOME/requirements.txt
RUN pip3 install --no-cache-dir -r $HOME/requirements.txt

# set the working directory in the container
WORKDIR $HOME
COPY /code $HOME/code

WORKDIR $HOME/code

RUN chmod +x run.sh

RUN useradd -ms /bin/bash $USER
USER $USER


CMD ["sh", "run.sh"]
