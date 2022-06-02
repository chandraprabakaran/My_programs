
import sys
sys.path.append("/Users/chandru/rabbit/PV/pv_simulation")
from pv_simulation.simulator import simulator
from pv_simulation.csv_files import csv_files
import random
import logging
import os
from aio_pika.exceptions import AMQPConnectionError
import asyncio
from pv_simulation.RabbitBroker import RabbitBroker
import time


async def main():
    try:
        # get logfile location
        logfile = os.environ['logfile']
        # configure logging
        logging.basicConfig(filename=logfile, filemode="a", level=logging.INFO,
                            format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

        # read values from environment
        broker_address = os.environ['broker_address']
        broker_queue_name = os.environ['broker_msg_queue']
        min_pv = int(os.environ['min_pv'])
        max_pv = int(os.environ['max_pv'])
        initial_delay_second_for_broker_startup = int(os.environ['initial_delay_second_for_broker_startup'])

        logging.info("Broker address: %s, Message Queue: %s, Min_PV: %s Max_PV: %s",
                     broker_address, broker_queue_name, min_pv, max_pv)
         # get output file location
        file_store = os.environ['file_store']
        csv_file_writer = csv_files(file_store)

        broker = RabbitBroker(broker_address=broker_address, broker_queue_name=broker_queue_name)

        pv_simulator = simulator(broker= broker, min_power_value=min_pv, max_power_value=max_pv,
                                   simulator_pv_generator=lambda x, y: random.randrange(x, y),
                                   csv_filer_writer=csv_file_writer)
        try:
            # initial sleep for the broker to be ready
            time.sleep(initial_delay_second_for_broker_startup)
            # Connect with broker
            await pv_simulator.connect_with_broker()
            # start consuming power values
            await pv_simulator.start_consuming_power_value()
        except KeyboardInterrupt as key:
            logging.error("PVSimulator (Consumer) stopped: " + key.__str__())
        except AMQPConnectionError as amp:
            logging.error("Connection Error: ", amp)
        except Exception as error:
            logging.error("[Startup Error] Cannot start PVSimulator (Consumer): " + error.__str__())

    except KeyError as key_err:
        logging.error("[Startup Error] Unable to find env variable : " + key_err.__str__())
    except ValueError as value_err:
        logging.error("[Startup Error] Can not convert %s to int.", value_err.__str__())
    except TypeError as te:
        logging.error("[Startup Error] Type Error: ", te)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.create_task(main())
    loop.run_forever()
