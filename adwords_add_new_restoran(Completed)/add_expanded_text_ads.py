#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Добавляет объвления, смотря на их категорию. Берутся объявления из файлов по категориям"""

import uuid
import csv
import sys

# reload(sys)
# sys.setdefaultencoding('utf8')

import re
#from googleads import adwords

def main(client, ad_group_id, category, name, finalUrls):
    #try:
      if(category=="Суши-бар"): #сравнивает какая категория
          with open("sushi.csv", "rt") as file: #открывать файл именно той категории
              reader = csv.DictReader(file, delimiter=";") #delimeter ; должен быть, так как в файле так и если в объявление точка или запятая в тексте есть, чтоб он их не разделял.
              for line in reader: #достаем данные из файла и передаем функции add_text
                  add_text(client, line["head1"], re.sub("!|`|№|(|)|«|»", "", name), ad_group_id, line["head2"], line["description"], finalUrls, line["path1"], line["path2"],  line["head3"], line["description2"])
                  #line["head1"] это первый заголовок, name название заведения, ad_group_id айди группы объявлений,  line["head2"] второй заголовок, line["description"] описание объвления, finalUrls ссылка на сайте, line["path1"] Отображаемый путь

     #так же в остальных категориях, меняются только категории. Их берем из API chocofood
      elif (category=='Шашлычная'):
          with open("sashlyk.csv", "rt") as file:
              reader = csv.DictReader(file, delimiter=";")
              for line in reader:
                  add_text(client, line["head1"],re.sub("!|`|№|(|)|«|»", "", name), ad_group_id, line["head2"], line["description"], finalUrls, line["path1"], line["path2"],  line["head3"], line["description2"])


      elif (category=='Пиццерия'):
          with open("pizza.csv", "rt") as file:
              reader = csv.DictReader(file, delimiter=";")
              for line in reader:
                  add_text(client, line["head1"], re.sub("!|`|№|(|)|«|»", "", name), ad_group_id, line["head2"], line["description"], finalUrls, line["path1"], line["path2"], line["head3"], line["description2"])

      else:
          with open("common.csv", "rt") as file:
              reader = csv.DictReader(file, delimiter=";")
              for line in reader:
                  add_text(client, line["head1"], re.sub("!|`|№|(|)|«|»", "", name), ad_group_id, line["head2"], line["description"], finalUrls, line["path1"], line["path2"],  line["head3"], line["description2"])

      """elif (category=='Фаст-фуд'):
          with open("fast_food.csv", "rb") as file:
              reader = csv.DictReader(file, delimiter=";")
              for line in reader:
                  add_text(client, line["head1"], name, ad_group_id, line["head2"], line["description"], finalUrls, line["path1"], line["path2"])


      elif (category=='Кондитерская' or category=='Кондитерский дом'):
          with open("sladkoe.csv", "rb") as file:
              reader = csv.DictReader(file, delimiter=";")
              for line in reader:
                  add_text(client, line["head1"], name, ad_group_id, line["head2"], line["description"], finalUrls, line["path1"], line["path2"])

      elif (category=='Ресторан'):
          with open("restaurant.csv", "rb") as file:
              reader = csv.DictReader(file, delimiter=";")
              for line in reader:
                  add_text(client, line["head1"], name, ad_group_id, line["head2"], line["description"], finalUrls, line["path1"], line["path2"])
                  """
    #except:
    #    pass

def add_text(client, head1, name, ad_group_id, head2, description, finalUrls, path1, path2, head3, description2):
    ad_group_ad_service = client.GetService('AdGroupAdService', version='v201809')
    headlinePart1=head1+" "+name
    if (len(headlinePart1)>=30): #проверяет если длина заголовка и название Ресторана больше 30 символов, нельзя чтоб было больше 30
        headlinePart1=name #если больше то первый заголовок остается просто навание Ресторана и в другом случаи заголовок плюс название ресторана

    if (len(name)>=30):
        headlinePart1=name.split(" ")[0]+name.split(" ")[1]

    #запрос на добавление объявления
    operations = [
    {
          'operator': 'ADD',
          'operand': {
              'xsi_type': 'AdGroupAd',
              'adGroupId': ad_group_id,
              'ad': {
                  'xsi_type': 'ExpandedTextAd',
                  'headlinePart1': "{}".format(headlinePart1), #1 заголовок
                  'headlinePart2':"{}".format(head2), #2 заголовок
                  'description': "{}".format(description), #описание
                  'finalUrls': "{}".format(finalUrls), #ссылка
                  'path1': "{}".format(path1), #Отображаемый путь
                  'path2':"{}".format(path2),#Отображаемый путь2
                  'headlinePart3':"{}".format(head3),
                  'description2':"{}".format(description2)
              },
              'status': 'ENABLE' #объявления добавляются включенными
          }}]
    ads = ad_group_ad_service.mutate(operations) #вызываем сервис adwords
    print("ADDED ads")
    #for criterion in ads:
    #     print ('Added ads %s') % (criterion['ad']['headlinePart1'])
