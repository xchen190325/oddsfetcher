import csv
import re
import pandas as pd
import requests
pattern = 'data-id=\"(\d\d\d\d\d\d\d)\" data-status='
with open('game.html','r') as gamefile:
    res = gamefile.read()
game_id = re.findall(pattern,res)
def is_super_league(page):
    # if '欧冠杯' or '英超' or '欧联杯' or '意甲' or '法甲' or '德甲' or '西甲' in page:
    #     return True
    if re.findall('欧冠杯 \d\d\d\d/\d\d/\d\d \d\d:\d\d',page):
        return True
    elif re.findall('欧联杯 \d\d\d\d/\d\d/\d\d \d\d:\d\d',page):
        return True
    elif re.findall('英超 \d\d\d\d/\d\d/\d\d \d\d:\d\d',page):
        return True
    elif re.findall('法甲 \d\d\d\d/\d\d/\d\d \d\d:\d\d',page):
        return True
    elif re.findall('德甲 \d\d\d\d/\d\d/\d\d \d\d:\d\d',page):
        return True
    elif re.findall('意甲 \d\d\d\d/\d\d/\d\d \d\d:\d\d',page):
        return True
    elif re.findall('西甲 \d\d\d\d/\d\d/\d\d \d\d:\d\d',page):
        return True
    elif re.findall('葡超 \d\d\d\d/\d\d/\d\d \d\d:\d\d',page):
        return True
for id in game_id:
    output = requests.get(f'https://live.leisu.com/oupei-{id}')
    if is_super_league(output.content.decode()):
        print(id)