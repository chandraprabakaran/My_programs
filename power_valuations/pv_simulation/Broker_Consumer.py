import sys
sys.path.append("/Users/chandru/rabbit/PV/pv_simulation")

from aio_pika import IncomingMessage


class Consumer_connection:
    def start_consuming_power_value(self) -> None:
        """Read messages from the broker"""
        pass

    def close_connection(self):
        """Close connection"""
        pass

    def on_message(self, message: IncomingMessage):
        """
        Callback function for message receive
        """

class Broker_connection:
    def connect_to_server(self):
       
        pass

    def publish(self, value: str):
       
        pass

    def register_consumer(self, consumer: Consumer_connection):
      
        pass

    def close_connection(self):
       
        pass
