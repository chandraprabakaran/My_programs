"""
Copyright (c) 2018 Reynaldo John Tristan Mahinay Jr., Franz Stewart Dizon, Stephen Kyle Farinas and Harry Pardo
"""
import pymongo
from pymongo import MongoClient


import csv
import pyodbc
import time

import pandas as pd

import Apriori1
import FPGrowth
import Fuzzification
import RuleBasedClassifier
import sqlite3

def connect_db(method):
    # DB Connect
    client = MongoClient("localhost",27017)
    client.list_database_names()

    db = client.heart
    print(db.list_collection_names())
    db.data_analysis.count_documents({})
    print(db.data_analysis.count_documents({}))
    cursor = db.data_analysis
    if (method == 'train'):
        query = db.data_analysis.find({"Method":"Train"})
    else:
        query = db.data_analysis.find({"Method":"Test"})

    cursor.execute(query)
    columns = [column[0] for column in cursor.description]
    temp = cursor.fetchall()
    for i in range(0, len(temp)):
        temp[i] = tuple(temp[i])
    ppsd_data = pd.DataFrame(temp, columns=columns)

    return ppsd_data



def table_csv(data):
    # print(data)
    with open('fuzzified.csv', 'w+', newline="") as file:
        writer = csv.writer(file)
        writer.writerows(data)

    file.close()


