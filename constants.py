import os
from enum import Enum

API_BASE = os.environ['API_BASE']
API_TABLE = os.environ['API_TABLE']
API_TOKEN = os.environ['API_TOKEN']

DB = 'airboj.db'

class FieldName(Enum):
  NUMBER = '번호'
  TITLE = '제목'
  LINK = '링크'
  SOLVED = '푼 날짜'
