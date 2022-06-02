FROM python:3.8

ADD input.py /src/pv_meter/input.py
ADD Meter.py /src/pv_meter/Meter.py
ADD Broker_Producer.py /src/pv_meter/Broker_Producer.py
ADD RabbitBroker.py /src/pv_meter/RabbitBroker.py
ADD requirements.txt /src

WORKDIR /src

RUN pip install -r requirements.txt

ENTRYPOINT ["python", "-m", "pv_meter"]