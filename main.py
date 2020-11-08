from datetime import datetime, timedelta, timezone
from time import sleep
from airtable import Airtable
import requests
from bs4 import BeautifulSoup
from constants import *
import db

airtable = Airtable(API_BASE, API_TABLE, API_TOKEN)
db.init()

def fetchNew():
  lastFetch = db.getLastestFetch()
  lastModified = f'LAST_MODIFIED_TIME({{{FieldName.NUMBER.value}}})'
  records = airtable.get_all(formula=f"IS_AFTER({lastModified},'{lastFetch}')")

  db.saveLatestFetch(datetime.utcnow() - timedelta(seconds=1))
  return records

def updateRecord(record):
  link = 'boj.kr/' + str(record['fields'][FieldName.NUMBER.value])
  linkWithProtocol = 'http://' + link

  r = requests.get(linkWithProtocol)
  if r.status_code != 200: return

  html = BeautifulSoup(r.text, features="html.parser")
  title = html.find(id='problem_title').text

  fields = {
    FieldName.LINK.value: link,
    FieldName.TITLE.value: title,
  }
  airtable.update(record['id'], fields)

def loop():
  print('Fetching after:', db.getLastestFetch())
  records = fetchNew()
  print(records)
  print()
  for r in records:
    updateRecord(r)

def main():
  while True:
    loop()
    sleep(5)

if __name__ == '__main__':
  main()
