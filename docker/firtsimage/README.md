# Firts Docker Image

This is a simple example of a Docker image.

Check the [Dockerfile](Dockerfile) for more details.

---

## Build the image

```bash
docker build -t webapp .
```

## Run the container

```bash
docker run -d -p 80:5000 webapp
```
