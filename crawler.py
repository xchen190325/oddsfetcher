from translate import Translator
import csv
import re
import pandas as pd
import requests
with open('idlist.txt','r') as id_file:
    res = csv.reader(id_file)
    row = [row for row in res]
ids_list = []
for item in row:
    for i in item:
        ids_list.append(i)
trans = Translator(from_lang="chinese",to_lang="english")

hg,li,b5,sna,wl,ms,ao,inte,pin,b10,ysb,w = '','','','','','','','','','','',''
res = requests.get('https://live.leisu.com/')
pattern = '\[(3\d\d\d\d\d\d)'
game_type_pattern = '<\/div><\/div><div class=\"team-center\"><div class=\"clearfix-row\"> (.*) 2020\/12\/10 01:55<\/div><div'
ids = re.findall(pattern,res.content.decode())
name_pattern = '<span class="line-h-22 float-left m-l-5 w-105 word-break text-a-l">( .{2,15} )<\/span><\/'
odds_pattern = '<div class=\"begin float-left w-bar-100 bd-bottom p-b-8 color-999 m-b-8\"><span class=\"float-left col-3\"> (.{2,15}) </span>'
# ids_list = ['3462698','3462651','3462650','3462639','3462638','3462627','3462626','3462615','3462614']
team_1_pattern = '<div class=\"name\"><span class=\"display-i-b line-h-25\"> (.*)</span></div><div class=\"team-icon\"'
team_2_pattern = '\"></div><div class=\"name\"><span class=\"display-i-b line-h-25\">(.*) </span></div></div></div></div><div class=\"nav-panel\"><div class=\"content children\"><ul class=\"nav-list\"><li><a class=\"link '
def listToString(s):
    str1 = " "
    return (str1.join(s))

def is_super_league(page):
    # if '欧冠杯' or '英超' or '欧联杯' or '意甲' or '法甲' or '德甲' or '西甲' in page:
    #     return True
    if re.findall('欧冠杯 \d\d\d\d/\d\d/\d\d \d\d:\d\d',page):
        return True
for id in ids_list:
  odds_page = requests.get(f'https://live.leisu.com/oupei-{id}')
  page_content = odds_page.content.decode()
  odds_346 = re.findall(odds_pattern,page_content)
  game_type = listToString(re.findall(game_type_pattern,page_content))
  # game_type = trans.translate(game_type)
  team_1_name = listToString(re.findall(team_1_pattern,page_content))
  team_2_name = listToString(re.findall(team_2_pattern,page_content))
  # team_1_name = trans.translate(team_1_name)
  # team_2_name = trans.translate(team_2_name)
  print(game_type, team_1_name, team_2_name)
  name = re.findall(name_pattern,page_content)
  name = ['Bet365'] + name
  list_res = zip(name,odds_346)
  list_odds = []
  for item in list_res:
      list_odds.append(item)
  print(list_odds)
  for item in list_odds:
      # print(item[0].strip(),item[1])
      if item[0].strip() == 'Bet365':
          print(item[0].strip(),item[1])
          b5 = item[1]
      if item[0].strip() == '皇冠':
          print(item[0].strip(),item[1])
          hg = item[1]
      if item[0].strip() == '10BET':
          print(item[0].strip(),item[1])
          b10 = item[1]
      if item[0].strip() == '立博':
          print(item[0].strip(),item[1])
          li = item[1]
      if item[0].strip() == '明陞':
          print(item[0].strip(),item[1])
          ms = item[1]
      if item[0].strip() == '澳彩':
          print(item[0].strip(),item[1])
          ao = item[1]
      if item[0].strip() == 'SNAI':
          print(item[0].strip(),item[1])
          sna = item[1]
      if item[0].strip() == '威廉希尔':
          print(item[0].strip(),item[1])
          wl = item[1]
      if item[0].strip() == '易胜博':
          print(item[0].strip(),item[1])
          ysb = item[1]
      if item[0].strip() == '韦德':
          print(item[0].strip(),item[1])
          w = item[1]
      if item[0].strip() == 'Inter wetten':
          print(item[0].strip(),item[1])
          inte = item[1]
      if item[0].strip() == '10BET':
          print(item[0].strip(),item[1])
          b10 = item[1]
      if item[0].strip() == '平博':
          print(item[0].strip(),item[1])
          pin = item[1]
  with open('oddsList.csv','a') as file:
      file.write(f'{team_1_name + " " + team_2_name },{hg},{li},{b5},{sna},{wl},{ms},{ao},{inte}, ,{game_type},{pin},{b10},{ysb},{w},\n')