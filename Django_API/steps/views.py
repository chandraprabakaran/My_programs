from django.http import JsonResponse
from .models import table1,table2
from .serializers import SalesSerializer,CarsSerializer
from rest_framework.decorators import api_view
from rest_framework import status,generics
from rest_framework.response import Response
from django.shortcuts import render
from django.db import connection
from django.db.models import Q
from rest_framework.permissions import IsAuthenticated
@api_view(['GET','POST'])

def sales_list(request,format =None):
    permission_classes  =(IsAuthenticated, )
    if request.method =='GET':
        sales = table1.objects.all()
        serializer = SalesSerializer(sales,many=True)
        return Response(serializer.data)

    if request.method =='POST':
        serializer =SalesSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status = status.HTTP_201_CREATED)
@api_view(['GET','PUT','DELETE'])
def sales_detail(request,car_id_sales,format =None):

    try:
        sales = table1.objects.get(pk = car_id_sales)
    except table1.DoesnotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)

    if request.method =='GET':
        serializer = SalesSerializer(sales)
        return Response(serializer.data)
    elif request.method =='PUT':
        serializer = SalesSerializer(sales, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status = status.HTTP_450_BAD_REQUEST)
    elif request.method=="DELETE":
        sales.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)

@api_view(['GET','POST'])
def cars_list(request):
    if request.method =='GET':
        cars = table2.objects.all()
        serializer = CarsSerializer(cars, many=True)
        return Response(serializer.data)

    if request.method =='POST':
        serializer =CarsSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status = status.HTTP_201_CREATED)
@api_view(['GET','PUT','DELETE'])
def sales_detail(request,car_id_details,format =None):
    try:
        cars = table2.objects.get(pk = car_id_details)
    except table1.DoesnotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)

    if request.method =='GET':
        serializer = SalesSerializer(cars)
        return Response(serializer.data)
    elif request.method =='PUT':
        serializer = SalesSerializer(cars, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status = status.HTTP_450_BAD_REQUEST)
    elif request.method=="DELETE":
        cars.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)

def webpage(request):
    cars = table2.objects.all()
    print(cars.query)
    print(connection.queries)
    return render(request,'average.html',{'posts':cars})
def average(request):
    cursor =connection.cursor()
    cursor.execute("SELECT country,avg(sell_price) AS sales FROM steps_table1 GROUP BY country")
    output = cursor.fetchall()
    return render(request, 'output.html', {'posts': output})

def airbags(request):
    cursor = connection.cursor()
    cursor.execute("SELECT car_id_sales,COUNT(car_id_sales),country FROM steps_table1 INNER JOIN steps_table2 ON steps_table1.car_id_sales=steps_table2.car_id_details WHERE steps_table2.has_airbags=0 GROUP BY country")
    output = cursor.fetchall()
    return render(request, 'count.html', {'posts': output})
def timediff(request):
    cursor = connection.cursor()
    cursor.execute("SELECT car_id_sales,country,selling_date,payment_date,JULIANDAY(payment_date)-JULIANDAY(selling_date) AS difference FROM steps_table1")
    output = cursor.fetchall()
    return render(request, 'time_difference.html', {'posts': output})
def sales(request):
    cursor = connection.cursor()
    cursor.execute(
        "SELECT car_id_sales,country,merchant_id,selling_date,selling_week,	payment_date,sell_price,transported_to_merchant,transport_date,has_tuning,has_airbags,has_alarm_system,Models FROM steps_table1 INNER JOIN steps_table2 ON steps_table1.car_id_sales=steps_table2.car_id_details GROUP BY steps_table1.country")
    output = cursor.fetchall()
    return render(request, 'total_sales.html', {'posts': output})