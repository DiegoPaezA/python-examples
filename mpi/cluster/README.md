# Docker Cluster for OpenMPI and mpi4py

This repository contains a Dockerfile for building a Docker image with OpenMPI and mpi4py installed. The image is based on the official Ubuntu 20.04 image.

## Building the image

To build the image, run the following command:

```
docker build -t cluster_mpi .
```

## Running the image with docker compose

To run the image with docker compose, run the following command:

```
docker-compose up -d
```
