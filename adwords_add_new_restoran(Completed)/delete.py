#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Удаляет группы объвлений из файла ad_groups_name_id.csv, для того чтобы постоянно не заливать объявления в одну и ту же группу"""

import csv
import sys

def main(id, name, AD_GROUP_ID):
    delete="[{}]{},{}".format(id, name, AD_GROUP_ID) #какую строчку удалить

    fn = 'ad_groups_name_id.csv'
    f = open(fn)
    output = []
    for line in f: #читает все линии в файле
        if not delete in line: #если наша строка не в этих строках
            output.append(line) #добавляет все строки кроме сктроки которую хотим удалить
    f.close()
    f = open(fn, 'w')
    f.writelines(output) #записывает обратно в файл
    f.close()
    print("DELETED")
