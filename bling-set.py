from lxml import html
import requests
import sqlite3
c = sqlite3.connect('bling.db')

oldscore={}
oldscore['0x136508b87aa0453E199f03b3cfbcA8ff32084fD1']=6550709
oldscore['0x9D284b452f252f0B6FcbEBe5cD3DbAbD1d4c684C']=9100178

for addr in oldscore.keys():
  print(addr)
  print(oldscore[addr])
  c.execute('UPDATE users set oldscore=? where addr=?', (oldscore[addr],addr))

c.commit()

