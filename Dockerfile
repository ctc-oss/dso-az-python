FROM python:3.9

ENV PYTHONPATH=/opt/src

WORKDIR /opt/src
COPY . /opt/src

RUN python -m pip install -r requirements.txt --no-cache-dir

ENTRYPOINT ["python", "-m", "dso_az_python"]
