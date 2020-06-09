FROM python:3.7

WORKDIR /app

COPY . /app

RUN python setup.py install
CMD ["python", "-m", "monitoring_scripts"]
