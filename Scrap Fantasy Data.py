import json
import re
import urllib.request
import numpy as np
from bs4 import BeautifulSoup

f = open('nbapro.txt','w')
errorFile = open('nbaerror.txt','w')

soup = BeautifulSoup(urllib.request.urlopen('http://www.numberfire.com/nba/fantasy/full-fantasy-basketball-projections'))

script = soup.find('script', text=lambda x: x and 'NF_DATA' in x).text
data = re.search(r'NF_DATA = (.*?);', script).group(1)
data = json.loads(data)

for player_id, player in data['players'].items():
    print(player['name'] + ',' + player['id'])
##
##for player_id, player in data['players'].items():
##    print(player['id'])
##    print(player['name'] + ' ' + player['position'])
   
   
for proj in data['daily_projections']:
    print(str(proj['fanduel_fp']) + ',' + str(proj['nba_player_id']))
    
for rank_id, team_analytics in data['team_analytics'].item():
    print(rank['ovr_rank'])
          
f.close
errorFile.close
