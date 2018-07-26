# Python Docker Test

## Testing Flask Server

## Run with Docker
```bash
docker build -t run.py .
docker run -it --rm -p 3000:3000 --name run.py run.py
```

## Using docker-compose
```bash
docker build -t run.py .
docker-compose up
...
docker-compose down
```
