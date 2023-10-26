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
    {'活动': '社团大比', '跨服': 4, '开始': '2023-10-10', '结束': '2023-10-10', '游戏天数(开始)': 2094, '游戏天数(结束)': 2094},
    {'活动': '魔道入侵', '跨服': 1, '开始': '2023-10-11', '结束': '2023-10-11', '游戏天数(开始)': 2095, '游戏天数(结束)': 2095},
    {'活动': '魔道入侵', '跨服': 2, '开始': '2023-10-12', '结束': '2023-10-12', '游戏天数(开始)': 2096, '游戏天数(结束)': 2096},
    {'活动': '炼体法相', '跨服': 2, '开始': '2023-10-12', '结束': '2023-10-13', '游戏天数(开始)': 2096, '游戏天数(结束)': 2097},
    {'活动': '兽渊探秘', '跨服': 2, '开始': '2023-10-13', '结束': '2023-10-14', '游戏天数(开始)': 2097, '游戏天数(结束)': 2098},
    {'活动': '社团花会', '跨服': 4, '开始': '2023-10-14', '结束': '2023-10-15', '游戏天数(开始)': 2098, '游戏天数(结束)': 2099},
    {'活动': '仙盟争霸', '跨服': 8, '开始': '2023-10-15', '结束': '2023-10-16', '游戏天数(开始)': 2099, '游戏天数(结束)': 2100},
    {'活动': '丹道问鼎', '跨服': 2, '开始': '2023-10-16', '结束': '2023-10-17', '游戏天数(开始)': 2100, '游戏天数(结束)': 2101},
    {'活动': '虚天殿', '跨服': 4, '开始': '2023-10-17', '结束': '2023-10-18', '游戏天数(开始)': 2101, '游戏天数(结束)': 2102},
    {'活动': '灵宠竞武', '跨服': 1, '开始': '2023-10-18', '结束': '2023-10-18', '游戏天数(开始)': 2102, '游戏天数(结束)': 2102},
    {'活动': '灵宠竞武', '跨服': 4, '开始': '2023-10-19', '结束': '2023-10-20', '游戏天数(开始)': 2103, '游戏天数(结束)': 2104},
    {'活动': '云梦试剑', '跨服': 2, '开始': '2023-10-19', '结束': '2023-10-19', '游戏天数(开始)': 2103, '游戏天数(结束)': 2103},
    {'活动': '升仙会', '跨服': 4, '开始': '2023-10-20', '结束': '2023-10-20', '游戏天数(开始)': 2104, '游戏天数(结束)': 2104},
    {'活动': '魔道入侵', '跨服': 1, '开始': '2023-10-21', '结束': '2023-10-21', '游戏天数(开始)': 2105, '游戏天数(结束)': 2105},
    {'活动': '魔道入侵', '跨服': 2, '开始': '2023-10-22', '结束': '2023-10-22', '游戏天数(开始)': 2106, '游戏天数(结束)': 2106},
    {'活动': '龙相竞舟', '跨服': 4, '开始': '2023-10-21', '结束': '2023-10-23', '游戏天数(开始)': 2105, '游戏天数(结束)': 2107},
    {'活动': '炼体法相', '跨服': 1, '开始': '2023-10-21', '结束': '2023-10-21', '游戏天数(开始)': 2105, '游戏天数(结束)': 2105},
    {'活动': '炼体法相', '跨服': 8, '开始': '2023-10-22', '结束': '2023-10-23', '游戏天数(开始)': 2106, '游戏天数(结束)': 2107},
    {'活动': '兽渊探秘', '跨服': 8, '开始': '2023-10-23', '结束': '2023-10-24', '游戏天数(开始)': 2107, '游戏天数(结束)': 2108},
    {'活动': '社团丹道', '跨服': 2, '开始': '2023-10-24', '结束': '2023-10-25', '游戏天数(开始)': 2108, '游戏天数(结束)': 2109},
    {'活动': '虚天殿', '跨服': 2, '开始': '2023-10-25', '结束': '2023-10-26', '游戏天数(开始)': 2109, '游戏天数(结束)': 2110},
    {'活动': '瑶池花会', '跨服': 2, '开始': '2023-10-26', '结束': '2023-10-27', '游戏天数(开始)': 2110, '游戏天数(结束)': 2111},
    {'活动': '天地弈局', '跨服': 1, '开始': '2023-10-27', '结束': '2023-10-27', '游戏天数(开始)': 2111, '游戏天数(结束)': 2111},
    {'活动': '天地弈局', '跨服': 4, '开始': '2023-10-28', '结束': '2023-10-28', '游戏天数(开始)': 2112, '游戏天数(结束)': 2112},
    {'活动': '灵宠竞武', '跨服': 2, '开始': '2023-10-28', '结束': '2023-10-29', '游戏天数(开始)': 2112, '游戏天数(结束)': 2113},
    {'活动': '社团大比', '跨服': 4, '开始': '2023-10-29', '结束': '2023-10-29', '游戏天数(开始)': 2113, '游戏天数(结束)': 2113},
    {'活动': '云梦试剑', '跨服': 4, '开始': '2023-10-30', '结束': '2023-10-30', '游戏天数(开始)': 2114, '游戏天数(结束)': 2114},
    {'活动': '社团炼体', '跨服': 4, '开始': '2023-10-30', '结束': '2023-10-31', '游戏天数(开始)': 2114, '游戏天数(结束)': 2115},
    {'活动': '洗灵证武', '跨服': 1, '开始': '2023-10-31', '结束': '2023-11-01', '游戏天数(开始)': 2115, '游戏天数(结束)': 2116},
    {'活动': '魔道入侵', '跨服': 1, '开始': '2023-10-31', '结束': '2023-10-31', '游戏天数(开始)': 2115, '游戏天数(结束)': 2115},
    {'活动': '魔道入侵', '跨服': 2, '开始': '2023-11-01', '结束': '2023-11-01', '游戏天数(开始)': 2116, '游戏天数(结束)': 2116},
    {'活动': '瑶池花会', '跨服': 1, '开始': '2023-11-02', '结束': '2023-11-02', '游戏天数(开始)': 2117, '游戏天数(结束)': 2117},
    {'活动': '虚天殿', '跨服': 4, '开始': '2023-11-02', '结束': '2023-11-03', '游戏天数(开始)': 2117, '游戏天数(结束)': 2118},
    {'活动': '瑶池花会', '跨服': 4, '开始': '2023-11-03', '结束': '2023-11-04', '游戏天数(开始)': 2118, '游戏天数(结束)': 2119},
    {'活动': '珍珑游宴', '跨服': 4, '开始': '2023-11-04', '结束': '2023-11-06', '游戏天数(开始)': 2119, '游戏天数(结束)': 2121},
    {'活动': '兽渊探秘', '跨服': 2, '开始': '2023-11-04', '结束': '2023-11-05', '游戏天数(开始)': 2119, '游戏天数(结束)': 2120},
    {'活动': '丹道问鼎', '跨服': 2, '开始': '2023-11-05', '结束': '2023-11-06', '游戏天数(开始)': 2120, '游戏天数(结束)': 2121},
    {'活动': '仙盟争霸', '跨服': 8, '开始': '2023-11-06', '结束': '2023-11-07', '游戏天数(开始)': 2121, '游戏天数(结束)': 2122},
    {'活动': '灵宠竞武', '跨服': 1, '开始': '2023-11-07', '结束': '2023-11-07', '游戏天数(开始)': 2122, '游戏天数(结束)': 2122},
    {'活动': '灵宠竞武', '跨服': 8, '开始': '2023-11-08', '结束': '2023-11-09', '游戏天数(开始)': 2123, '游戏天数(结束)': 2124},
    {'活动': '云梦试剑', '跨服': 2, '开始': '2023-11-08', '结束': '2023-11-08', '游戏天数(开始)': 2123, '游戏天数(结束)': 2123},
    {'活动': '升仙会', '跨服': 8, '开始': '2023-11-09', '结束': '2023-11-9', '游戏天数(开始)': 2124, '游戏天数(结束)': 2124},
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

# filter out events that are already over
data = data[data['剩余天数'].apply(lambda x: x.split('天')[0]).astype(int) >= 0]

print(tabulate(data, headers='keys', tablefmt='psql'))

data.to_csv('event_calendar.csv', index=False, encoding='utf-8-sig')