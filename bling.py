from lxml import html
import requests
import sqlite3
c = sqlite3.connect('bling.db')

#c.execute('''CREATE TABLE users
#             (addr text, oldscore integer)''')

# Insert a row of data
#c.execute("INSERT INTO users VALUES ('0x136508b87aa0453E199f03b3cfbcA8ff32084fD1',6417395)")
#c.execute("INSERT INTO users VALUES ('0x9D284b452f252f0B6FcbEBe5cD3DbAbD1d4c684C',8288918)")

# Save (commit) the changes
c.commit()

data = requests.get("https://nweb.io/leaderboard")
tree = html.fromstring(data.content)
players = tree.xpath('//tr')

oldscore={}

for row in c.execute('SELECT * FROM users'):
  print(row)
  oldscore[row[0]]=row[1]

#oldscore['0x136508b87aa0453E199f03b3cfbcA8ff32084fD1']=6417395
#oldscore['0x9D284b452f252f0B6FcbEBe5cD3DbAbD1d4c684C']=8288918

#oldscore['0x136508b87aa0453E199f03b3cfbcA8ff32084fD1']=5985315
#oldscore['0x9D284b452f252f0B6FcbEBe5cD3DbAbD1d4c684C']=7423337
print("oldscore:")
print(oldscore)
newscore={}
newgainz={}

for player in players:
  addr = player[0].text
  if player[1].text=='Points':
    continue
  score = int(player[1].text)

  if addr in oldscore:
    newscore[addr]=score
    gainz = score - oldscore[addr]
    newgainz[addr]=gainz
    print('congratz '+addr+' '+str(gainz)+' points gained this week')

print('newscore:')
print(newscore)

print('newgainz:')
print(newgainz)

totalgainz = 0.0
for player in newgainz:
  totalgainz += newgainz[player]

print('totalgainz:')
print(totalgainz)

for player in newgainz:
  print("send "+str(newgainz[player]/totalgainz*10000)+' to '+player)

for addr in newscore.keys():
  print(addr)
  print(newscore[addr])
#  c.execute('UPDATE users set oldscore=? where addr=?', (newscore[addr],addr))
print("DIDN'T UPDATE THE DB")

c.commit()

