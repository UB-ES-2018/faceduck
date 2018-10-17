FROM python:alpine3.7

CMD export PYTHONDONTWRITEBYTECODE=1; export FLASK_ENV=development; export LANG=C.UTF-8; export export LC_ALL=C.UTF-8; cd /app; pip3 install -r requirements.txt && python3 main.py

EXPOSE 5000
