#!/usr/bin/env python
# -*- coding: utf-8 -*-
import add_expanded_text_ads
import add_ad_groups
import csv
from googleads import adwords
import add_key
import json_parse
import check
import delete
import sys

def add_groups (campaign_name, restaurant_id, name): #добавляет группу объявлений в нужную кампанию
    data_json = json_parse.main()
    adwords_client = adwords.AdWordsClient.LoadFromStorage('googleads.yaml')

    #здесь хранятся название и айди кампании
    with open ('campaign_name_id.csv', 'r') as a:
     reader = csv.reader(a, delimiter='\n')
     for data in reader:
         name_id=data[0].split(',') #лист хранит найзвание и айди
         if (campaign_name==name_id[0]): #проверяет название кампании с названием кампании в файле
             CAMPAIGN_ID = '%s' % name_id[1] #если они равны то достает кампании айди

             print("CAMPAIGN_ID {}, campaign name {}".format(CAMPAIGN_ID, campaign_name))
             checked_id=check.main(restaurant_id) #проверяет залит ли этот ресторан
             if (checked_id==True): #если True значит не залит и нужно добавлять группу объявлений
                 print("Начинаю заливать")
                 add_ad_groups.main(adwords_client, CAMPAIGN_ID, restaurant_id, name, campaign_name) #заливает группу объявлений

def add_text_keywords(): #добавляет объявления и ключевые слова группы
    adwords_client = adwords.AdWordsClient.LoadFromStorage('googleads.yaml')

    data_json=json_parse.main()
    for data in data_json:
        group_name="["+str(data["id"])+"]"+data["title"] #название группы в форме [id]Name_of_restaurant
        category=data["categories"][0]["title"] #категория
        name=data["title"] #название ресторан
        finalUrls=data["menu_url"] #ссылка
        id=data["id"] #айди


        with open ('ad_groups_name_id.csv', 'rt') as a: #смотрит по названию группы и достает его айди из файла
            reader = csv.reader(a, delimiter='\n')
            for data in reader:
                name_id=data[0].split(',')
                if (group_name==name_id[0]): #сравнивет название группы и название из файла
                    AD_GROUP_ID=name_id[1] #если равны достает его айди
                    add_expanded_text_ads.main(adwords_client, AD_GROUP_ID, category, name, finalUrls) #передает все данные на добавления оюъявления
                    add_key.main(adwords_client, AD_GROUP_ID, id) #передает все данные на добавление ключевиков
                    check.add(id)
                    delete.main(id, name, AD_GROUP_ID) #удаляет из файла полностью новые залитые ресторана

#if __name__ == '__main__':
#    print("Removed", rem("Daikon"))
