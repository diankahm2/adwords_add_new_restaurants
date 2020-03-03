#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""проверяет по айди ресторана есть ли он в adwords или нет"""

#import json_parse.py
import csv

list=[]

def main(check_id):
    with open ("new_file.csv", "rt") as f: #открывает файл в нем айдишки ресторанов которые уже залиты
        reader=csv.DictReader(f, delimiter=",")
        for row in reader:
            id_from_file=row["id"] #айди из файла
            list.append(id_from_file) #ложит в лист
        id_to_check="[{}]".format(check_id) #айди которое нужно проверить есть ли или нет
        if (id_to_check not in list): #если не в листе, значит отправляет True, означает этот ресторан еще не залит
            return True
        else:
            return False #противном случае, уже залит и отправляет False


def add(check_id):
    f=open("new_file.csv", "a")
    data=[]
    data.append(["[{}]".format(check_id), 1])
    w=csv.writer(f)
    w.writerows(data)
    f.close()

    #with open ("new_file.csv", "a") as f:

#открывает файл в нем айдишки ресторанов которые уже залиты
        # reader=csv.DictReader(f, delimiter=",")
        # for row in reader:
        #     id_from_file=row["id"] #айди из файла
        #     list.append(id_from_file) #ложит в лист
        # id_to_check="[{}]".format(check_id) #айди которое нужно проверить есть ли или нет
        # if (id_to_check not in list): #если не в листе, значит отправляет True, означает этот ресторан еще не залит
        #     return True
        # else:
        #     return False #противном случае, уже залит и отправляет False
