FROM ubuntu:focal

ENV USER mpitest
ENV HOME /home/$USER
ENV MPI_DIR=/opt/ompi
ENV PATH="$MPI_DIR/bin:$HOME/.local/bin:$PATH"
ENV LD_LIBRARY_PATH="$MPI_DIR/lib:$LD_LIBRARY_PATH"
WORKDIR $HOME

# Install any necessary packages
RUN apt-get update && apt-get install -y \
    # Add any necessary packages here
    && rm -rf /var/lib/apt/lists/*
# Copy the script to the container


COPY ./script.sh WORKDIR/
RUN chmod +x WORKDIR/script.sh
# Set the entrypoint to the script with CMD arguments

CMD ["sh", "WORKDIR/script.sh"]
