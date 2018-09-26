FROM ubuntu

RUN apt-get update && apt-get install -y python3 python3-pip

CMD export LANG=C.UTF-8; export export LC_ALL=C.UTF-8; cd /app; pip3 install -r requirements.txt && python3 main.py

EXPOSE 5000
