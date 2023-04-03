FROM ubuntu:focal-20230308

ENV USER mpitest
ENV HOME /home/$USER
ENV DEBIAN_FRONTEND noninteractive

WORKDIR $HOME
COPY . .

RUN apt update && apt install -y tcl

RUN apt-get update && \
    apt-get install -y openmpi-bin libopenmpi-dev python3 python3-pip && \
    pip3 install mpi4py && \
    pip3 install --no-cache-dir -r requirements.txt 

RUN chmod +x $HOME/run.sh

RUN useradd -ms /bin/bash $USER
USER $USER


CMD ["sh", "run.sh"]
