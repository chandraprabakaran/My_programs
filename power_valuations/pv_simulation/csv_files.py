
import sys
sys.path.append("/Users/chandru/rabbit/PV/pv_simulation")

import csv
from datetime import datetime
import aiofiles
from aiocsv import AsyncWriter
import logging
import decimal


class FileWriter:
    def write(self, timestamp: datetime, meter_power_value: decimal, simulator_power_value: decimal,
              combined_power_value: decimal) -> None:
        pass


class csv_files(FileWriter):
    __destination = ""

    def __init__(self, destination):
        """
        :param destination:
        """
        self.__destination = destination

    async def write(self, timestamp: datetime, meter_power_value: int, simulator_power_value: int,
                    combined_power_value: int) -> None:
        """
        Writes values into a csv file
        (timestamp,meter_power_value,simulator_power_value,combined_power_value)
        """
        async with aiofiles.open(self.__destination, mode='a') as csv_file:
            csv_file_writer = AsyncWriter(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            await csv_file_writer.writerow(['datetime','meter_power','simulator_power','total_power'])
            await csv_file_writer.writerows([datetime.now(), meter_power_value, simulator_power_value,
                                            combined_power_value])
        logging.debug("%s, %s, %s, %s are writen to %s", datetime.now(), meter_power_value, simulator_power_value,
                      combined_power_value, self.__destination)
