#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Здесь добавляют новые группы, принимает айди кампании в которую добавить группы
    сохраняет айди и название группы в файл и отправляет данные в google sheet"""

import uuid
import csv


import sys
# from importlib import reload
#
# reload(sys)
# sys.setdefaultencoding('utf8')

import json_parse
import check
import googlesheet
import datetime


def main(client, campaign_id, id, name, campaign_name):
    now = datetime.datetime.now()
    date=now.strftime("%Y-%m-%d %H:%M") #берет время для google sheet, чтоб знать когда залилась группа

    ad_groups_name_id = dict()
    for_google_sheet=[]
    ids=[]

    ad_group_service = client.GetService('AdGroupService', version='v201809')
    if (check.main(id)==True): #проверяет есть ли эта группа в adwords по айди
        operations = [{
                  'operator': 'ADD',
                  'operand': {
                      'campaignId': campaign_id, #айди кампании в которую заливать
                      'name': '[{}]{}'.format(id, name), #это название группы
                      'status': 'PAUSED',
                      'biddingStrategyConfiguration': {
                          'bids': [
                              {
                                  'xsi_type': 'CpaBid', #целевая цена за конверсию
                                  'bid': {
                                      'microAmount': 2500000 #2.5 dollars ставка
                                  },
                              }
                          ]
                      },
                      'settings': [
                          {
                              'xsi_type': 'TargetingSetting',
                              'details': [
                                  {
                                      'xsi_type': 'TargetingSettingDetail',
                                      'criterionTypeGroup': 'PLACEMENT',
                                      'targetAll': 'false',
                                  },
                                  {
                                      'xsi_type': 'TargetingSettingDetail',
                                      'criterionTypeGroup': 'VERTICAL',
                                      'targetAll': 'true',
                                  },
                              ]
                          }
                      ]
                  }
              }]



        try:
                ad_groups = ad_group_service.mutate(operations)

                for ad_group in ad_groups['value']:
                    print ('Ad group with name "%s" and id "%s" was added.' % (ad_group['name'], ad_group['id']))
                    ad_groups_name_id.update({ ad_group['name'] : ad_group['id'] }) #сохраняет айди и название группы в лист
                    for_google_sheet.append([ad_group['name'], date, campaign_name]) #сохраняет айди, название группы, время, название кампании в лист
                    ids.append(["[{}]".format(ad_group['id']), 0])

        except Exception as exception:
            #print("hello i am exceprion", exception)
            if exception == "[AdGroupServiceError.DUPLICATE_ADGROUP_NAME @ operations[0].operand.name; trigger:'[{}]{}']".format(id, name):
                print("I am error just pass")
                check.add(id)
                pass
            #assert type(exception).__name__ == 'NameError'
            #assert exception.__class__.__name__ == 'NameError'




    googlesheet.main(for_google_sheet) #отправляет данные в google sheet
    with open('ad_groups_name_id.csv','a') as f: #сохраняет в файл данные
        r=csv.reader(f, delimiter="\n")
        w = csv.writer(f)
        w.writerows(ad_groups_name_id.items())
