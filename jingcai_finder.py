'''
1.在网上找到比赛，过滤，然后复制比赛html到 https://regex101.com/
2. 用这个regex <li class=\"list-item list-item-(\d\d\d\d\d\d\d) list-day-12-13 notStart\"
   过滤出所有顶级比赛
3.用内置软件得到id list， 并用http://quchuchongfu.renrensousuo.com/ 去重
4. 导入list到idlist.txt， 用竞彩finder 找到竞彩开出的比赛 和 非竞彩比赛
5. 得到竞彩list 和非竞彩list，取得两个list赔率 分别测试信心值
6.计入统计
'''
import requests
import csv
with open('idlist.txt','r') as idlistfile:
    res = csv.reader(idlistfile)
    rows = [row for row in res]
id_list = []
for i in rows:
    for id in i:
        id_list.append(id)
for id in id_list:
    try:
        output = requests.get(f'https://live.leisu.com/oupei-{id}')
        # if is_super_league(output.content.decode()) and '竞彩官方' in output.content.decode():
        #     # with open('idlist.txt','a') as idlistfile:
        #         # idlistfile.write(f'{id}')
        #     print(id)
        if '竞彩官方' in output.content.decode():
            with open('idlist.txt','a') as idlistfile:
                # idlistfile.write(f'{id}')
                print(id)
    except ConnectionError:
        print('not connectable')
