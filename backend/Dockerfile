FROM python:alpine3.7

ENV PYTHONDONTWRITEBYTECODE=1 \
	LANG=C.UTF-8 \
	LC_ALL=C.UTF-8
CMD [ $CI ] && export FLASK_ENV=production || export FLASK_ENV=development; cd /app; pip3 install -r requirements.txt && python3 main.py

EXPOSE 5000
