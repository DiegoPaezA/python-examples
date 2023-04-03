FROM ubuntu:focal

ENV USER mpitest
ENV HOME /home/$USER
WORKDIR $HOME

# Install any necessary packages
RUN apt-get update && apt-get install -y \
    # Add any necessary packages here
    && rm -rf /var/lib/apt/lists/*
# Copy the script to the container


COPY ./script.sh $HOME/
RUN chmod +x $HOME/script.sh
# Set the entrypoint to the script with CMD arguments

CMD ["sh", "script.sh"]
