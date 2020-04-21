#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''Генерит ключевые слова по формуле. Так же для рестораннов на латинице переписывает буквами кирилицы. И отправляет лист в add_key.py'''

import json_parse
from transliterate import translit, get_available_language_codes
import re

def main(id):
    data_json = json_parse.main() #читает данные с API chocofood,
    all_keywords=[] #хранит все ключевые слова в листе

    c=["меню",  "заказать", "заказ", "сайт", "чокофуд",
        "chocofood", "цены", "отзывы"] #нужно для формулы

    # c=["меню".decode("utf-8"),  "заказать".decode("utf-8"), "заказ".decode("utf-8"), "сайт".decode("utf-8"), "чокофуд".decode("utf-8"),
    # "chocofood".decode("utf-8"), "цены".decode("utf-8"), "отзывы".decode("utf-8")] #нужно для формулы
    a=[] #чтоб хранить название ресторана

    for data in data_json:
        #print(data["id"])
        city=data["city"] #город
        if (data["id"]==id): #айди ресторана, определяет для какого ресторана генерить ключевики

            # #n=re.sub(" '|!|`|№|«|»|’|(|)", "", data["title"])
            # #n = re.sub(r"(^| )[^ ]*[^A-Za-z ][^ ]*(?=$| )", "", data["title"])
            # n  = re.sub(r'[^A-Za-z]', '', data["title"])
            # print("name", data['title'])
            # print("After Removing", n)
            #name1=data["title"].split(" ") #если ресторана название состоит из двух слов и добавлять перед каждым словом +

            whitelist = set('abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ абвгдеёжзийклмнопрстуфхцчшщъыьэюя АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ' )
            kek = ''.join(filter(whitelist.__contains__, data))


            #print("name", data)
            #print("After Removing", kek)
            n= re.sub(' +', ' ', kek)
            print("After removing musor from name", n)
            name1=n.split(" ")

            s=" +"
            for d in name1:
                a.append(d)

            name="+"+s.join(a)
            name2="+"+(translit(s.join(a), 'ru')) # с латиницы на кирилицу

            all_keywords.append(name) #все ключевики складываются в этот лист
            all_keywords.append(name2)


            if city =="Нур-Султан (Астана)":
                city="НурСултан Астана"

            b=[city, "Доставка", "Доставка +%s" % city] #тоже для формулы

            for i in b:
                key2=name+" "+"+"+str(i)
                key22=name2+" "+"+"+str(i)
                all_keywords.append(key2)
                all_keywords.append(key22)

            for k in c:
                key3=name+" "+"+"+k
                key33=name2+" "+"+"+k
                all_keywords.append(key3)
                all_keywords.append(key33)
        #else:
            #print("NOT")
    print(all_keywords)
    return (all_keywords) #возвращает лист всех ключевиков

#if __name__ == '__main__':
#    print(main(16))
