## Project Description
The PV_simulator challenge has mainly three modules Meter,Broker as rabbitmq and PV simulator.The power consumption with respect to time interval are stored in csv file.

### Meter:
The meter module produce random but continous values from 0 to 9000 watts .It sends the values as messages to the broker(rabbitmq).

### PV simulator:
It generates a simulated PV power value and listen to the broker(rabbitmq).In final stage it adds the meter value and output of the result.

### Writing to a file:
The results are stored in a csv file,with current timestamp,the meter value and power value of PV.

## How to run
To Run
docker-should be installed
docker-compose should be installed
rabbitmq should built as container


### Run Steps
docker ps
docker-compose up

 ## Output
 ### Logs
 the Pv output at pv.csv file which has the value of timestamp,the meter value power value and combined power value of PV.