# IPR OF HARRY PARDO
def insert_fprulesCSV(rules, confi):
    antecedents = []
    consequents = []
    confidence = []
    for rule in rules:
        temp = []
        for x in rule:
            temp.append(x)

        antecedents.append(",".join(temp))
    for con in confi:
        temp = []
        for y in con[:-1]:
            for z in y:
                temp.append(z)
        consequents.append(",".join(temp))

        confidence.append(con[-1])
    with open('FPRules.csv', 'w+') as file:
        # for line in rules:
        # file.write("%s" % line)
        # file.write('\n')
        writer = csv.writer(file, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
        writer.writerow(['Antecedent', 'Consequent', 'Confidence'])
        for x, y, z in zip(antecedents, consequents, confidence):
            writer.writerow(x, y, z)


def insert_fprules(rules, confi):
    client = MongoClient("localhost",27017)
    client.list_database_names()

    db = client.heart
    print(db.list_collection_names())
    db.data_analysis.count_documents({})
    print(db.data_analysis.count_documents({}))
    cursor = db.data_analysis
    db.data_analysis.insertMany(
    FP_Rules,
   {
      "antecedents": " ",
      "consequents":" ",
      "confidence":" "
   })
    antecedents = []
    consequents = []
    confidence = []
    for rule in rules:
        temp = []
        for x in rule:
            temp.append(x)

        antecedents.append(",".join(temp))
    for con in confi:
        temp = []
        for y in con[:-1]:
            for z in y:
                temp.append(z)
        consequents.append(",".join(temp))

        confidence.append(con[-1])
    query = cursor.insert_many({"antecedents": " ","consequents":" ","confidence":" "})

    for x, y, z in zip(antecedents, consequents, confidence):
        temp = x.split(',')
        count = len(temp)
        params = (x, y, z, count)
        # print(params)
        cursor.execute(query, params)

    cnxn.commit()


def insert_arules(antecedent, consequent, confidence, lift):
    client = MongoClient("localhost",27017)
    client.list_database_names()

    db = client.heart
    print(db.list_collection_names())
    db.data_analysis.count_documents({})
    print(db.data_analysis.count_documents({}))
    cursor = db.data_analysis
    query = db.data_analysis.insertMany(
     Apriori_Rules2,
   {
      "Antecedent": " ",
      "Consequent":" ",
      "Confidence":" ",
      "Num_Antecedent":" ",
      "lift":" "
   })
    for x, y, z, l in zip(antecedent, consequent, confidence, lift):
        count = len(x)
        sx = ','.join(x)
        sy = ','.join(y)

        params = (sx, sy, z, count, l)

        cursor.execute(query, params)
    cnxn.commit()


def insert_arulesCSV(antecedent, consequent, confidence):
    with open('Apriori_Rules.csv', 'w+') as file:
        writer = csv.writer(file, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
        writer.writerow(['Antecedent', 'Consequent', 'Confidence'])
        for x, y, z in zip(antecedent, consequent, confidence):
            sx = ','.join(x)
            sy = ','.join(y)
            writer.writerow(sx, sy, z)


def insert_db(fuzzified_data, ppsd_data):
    client = MongoClient("localhost",27017)
    client.list_database_names()

    db = client.heart
    print(db.list_collection_names())
    db.data_analysis.count_documents({})
    print(db.data_analysis.count_documents({}))
    cursor = db.data_analysis
    query = db.data_analysis.insertMany(
      FFSD_TrainingData2,
   {"Pregnancies":" ",
   "Glucose":" ",
   "BloodPressure":" ",
   "SkinThickness":" ",
   "Insulin":" ",
   "BMI":" ",
   "DiabetesPedigreeFunction":" ",
   "Age": " ",
   "Outcome":" ",
   "Method":" "})

    fuzz = []

    for x in fuzzified_data:
        temp = []

        for y in fuzzified_data[x]:
            temp.append(y)
        fuzz.append(temp)

    count = len(fuzz[0])

    table = []
    for i in range(0, count):
        row = []
        for x in fuzz:
            row.append(x[i])

        params = tuple(row)
        cursor.execute(query, params)
        table.append(row)
    # cnxn.commit()
    table_csv(table)


def fixforcsv(fuzzified_data, ppsd_data):
    query = db.data_analysis.insertMany(FFSD_TestData2,
    {"Pregnancies":" ",
    "Glucose":" ",
    "BloodPressure":" ",
    "SkinThickness":" ",
    "Insulin":" ",
    "BMI":" ",
    "DiabetesPedigreeFunction":" ",
    "Age": " ",
    "Outcome":" ",
    "Method":" "})

    dataframe = pd.DataFrame(
        columns=["Pregnancies",
        "Glucose",
        "BloodPressure",
        "SkinThickness",
        "Insulin",
        "BMI",
        "DiabetesPedigreeFunction",
        "Age",
        "Outcome",
        "Method"])


    dataframe['Pregnancies'] = fuzzified_data[0]
    dataframe['Glucose'] = fuzzified_data[1]
    dataframe['BloodPressure'] = fuzzified_data[2]
    dataframe['SkinThickness'] = fuzzified_data[3]
    dataframe['Insulin'] = fuzzified_data[4]
    dataframe['BMI'] = fuzzified_data[5]
    dataframe['DiabetesPedigreeFunction'] = fuzzified_data[6]
    dataframe['Age'] = fuzzified_data[7]
    dataframe['Outcome'] = fuzzified_data[8]
    dataframe['Method'] = fuzzified_data[9]


    list1 = dataframe.values.tolist()
    for x in list1:
        params = tuple(x)
        cursor.execute(query, params)
    cnxn.commit()

    return dataframe


def conn():
    client = MongoClient("localhost",27017)
    client.list_database_names()

    db = client.heart
    print(db.list_collection_names())
    db.data_analysis.count_documents({})
    print(db.data_analysis.count_documents({}))
    curs  = db.data_analysis
    query = db.data_analysis.find({},
    {"Pregnancies":" ",'_id':False
    })

    # cursor.execute(query)
    columns = [column[0] for column in query]
    temp = query
    # for i in range(0, len(temp)):
    #     temp[i] = tuple(temp[i])
    ppsd_data = pd.DataFrame(temp, columns=columns)

    return ppsd_data


def main():
    # Connect to database
    ppsd_data = connect_db('train')

    fuzzified_data = Fuzzification.fuzzify(ppsd_data)
    # print(fuzzified_data)

    # Insert Fuzzified Data
    insert_db(fuzzified_data, ppsd_data)

    # Apriori Algorithm
    fuzzy_csv = pd.read_csv('fuzzified.csv')

    # FP Grwoth
    start_time = time.time()

    rules, confi = FPGrowth.mine('fuzzified.csv')
    print("FP: --- %s seconds ---" % (time.time() - start_time))

    insert_fprules(rules, confi)
    # insert_fprulesCSV(rules,confi)
    start_time = time.time()
    ant, con, conf, lift = Apriori.mine('fuzzified.csv')
    print("Apriori: --- %s seconds ---" % (time.time() - start_time))
    insert_arules(ant, con, conf, lift)
    # insert_arulesCSV(ant,con,conf)


def Nmain():
    fuzzified_data = conn()
    print(fuzzified_data)

    RuleBasedClassifier.classfiy(fuzzified_data)


Nmain()
