from django.db import models


class table1(models.Model):

    car_id_sales = models.CharField(max_length=200, primary_key=True, unique=True)
    country = models.CharField(max_length=200, null=True, blank=True)
    merchant_id = models.CharField(max_length=200, null=True, blank=False)
    selling_date = models.DateField(null=True, blank=False)
    selling_week = models.CharField(max_length=200, null=True, blank=False)
    payment_date = models.DateField(null=True, blank=False)
    sell_price = models.CharField(max_length=200, null=True, blank=False)
    transported_to_merchant = models.CharField(max_length=200, null=True, blank=False)
    transport_date = models.DateField(null=True, blank=False)

    created_at = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{} car_id'.format(self.car_id_sales)

class table2(models.Model):
    car_id_details = models.CharField(max_length=200, primary_key=True, unique=True)
    has_tuning = models.CharField(max_length=200, null=True, blank=True)
    has_airbags = models.CharField(max_length=200, null=True, blank=True)
    has_alarm_system = models.CharField(max_length=200, null=True, blank=True)
    Models = models.CharField(max_length=200, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{} car_id'.format(self.car_id_details)
