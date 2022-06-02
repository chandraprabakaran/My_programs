"""
PV meter Broker connection
"""

class Broker_connection:
    def connect_to_server(self):
        pass

    def publish(self, value: str):
        pass

    def register_consumer(self, consumer):
        pass

    def close_connection(self):
        pass


class Producer_connection:
    def connect_with_broker(self):
        pass

    def publish_message(self, power_value: int) -> None:
        pass

    def close_connection(self):
        pass
