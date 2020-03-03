#!/usr/bin/env python
# -*- coding: utf-8 -*-

""""Главный файл который нужно запускать. По городу определяет кампанию в которую надо добавить группу"""
import sys
sys.path.insert(0, '/home/user/Desktop/adwords_editing/adwords_add_new_restoran(Completed)/main.py')

import json_parse
import main
import check

#от API chocofood достает город сравнивает
data_json=json_parse.main()
for data in data_json:
    id=data["id"]
    city=data["city"]
    name=data["title"]
    print("Айдишка", id)
    print("Gorod", city)

    #checked_id=check.main(id) #проверяет залит ли этот ресторан
    #if (checked_id==True): #если True значит не залит и нужно добавлять группу объявлений
        #add_ad_groups.main(adwords_client, CAMPAIGN_ID, restaurant_id, name, campaign_name) #заливает группу объявлений

     #   print("Заливка начинается", id)

    if(city=="Алматы"): #если это Алматы то передает что название кампании "Рестораны Алматы"
        campaign_name="Рестораны Алматы"
        main.add_groups(campaign_name, id, name) #вызывает на добавление группы и передает данные
        main.add_text_keywords() #вызывает на добавление объявления, ключей и передает данные
        print(name, city)

    #так же со всеми остальными кампаниями

    if(city=="Астана"):
       campaign_name="Рестораны Астана"
       main.add_groups(campaign_name, id, name)
       main.add_text_keywords()

    if(city=="Шымкент"):
       campaign_name="Рестораны Шымкент"
       main.add_groups(campaign_name, id, name)
       main.add_text_keywords()

    if(city=="Караганда"):
       campaign_name="Рестораны Караганда"
       main.add_groups(campaign_name, id, name)
       main.add_text_keywords()

    elif (city=="Актау"):
       campaign_name="Рестораны Актау"
       main.add_groups(campaign_name, id, name)
       main.add_text_keywords()

    elif(city=="Актобе"):
       campaign_name="Рестораны Актобе"
       main.add_groups(campaign_name, id, name)
       main.add_text_keywords()

    elif(city=="Атырау"):
       campaign_name="Рестораны Атырау"
       main.add_groups(campaign_name, id, name)
       main.add_text_keywords()

    elif(city=="Капчагай"):
       campaign_name="Рестораны Капчагай"
       main.add_groups(campaign_name, id, name)
       main.add_text_keywords()

    elif(city=="Каскелен"):
       campaign_name="Рестораны Каскелен"
       main.add_groups(campaign_name, id, name)
       main.add_text_keywords()

    elif(city=="Павлодар"):
       campaign_name="Рестораны Павлодар"
       main.add_groups(campaign_name, id, name)
       main.add_text_keywords()

    elif(city=="Семей"):
       campaign_name="Рестораны Семей"
       main.add_groups(campaign_name, id, name)
       main.add_text_keywords()

    if(city=="Талдыкорган"):
       campaign_name="Рестораны Талдыкорган"
       main.add_groups(campaign_name, id, name)
       main.add_text_keywords()

    elif(city=="Тараз"):
       campaign_name="Рестораны Тараз"
       main.add_groups(campaign_name, id, name)
       main.add_text_keywords()

    elif(city=="Темиртау"):
       campaign_name="Рестораны Темиртау"
       main.add_groups(campaign_name, id, name)
       main.add_text_keywords()

    elif(city=="Усть-Каменогорск"):
       campaign_name="Рестораны Усть-Каменогорск"
       main.add_groups(campaign_name, id, name)
       main.add_text_keywords()

    elif(city=="Экибастуз"):
       campaign_name="Рестораны Экибастуз"
       main.add_groups(campaign_name, id, name)
       main.add_text_keywords()
    # else:
    #     print("Такой уже есть", id)
