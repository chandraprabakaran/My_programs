
import sys
sys.path.append("/Users/chandru/rabbit/PV/pv_simulation")
from pv_simulation.Broker_Consumer import Consumer_connection
from pv_simulation.csv_files import FileWriter
from datetime import datetime
from aio_pika import IncomingMessage
import logging
from pv_simulation.Broker_Consumer import Broker_connection


def combine_power_values(power_value_from_broker: int, generated_power_value: int) -> int:
    return power_value_from_broker + generated_power_value


class simulator(Consumer_connection):
    __csv_filer_writer = FileWriter
    __power_value_generator = None

    __broker_address = ""
    __broker_queue_name = ""
    __broker_queue = object

    def __init__(self, min_power_value: int,
                 max_power_value: int, simulator_pv_generator, broker: Broker_connection, csv_filer_writer: FileWriter):

        # initialize broker
        self.__broker = broker
        # initialize output file
        self.__csv_filer_writer = csv_filer_writer
        # initialize simulator pv generator
        self.__min_power_value = min_power_value
        self.__max_power_value = max_power_value
        self.__simulator_pv_generator = simulator_pv_generator
        logging.info("PVSimulator properties are initialized with Min PV: %s, Max PV: %s", self.__min_power_value,
                     self.__max_power_value)

    async def connect_with_broker(self):
        await self.__broker.connect_to_server()

    async def start_consuming_power_value(self) -> None:
        # Start listening the queue
        await self.__broker.register_consumer(self)

    async def on_message(self, message: IncomingMessage):
        simulator_power_value = self.generate_power_value()
        if simulator_power_value > 0:
            try:
                meter_power_value = int(message.body.decode('utf-8'))
                logging.debug("Received Meter Power Value %s", meter_power_value)
                await self.write_power_value(meter_power_value, simulator_power_value,
                                             combine_power_values(meter_power_value, simulator_power_value))
            except ValueError as te:
                logging.error("Unable to convert received value to int", te)

    def generate_power_value(self) -> int:
        """Generates random simulator power value
        """
        power_value = self.__simulator_pv_generator(self.__min_power_value, self.__max_power_value + 1)
        logging.debug("Generated power value %s", power_value)
        if power_value in range(self.__min_power_value, self.__max_power_value + 1):
            return power_value
        else:
            logging.error("Generated power value is outside of the range of %s-%s", self.__min_power_value,
                          self.__max_power_value)
            return -1

    async def write_power_value(self, meter_power_value: int, simulated_power_value: int,
                                combined_power_value: int) -> None:

        await self.__csv_filer_writer.write(datetime.now(), meter_power_value, simulated_power_value,
                                            combined_power_value)

    async def close_connection(self):
        await self.__broker.close_connection()
