from lxml import html
import requests
import sqlite3
c = sqlite3.connect('bling.db')

oldscore={}

for row in c.execute('SELECT * FROM users'):
  print(row)

