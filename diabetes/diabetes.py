import math
import sympy
import csv
from pandas import DataFrame
import pandas as pd
def reading_file(file):
    return open(file).read()

def isnum(number):
    if number % 1 ==0:
        return True
    return False

def isPrime(n):
    return sympy.isprime(n)

def calce(t):
    for e in range(2,t):
        if math.gcd(e,t)==1:
            return e
    return None

def calcd(t,e):
    d = 0
    L = 0
    while True:
        d = (t * L +1)/int(e)
        if isnum(d):
            break
        L += 1
    return int(d)

def encrypt(public_key,message):
    k,e,n = public_key
    c = pow(message,e,n)
    return c

def encrypt_string(public_key, input_string):
    list_ascii_p = format_message(input_string)
    print("list_ascii_numbers(BEFORE ENCRYPTION) : ", list_ascii_p)
    list_cipher_ascii = []
    for i in list_ascii_p:
        list_cipher_ascii.append(encrypt(public_key, i))
    print("list_ascii_numbers(AFTER ENCRYPTION) : ", list_cipher_ascii)
    return list_cipher_ascii

def decrypt(private_key,cipher_text):
    k,d,n = private_key
    m = pow(cipher_text,d,n)
    return m

def decrypt_string(private_key, list_cipher_ascii):
    list_decrypted_ascii = []
    for i in list_cipher_ascii:
        list_decrypted_ascii.append(decrypt(private_key, i))
    return list_decrypted_ascii


def format_message(input_string):
    list_ascii = []
    for i in range(len(input_string)):
        list_ascii.append(ord(input_string[i]))
    return list_ascii

def convert_ascii_to_char(list_items):
    char_list = ""
    for i in range(len(list_items)):
        char_list += (chr(list_items[i]))
    return char_list

def jkrsa(p, q, plain_text=""):
    n = p*q
    k = 2

    J = (p^k -1)*(q^k -1)

    e = calce(J)
    print(type(e))
    d = calcd(J,e)
    publicKey = (k,e,n)
    privateKey = (k,d,n)
    if plain_text == "":
        plain_message = reading_file('diabetes.csv')
    else:
        plain_message = plain_text

    print("Encrypting (", plain_message, ") ...")
    cipher_message = encrypt_string(publicKey, plain_message)
    print("Decrypting (", cipher_message, ") ...")
    p = decrypt_string(privateKey, cipher_message)

    print("plain_message(ASCII) : ", p)
    data = convert_ascii_to_char(p)
    datas = pd.DataFrame(list(data),columns = ['Datas'])
    datas.to_csv("decrypted1.csv",index=False)
    data = pd.read_csv("decrypted1.csv")
    # print(data)
    data = data.rename(columns={'Datas': 'value'})
    data['new'] = data['value'].str.cat(sep='')
    # print(data)
    ds = data['new'].str.split(',', expand=True)
    ds = data['new'].str.split('\n', expand=True)
    import numpy as np
    two_split = np.array_split(((ds.iloc[0]).values), 769)
    df = pd.DataFrame(two_split)
    df.to_csv("sample1.csv",index=False)
    datas = pd.read_csv("sample1.csv")
    datas.columns = ["data"]
    split_data = datas["data"].str.split(",")
    new = split_data.to_list()
    new_df = pd.DataFrame(new)
    # print(new_df)
    new_df.to_csv("diabetes1.csv",header=False,index=False)
    print("plain_message(CHAR) : ",convert_ascii_to_char(p))
    return cipher_message, p

def main():
    p = int(input("Enter p : "))
    if not isPrime(p):
        raise ValueError("P is not prime")

    q = int(input("Enter q : "))
    if not isPrime(q):
        raise ValueError("q is not prime")

    flag = input("Enter:-\n\t- 'f' to read from file => diabetes.csv.\n\t- 'm' to enter plaintext message.\n")
    if flag == 'f':
        return jkrsa(p,q)
    elif flag == 'm':
        m = input("Enter plaintext message:")
        return jkrsa(p,q, m)
    else:
        print("Error !")
        return None

if __name__ == '__main__':
    Cypher, Plain = main()
# the Jordan Totient function Jk(N) which is defined for positive integers K and N to be the number of ordered sets of K non-negative integers less than N such that greatest common divisor of each set is prime to N and
# (1.3) 𝑑 𝑁𝐽𝑘 (𝑁 𝑑) = 𝑁𝑘
