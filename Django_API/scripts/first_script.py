from steps.models import table1,table2
import pandas as pd
import csv
import numpy as np
from django.core.management.base import BaseCommand

df = pd.read_excel(
    '/Users/chandru/Downloads/task_data.xlsx',
    sheet_name='Sales',
    header=0)
# print(df)
df['transport_date'] = df['transport_date'].fillna(method='ffill')
values = {"car_id_sales": 0, "country": 0, "merchant_id": 0, "selling_date": 0000 - 00 - 00, "selling_week": 0000 - 00,
          "payment_date": 0000 - 00 - 00, "sell_price": 0, "transported_to_merchant": 0, "transport_date": "2021-08-03"}
files = df.fillna(value=values)
files.to_csv("sales_files.csv")
cars = pd.read_excel(
    '/Users/chandru/Downloads/task_data.xlsx',
    sheet_name='Cars',
    header=0)
cars.to_csv("cars_file.csv")
def run():
    # All data in run method only will be executed
    with open('sales_files.csv') as file:
        reader = csv.reader(file)
        next(reader)  # Advance past the header

        table1.objects.all().delete()
        table2.objects.all().delete()

        for row in reader:
            # print(row[1])
            car_id_sales = row[1]
            country = row[2]
            merchant_id = row[3]
            selling_date = row[4]
            selling_week = row[5]
            payment_date = row[6]
            sell_price = row[7]
            transported_to_merchant = row[8]
            transport_date =row[9]
            item = table1(car_id_sales = car_id_sales, country=country,merchant_id=merchant_id,selling_date=selling_date,selling_week=selling_week,payment_date=payment_date,sell_price=sell_price,transported_to_merchant=transported_to_merchant, transport_date=transport_date)
            item.save()
    with open('cars_file.csv') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            car_id_details = row[1]
            has_tuning = row[2]
            has_airbags = row[3]
            has_alarm_system = row[4]
            Models = row[5]
            items = table2(car_id_details = car_id_details, has_tuning=has_tuning,has_airbags=has_airbags,has_alarm_system=has_alarm_system,Models=Models)
            items.save()
    print("Data Added")

