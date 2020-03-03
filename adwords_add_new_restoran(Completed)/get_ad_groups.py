from googleads import adwords
import csv

PAGE_SIZE = 1000


def main(client, campaign_id):
  name_id = dict()
  ads_groups_ids = {}
  ad_group_service = client.GetService('AdGroupService', version='v201809')

  offset = 0
  selector = {
      'fields': ['Id', 'Name', 'Status'],
      'predicates': [
          {
              'field': 'CampaignId',
              'operator': 'EQUALS',
              'values': [campaign_id]
          }
      ],
      'paging': {
          'startIndex': str(offset),
          'numberResults': str(PAGE_SIZE)
      }
  }

  more_pages = True
  while more_pages:
    page = ad_group_service.get(selector)

    # Display results.
    if 'entries' in page:
      for ad_group in page['entries']:
          ads_groups_ids[unicode(ad_group['name'])] = str(ad_group['id'])
          print ("%s %s" % (ad_group["name"], ad_group["id"]))

          name_id.update( {ad_group['name'].encode("utf-8") : ad_group['id']} )

    else:
      print 'No ad groups were found.'
    offset += PAGE_SIZE
    selector['paging']['startIndex'] = str(offset)
    more_pages = offset < int(page['totalNumEntries'])
    #return ads_groups_ids
    #print(name_id)

    with open('ad_groups_name_id.csv','a') as f:
      w = csv.writer(f)
      w.writerows(name_id.items())


if __name__ == '__main__':
  adwords_client = adwords.AdWordsClient.LoadFromStorage("googleads.yaml")
  #main (adwords_client, 369828890)
  with open("campaign_name_id.csv", "rb") as file:
      reader = csv.DictReader(file, delimiter=",")
      for campaign in reader:
          print (campaign["id"])
          main(adwords_client, campaign["id"])
