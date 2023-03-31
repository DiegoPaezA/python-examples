FROM ubuntu:20.04

ENV DEBIAN_FRONTEND noninteractive

RUN apt update && apt install -y tcl

RUN apt-get update && \
    apt-get install -y openmpi-bin libopenmpi-dev python3 python3-pip && \
    pip3 install mpi4py

RUN useradd -ms /bin/bash mpiuser
USER mpiuser

WORKDIR /home/mpiuser

COPY . /app
WORKDIR /app

CMD ["mpirun", "-n", "4", "python3", "pi_mpi.py"]