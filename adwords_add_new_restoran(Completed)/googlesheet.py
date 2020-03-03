#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Записывает в google sheet название группы, кампании и время, которые залились с помощью скрипта"""

import gspread #использует эту библиотеку для залива
from oauth2client.service_account import ServiceAccountCredentials

import pprint

#data
def main(data): #принимает данные от add_ad_groups.py
    scope = ['https://spreadsheets.google.com/feeds',
             'https://www.googleapis.com/auth/drive']

    creds=ServiceAccountCredentials.from_json_keyfile_name("Add new restaurants-1ecd05a3ba51.json", scope) #данные авторизации
    client = gspread.authorize(creds)

    sheet = client.open("Restaurants").sheet1 #название google sheet
    for row in data:
        sheet.insert_row(row)#заливает строчки
