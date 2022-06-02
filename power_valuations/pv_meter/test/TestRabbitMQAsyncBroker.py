
import unittest
import sys
sys.path.append("/Users/chandru/rabbit/PV/pv_meter")
from pv_meter.RabbitBroker import AsyncBroker
import asyncio


class TestRabbitMQAsyncBroker(unittest.TestCase):
    __broker_address = "amqp://guest:guest@localhost"
    __broker_queue_name = "power"
    __message = "Hi there"

    def test_connect_to_server(self):
        rabbitmq = AsyncBroker(self.__broker_address, self.__broker_queue_name)
        try:
            loop = asyncio.get_event_loop()
            loop.run_until_complete(rabbitmq.connect_to_server())
            self.assertTrue(True)
        except ConnectionError:
            self.assertTrue(False)

    def test_publish(self):
        rabbitmq = AsyncBroker(self.__broker_address, self.__broker_queue_name)

        try:
            loop = asyncio.get_event_loop()
            loop.run_until_complete(rabbitmq.connect_to_server())
            loop.run_until_complete(rabbitmq.publish(self.__message))
            self.assertTrue(True)
        except Exception:
            self.assertTrue(False)

    def test_publish_without_connection(self):
        rabbitmq = AsyncBroker(self.__broker_address, self.__broker_queue_name)

        try:
            loop = asyncio.get_event_loop()
            loop.run_until_complete(rabbitmq.publish(self.__message))
            self.assertTrue(False)
        except AttributeError:
            self.assertTrue(True)

    def test_close_connection(self):
        rabbitmq = AsyncBroker(self.__broker_address, self.__broker_queue_name)

        try:
            loop = asyncio.get_event_loop()
            loop.run_until_complete(rabbitmq.connect_to_server())
            loop.run_until_complete(rabbitmq.close_connection())
            self.assertTrue(True)
        except Exception:
            self.assertTrue(False)

    def test_close_connection_without_connection(self):
        rabbitmq = AsyncBroker(self.__broker_address, self.__broker_queue_name)

        try:
            loop = asyncio.get_event_loop()
            loop.run_until_complete(rabbitmq.close_connection())
            self.assertTrue(False)
        except AttributeError:
            self.assertTrue(True)
