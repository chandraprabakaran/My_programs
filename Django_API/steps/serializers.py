from rest_framework import serializers

from .models import table1,table2
class SalesSerializer(serializers.ModelSerializer):
    class Meta:
        model = table1
        fields = ['car_id_sales','country','merchant_id','selling_date','selling_week','payment_date','sell_price','transported_to_merchant','transport_date']
class CarsSerializer(serializers.ModelSerializer):
    class Meta:
        model = table2
        fields = ['car_id_details','has_tuning','has_airbags','has_alarm_system','Models']