FROM ubuntu:latest
WORKDIR /app

RUN apt update
RUN apt-get update && apt-get install -y libx11-6 libxext-dev libxinerama-dev libxrandr-dev libxcursor-dev tk-dev
RUN apt-get install tk -y
COPY . .
# COPY requirements.txt /app/requirements.txt
# COPY todo.py ./

CMD ["python3", "todo.py"]