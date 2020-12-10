import csv
import re
import pandas as pd
import requests
pattern = '<li class=\"list-item list-item-(\d\d\d\d\d\d\d) list-day-12-14 notStart\"'
with open('game3.html','r') as gamefile:
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
    elif re.findall('法乙 \d\d\d\d/\d\d/\d\d \d\d:\d\d',page):
        return True
    elif re.findall('意乙 \d\d\d\d/\d\d/\d\d \d\d:\d\d',page):
        return True
    elif re.findall('葡超 \d\d\d\d/\d\d/\d\d \d\d:\d\d',page):
        return True
    elif re.findall('英冠 \d\d\d\d/\d\d/\d\d \d\d:\d\d',page):
        return True
    elif re.findall('英甲 \d\d\d\d/\d\d/\d\d \d\d:\d\d',page):
        return True
    elif re.findall('荷甲 \d\d\d\d/\d\d/\d\d \d\d:\d\d',page):
        return True
    elif re.findall('德乙 \d\d\d\d/\d\d/\d\d \d\d:\d\d',page):
        return True
for id in game_id:
    try:
        output = requests.get(f'https://live.leisu.com/oupei-{id}')
        if is_super_league(output.content.decode()) and '竞彩官方' in output.content.decode():
            # with open('idlist.txt','a') as idlistfile:
                # idlistfile.write(f'{id}')
            print(id)
        # if '竞彩官方' in output.content.decode():
        #     with open('idlist.txt','a') as idlistfile:
        #         # idlistfile.write(f'{id}')
        #         print(id)
    except ConnectionError:
        print('not connectable')