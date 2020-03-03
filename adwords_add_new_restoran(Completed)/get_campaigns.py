#!/usr/bin/python
from googleads import adwords
import csv


PAGE_SIZE = 100


def main(client):
  name_id = dict()

  campaign_service = client.GetService('CampaignService', version='v201806')

  offset = 0
  selector = {
      'fields': ['Id', 'Name', 'Status'],
      'paging': {
          'startIndex': str(offset),

          'numberResults': str(PAGE_SIZE)
      },
      }


  more_pages = True
  while more_pages:
    page = campaign_service.get(selector)

    # Display results.
    if 'entries' in page:
      for campaign in page['entries']:
        print ('Campaign with id "%s", name "%s", and status "%s" was '
               'found.' % (campaign['id'], campaign['name'].encode("utf-8"),
                           campaign['status'].encode("utf-8")))

        name_id.update( {campaign['name'].encode("utf-8") : campaign['id']} )

    else:
      print 'No campaigns were found.'
    offset += PAGE_SIZE
    selector['paging']['startIndex'] = str(offset)
    more_pages = offset < int(page['totalNumEntries'])
    #print(len(name_id))

    #with open('campaign_name_id.csv','a') as f:
     # w = csv.writer(f)
      #w.writerows(name_id.items())


if __name__ == '__main__':
  adwords_client = adwords.AdWordsClient.LoadFromStorage('googleads.yaml')
  main(adwords_client)
