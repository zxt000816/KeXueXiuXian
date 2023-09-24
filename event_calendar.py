import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import re
from tabulate import tabulate

known_events = [
    {'活动': '魔道入侵', '跨服': 1, '开始': '2023-09-23', '结束': '2023-09-23', '游戏天数(开始)': 2077, '游戏天数(结束)': 2077},
    {'活动': '魔道入侵', '跨服': 2, '开始': '2023-09-24', '结束': '2023-09-24', '游戏天数(开始)': 2078, '游戏天数(结束)': 2078},
    {'活动': '瑶池花会', '跨服': 2, '开始': '2023-09-24', '结束': '2023-09-25', '游戏天数(开始)': 2078, '游戏天数(结束)': 2079},
    {'活动': '兽渊探秘', '跨服': 4, '开始': '2023-09-25', '结束': '2023-09-26', '游戏天数(开始)': 2079, '游戏天数(结束)': 2080},
    {'活动': '社团丹道', '跨服': 2, '开始': '2023-09-26', '结束': '2023-09-27', '游戏天数(开始)': 2080, '游戏天数(结束)': 2081},
    {'活动': '天地弈局', '跨服': 1, '开始': '2023-09-27', '结束': '2023-09-27', '游戏天数(开始)': 2081, '游戏天数(结束)': 2081},
    {'活动': '天地弈局', '跨服': 4, '开始': '2023-09-28', '结束': '2023-09-28', '游戏天数(开始)': 2082, '游戏天数(结束)': 2082},
    {'活动': '灵宠竞武', '跨服': 2, '开始': '2023-09-28', '结束': '2023-09-29', '游戏天数(开始)': 2082, '游戏天数(结束)': 2083},
    {'活动': '升仙会', '跨服': 4, '开始': '2023-09-29', '结束': '2023-09-29', '游戏天数(开始)': 2083, '游戏天数(结束)': 2083},
    {'活动': '魔道入侵', '跨服': 1, '开始': '2023-10-01', '结束': '2023-10-01', '游戏天数(开始)': 2085, '游戏天数(结束)': 2085},
    {'活动': '魔道入侵', '跨服': 4, '开始': '2023-10-02', '结束': '2023-10-02', '游戏天数(开始)': 2086, '游戏天数(结束)': 2086},
    {'活动': '虚天殿', '跨服': 2, '开始': '2023-10-03', '结束': '2023-10-04', '游戏天数(开始)': 2087, '游戏天数(结束)': 2088},
    {'活动': '瑶池花会', '跨服': 1, '开始': '2023-10-03', '结束': '2023-10-03', '游戏天数(开始)': 2087, '游戏天数(结束)': 2087},
    {'活动': '瑶池花会', '跨服': 8, '开始': '2023-10-04', '结束': '2023-10-05', '游戏天数(开始)': 2088, '游戏天数(结束)': 2089},
    {'活动': '兽渊探秘', '跨服': 2, '开始': '2023-10-05', '结束': '2023-10-06', '游戏天数(开始)': 2089, '游戏天数(结束)': 2090},
    {'活动': '社团灵宠', '跨服': 2, '开始': '2023-10-06', '结束': '2023-10-07', '游戏天数(开始)': 2090, '游戏天数(结束)': 2091},
    {'活动': '天地弈局', '跨服': 1, '开始': '2023-10-07', '结束': '2023-10-07', '游戏天数(开始)': 2091, '游戏天数(结束)': 2091},
    {'活动': '天地弈局', '跨服': 8, '开始': '2023-10-08', '结束': '2023-10-09', '游戏天数(开始)': 2092, '游戏天数(结束)': 2093},
    {'活动': '丹道问鼎', '跨服': 1, '开始': '2023-10-08', '结束': '2023-10-08', '游戏天数(开始)': 2092, '游戏天数(结束)': 2092},
    {'活动': '丹道问鼎', '跨服': 4, '开始': '2023-10-09', '结束': '2023-10-10', '游戏天数(开始)': 2093, '游戏天数(结束)': 2094},
    {'活动': '社团大比', '跨服': 4, '开始': '2023-10-10', '结束': '2023-10-10', '游戏天数(开始)': 2094, '游戏天数(结束)': 2094}
]

data = pd.DataFrame(known_events)
today = datetime.today().replace(hour=0, minute=0, second=0, microsecond=0)

data['剩余天数'] = data['结束'].apply(lambda x: (datetime.strptime(x, '%Y-%m-%d') - today).days)

event_names = []
for _tuple in data[['活动', '跨服']].itertuples():
    event_name, num_of_servers = _tuple[1], _tuple[2]
    if num_of_servers == 1:
        event_names.append(f"{event_name}预赛")
    else:
        event_names.append(f"{event_name}跨服[{num_of_servers}]")

data['活动'] = event_names
data['剩余天数'] = data['剩余天数'].apply(lambda x: f"{x}天")
data = data[['活动', '剩余天数', '开始', '结束', '游戏天数(开始)', '游戏天数(结束)']]

print(tabulate(data, headers='keys', tablefmt='psql'))
data.to_csv('event_calendar.csv', index=False, encoding='utf-8-sig')