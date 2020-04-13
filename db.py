import shelve
from constants import DB
from datetime import datetime

def saveLatestFetch(value):
  db = shelve.open(DB)
  db['latestFetch'] = value
  db.close()

def getLastestFetch():
  db = shelve.open(DB)
  value = db['latestFetch']
  db.close()
  return value

def init():
  db = shelve.open(DB)
  if('latestFetch' not in db):
    db['latestFetch'] = datetime.utcnow()
  db.close()
