FROM python:alpine3.7

ENV PYTHONDONTWRITEBYTECODE=1 \
	LANG=C.UTF-8 \
	LC_ALL=C.UTF-8
CMD [ $CI ] && export FLASK_ENV=production || export FLASK_ENV=development; \
        cd /app; pip3 install -r requirements.txt && \
        if [ $CI ]; then coverage3 run --branch main.py; \
        else python3 main.py; fi

EXPOSE 5000
