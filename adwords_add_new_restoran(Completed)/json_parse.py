#!/usr/bin/python
# -*- coding: utf-8 -*-

#Парсер чтоб доставать данные с апи

import json
import requests

url = 'https://chocofood.kz/debug-api/marketing-restaurants-status/?format=json'

def main():
  response = requests.get(url)
  feed = response.text
  json_feed = json.loads(feed)
  return json_feed


#json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
