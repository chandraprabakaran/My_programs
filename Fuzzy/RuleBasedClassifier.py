
import pymongo
from pymongo import MongoClient


import pyodbc
import time
import sqlite3

import pandas as pd


def get_rules():
    client = MongoClient("localhost",27017)
    client.list_database_names()

    db = client.heart
    print(db.list_collection_names())
    db.data_analysis.count_documents({})
    print(db.data_analysis.count_documents({}))
    cursor = db.data_analysis

    start_time = time.time()
    query = db.data_analysis.find({"CONSEQUENT":"BMI_LOW",
    "CONSEQUENT":"BMI_HIGH",'_id': False})
    # cursor.execute(query)
    columns = [column[0] for column in query]
    temp = db.data_analysis.find()

    # for i in range(0, len(temp)):
    #     temp[i] = tuple(temp[i])
    apriori_rules = pd.DataFrame(temp, columns=columns)
    print(tem for ded in temp)
    print("Apriori get rules: --- %s seconds ---" % (time.time() - start_time))

    start_time = time.time()
    # cursor = db.data_analysis.insertMany(FP_Rules,{
    # "CONSEQUENT":"BMI",
    # "CONSEQUENT":"Glucose"
    # })
    query = db.data_analysis.find({},{"CONSEQUENT":"BMI_LOW",
    "CONSEQUENT":"BMI_HIGH",'_id': False})
    # columns = [column[1] for column in query]
    temp =  db.data_analysis.find()
    #
    # for i in range(0, len(temp)):
    #     temp[i] = tuple(temp[i])
    fp_rules = pd.DataFrame(temp, columns=columns)
    print("FP get rules: --- %s seconds ---" % (time.time() - start_time))

    return apriori_rules, fp_rules


# Rule-base Classifier
def find_match(test_data, rules):
    answers = []
    listdata = test_data[test_data.columns[:-1]].values.tolist()
    temp = 0
    ans = False
    for data in listdata:
        for ant, con, n in zip(rules['Antecedent'], rules['Consequent'], rules['Num_Antecedent']):
            if (n > 1):
                antecedents = ant.split(',')
            else:
                antecedents = ant

            ans = set(antecedents) < set(list(data))

            if (ans == True):

                answers.append(con)
                if (con == ('BMI_HIGH')):
                    temp += 1
                break
        if (ans == False):
            answers.append('BMI_LOW')
    print(temp)
    return answers

def check_accuracy(test_data_diabetes, rule_based_answers):
    total = len(test_data_diabetes)  # might need checking

    tp = 0
    fp = 0
    tn = 0
    fn = 0
    testRows = 0
    for x, y in zip(test_data_diabetes, rule_based_answers):
        print(str(x) + " " + str(y))
        # print("TestRows = " + str(testRows))
        if (str(x) == ('BMI_HIGH') and str(y) == ('BMI_HIGH')):
            tp += 1
            # print("True Positive: " + str(tp))
        elif (str(x) == ('BMI_LOW')and str(y) == ('BMI_HIGH')):
            fp += 1
            # print("False Positive: " + str(fp))
        elif (str(x) == ('BMI_LOW') and str(y) == ('BMI_LOW')):
            tn += 1
            # print("True Negative: " + str(tn))
        elif (str(x) == ('BMI_HIGH') and str(y) == ('BMI_LOW')):
            fn += 1

        testRows += 1

    if (tp == 0):
        PPV = 0
    else:
        PPV = float(tp / (tp + fp))
    print("PPV:" + str(PPV * 100))
    print("NPV:" + str(float(tn / (tn + fn) * 100)))
    print("Sensitivity:" + str(float(tp / (tp + fn) * 100)))
    print("Specificity:" + str(float(tn / (tn + fp) * 100)))
    if (PPV == 0):
        print("F: 0")
    else:
        print("F1:" + str(float((2 * tp) / (2 * tp + fp + fn) * 100)))
    print(str(float((tp + tn) / (total) * 100)))
    print("TP:" + str(tp) + " FP: " + str(fp) + " TN: " + str(tn) + " FN: " + str(fn))


def classfiy(test_data):
    client = MongoClient("localhost",27017)
    client.list_database_names()

    db = client.heart
    db.data_analysis.count_documents({})
    cursor = db.data_analysis

    apriori_rules, fp_rules = get_rules()

    start_time = time.time()
    prediction_apriori = find_match(test_data, apriori_rules)
    print(prediction_apriori)
    print("Apriori classify: --- %s seconds ---" % (time.time() - start_time))

    start_time = time.time()
    prediction_fp = find_match(test_data, fp_rules)
    print("FP classify: --- %s seconds ---" % (time.time() - start_time))

    print('---------------------------------------------------')
    print('Apriori')
    check_accuracy(test_data['BMI'], prediction_apriori)

    print('---------------------------------------------------')
    print('Fp Growth')
    check_accuracy(test_data['BMI'], prediction_fp)
