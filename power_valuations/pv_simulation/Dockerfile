FROM python:3.8

ADD output.py /src/pv_simulation/output.py
ADD Consumer.py /src/pv_simulation/Consumer.py
ADD simulator.py /src/pv_simulation/simulator.py
ADD csv_files.py /src/pv_simulation/csv_files.py
ADD Broker_Consumer.py /src/pv_simulation/Broker_Consumer.py
ADD RabbitBroker.py /src/pv_simulation/RabbitBroker.py
ADD requirements.txt /src

WORKDIR /src

RUN pip install -r requirements.txt

ENTRYPOINT ["python", "-m", "pv_simulation"]