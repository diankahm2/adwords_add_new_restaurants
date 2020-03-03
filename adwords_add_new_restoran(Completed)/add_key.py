#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Добавляет ключевые слова к группе объявлений. Принимает айди группы в которую добавлять и айди ресторана,
 чтоб добавить именно этого ресторана ключевики"""

from googleads import adwords
import generate_key
import time
def main(client, ad_group_id, restoran_id):

  all_keywords=generate_key.main(restoran_id) #сохраняет в лист все ключевые слова этого ресторана

  ad_group_criterion_service = client.GetService('AdGroupCriterionService', version='v201809')
  for key in all_keywords: #пробегается по листу и добавляет
      #try:
      keyword1   = {
          'xsi_type': 'BiddableAdGroupCriterion',
          'adGroupId': ad_group_id,
          'criterion': {
              'xsi_type': 'Keyword',
              'matchType': 'BROAD',
              'text': key
          },
      }
      operations = [
          {
              'operator': 'ADD',
              'operand': keyword1
          }
      ]
      ad_group_criteria = ad_group_criterion_service.mutate(operations)['value']
      print("added keys")

      #for criterion in ad_group_criteria:
       #   print(criterion)
          #print ('Keyword ad group criterion with ad group id "%s", criterion id ') % (criterion['criterion']['text'])

      # except:
      #     print("Wait until Exception will Proccess")
      #     time.sleep(35)
      #     continue
