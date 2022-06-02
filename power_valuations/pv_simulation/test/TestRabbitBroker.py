
import unittest
import sys
sys.path.append("/Users/chandru/rabbit/PV/pv_simulation")
from pv_simulation.RabbitBroker import RabbitBroker
import asyncio
from pv_simulation.Broker_Consumer import Consumer_connection
from aio_pika import IncomingMessage


class TestRabbitMQAsyncBroker(unittest.TestCase):
    __broker_address = "amqp://guest:guest@localhost"
    __broker_queue_name = "power"
    __message = "Hi there"

    def test_connect_to_server(self):
        rabbitmq = RabbitBroker(self.__broker_address, self.__broker_queue_name)
        try:
            loop = asyncio.get_event_loop()
            loop.run_until_complete(rabbitmq.connect_to_server())
            self.assertTrue(True)
        except ConnectionError:
            self.assertTrue(False)

    def test_publish(self):
        rabbitmq = RabbitBroker(self.__broker_address, self.__broker_queue_name)

        try:
            loop = asyncio.get_event_loop()
            loop.run_until_complete(rabbitmq.connect_to_server())
            loop.run_until_complete(rabbitmq.publish(self.__message))
            self.assertTrue(True)
        except Exception:
            self.assertTrue(False)

    def test_publish_without_connection(self):
        rabbitmq = RabbitBroker(self.__broker_address, self.__broker_queue_name)

        try:
            loop = asyncio.get_event_loop()
            loop.run_until_complete(rabbitmq.publish(self.__message))
            self.assertTrue(False)
        except AttributeError:
            self.assertTrue(True)

    def test_close_connection(self):
        rabbitmq = RabbitBroker(self.__broker_address, self.__broker_queue_name)

        try:
            loop = asyncio.get_event_loop()
            loop.run_until_complete(rabbitmq.connect_to_server())
            loop.run_until_complete(rabbitmq.close_connection())
            self.assertTrue(True)
        except Exception:
            self.assertTrue(False)

    def test_close_connection_without_connection(self):
        rabbitmq = RabbitBroker(self.__broker_address, self.__broker_queue_name)

        try:
            loop = asyncio.get_event_loop()
            loop.run_until_complete(rabbitmq.close_connection())
            self.assertTrue(False)
        except AttributeError:
            self.assertTrue(True)

    def test_register_consumer(self):
        dummy_consumer = DummyConsumer()
        rabbitmq = RabbitBroker(self.__broker_address, self.__broker_queue_name)
        try:
            loop = asyncio.get_event_loop()
            loop.run_until_complete(rabbitmq.connect_to_server())
            loop.run_until_complete( rabbitmq.register_consumer(dummy_consumer))
            loop.close()
            self.assertTrue(dummy_consumer.callback_executed)
        except AttributeError:
            self.assertTrue(False)


class DummyConsumer(Consumer_connection):
    callback_executed = False

    async def on_message(self, message: IncomingMessage):
        self.callback_executed = True
