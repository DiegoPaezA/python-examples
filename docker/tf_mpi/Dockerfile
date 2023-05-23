FROM tensorflow/tensorflow:2.6.0-gpu

ENV USER mpitest
ENV HOME /home/$USER
ENV DEBIAN_FRONTEND noninteractive

RUN apt-key adv --fetch-keys https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1804/x86_64/3bf863cc.pub
RUN apt-key adv --fetch-keys https://developer.download.nvidia.com/compute/machine-learning/repos/ubuntu1804/x86_64/7fa2af80.pub
# Install OpenMPI
RUN apt update && \
    apt install --no-install-recommends -y build-essential software-properties-common tcl && \
    add-apt-repository -y ppa:deadsnakes/ppa && \
    apt install --no-install-recommends -y openmpi-bin libopenmpi-dev openssh-server && \
    #apt install --no-install-recommends -y python3 python3-pip python3-setuptools python3-distutils python3-dev && \
    pip3 install mpi4py && \
    apt clean && rm -rf /var/lib/apt/lists/*

RUN mkdir /var/run/sshd
RUN echo 'root:PASSWORD' | chpasswd
RUN sed -i 's/PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd
EXPOSE 22

COPY requirements.txt $HOME/requirements.txt
RUN python3 -m pip install --upgrade pip && \
    python3 -m pip install --no-cache-dir -r $HOME/requirements.txt

# set the working directory in the container
WORKDIR $HOME
COPY /code $HOME/code

WORKDIR $HOME/code

RUN chmod +x run.sh

RUN useradd -ms /bin/bash $USER
USER $USER


CMD ["sh", "run.sh"]
