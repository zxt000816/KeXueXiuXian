import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import re
from tabulate import tabulate
from event_items import daily_work

date_events = [
    {'date': '2023-08-26', 'event': '虚天殿跨服[2]*S'},
    {'date': '2023-08-27', 'event': '虚天殿跨服[2]*E;灵宠竞武预赛*S'},
    {'date': '2023-08-28', 'event': '灵宠竞武预赛*E;天地弈局预赛*E'},
    {'date': '2023-08-29', 'event': '天地弈局跨服[4]*E;瑶池花会跨服[2]*S'},
    {'date': '2023-08-30', 'event': '瑶池花会跨服[2]*E;兽渊探秘跨服[2]*S'},
    {'date': '2023-08-31', 'event': '兽渊探秘跨服[2]*E;丹道问鼎跨服[2]*S'},
    {'date': '2023-09-01', 'event': '丹道问鼎跨服[2]*E;升仙会跨服[2]*E'},
    {'date': '2023-09-02', 'event': '云梦试剑跨服[2]*E'},
    {'date': '2023-09-03', 'event': '魔道入侵预赛*E;炼体法相预赛*E'},
    {'date': '2023-09-04', 'event': '魔道入侵跨服[2]*E'},
    {'date': '2023-09-05', 'event': '炼体法相跨服[4]*E'},
    {'date': '2023-09-06', 'event': '虚天殿跨服[2]*E;灵宠竞武跨服[2]*S'},
    {'date': '2023-09-07', 'event': '灵宠竞武跨服[2]*E;天地弈局预赛*E'},
    {'date': '2023-09-08', 'event': '天地弈局跨服[4]*E;丹道问鼎跨服[2]*S'},
    {'date': '2023-09-09', 'event': '丹道问鼎跨服[2]*E'},
    {'date': '2023-09-10', 'event': '云梦试剑跨服[2]*E;炼体法相跨服[2]*S'},
    {'date': '2023-09-11', 'event': '炼体法相跨服[2]*E;升仙会跨服[2]*E'},
    {'date': '2023-09-12', 'event': '魔道入侵预赛*E'},
    {'date': '2023-09-13', 'event': '魔道入侵跨服[2]*E;瑶池花会跨服[2]*S'},
    {'date': '2023-09-14', 'event': '瑶池花会跨服[2]*E;兽渊探秘跨服[4]*S'},
    {'date': '2023-09-15', 'event': '兽渊探秘跨服[4]*E;丹道问鼎预赛*E'},
    {'date': '2023-09-16', 'event': '社团大比跨服[2]*E'},
    {'date': '2023-09-17', 'event': '丹道问鼎跨服[8]*E'},
]

date_events_df = pd.DataFrame(date_events)
date_events_df['date'] = pd.to_datetime(date_events_df['date'])

event1_template = {'预赛': None, '跨服[2]': None, '跨服[4]': None, '跨服[8]': None}
event2_template = {'*S': None, '*E': None}
event_last_date = {
    '魔道入侵': event1_template.copy(),
    '虚天殿': event1_template.copy(),
    '天地弈局': event1_template.copy(),
    '兽渊探秘': event1_template.copy(),
    '云梦试剑': event1_template.copy(),
    '升仙会': event1_template.copy(),
    '社团大比': event1_template.copy(),
    '丹道问鼎': event1_template.copy(),
    '瑶池花会': event1_template.copy(),
    '炼体法相': event1_template.copy(),
    '灵宠竞武': event1_template.copy(),
}

event_regex = r'(?P<event_name>魔道入侵|虚天殿|天地弈局|兽渊探秘|云梦试剑|升仙会|社团大比|丹道问鼎|瑶池花会|炼体法相|灵宠竞武|丹道问鼎)'
event_type_regex = r'(?P<event_type>预赛|跨服\[2\]|跨服\[4\]|跨服\[8\])'
event_time_regex = r'(?P<event_time>\*S|\*E)'

for _tuple in date_events_df.itertuples(index=False):
    _date, _events = _tuple
    if _events == '':
        continue

    _events = _events.split(';')
    for _event in _events:
        _event = _event.strip()
        _event_name = re.search(event_regex, _event).group('event_name')
        _event_type = re.search(event_type_regex, _event).group('event_type')
        _event_time = re.search(event_time_regex, _event).group('event_time')
        
        if _event_time == '*E':
            prev_event_time = event_last_date[_event_name][_event_type]
            if prev_event_time is None:
                event_last_date[_event_name][_event_type] = _date
            else:
                if prev_event_time < _date:
                    event_last_date[_event_name][_event_type] = _date

# 计算各个活动距离现在的天数, 如果是负数, 则表示已经结束
results = []
for _event_name, _event_info in event_last_date.items():
    for _event_type, _event_date in _event_info.items():
        if _event_date is None:
            _event_last_days = np.nan
        else:
            _event_last_days = (_event_date - datetime.now()).days + 1
        
        results.append({
            'event_name': _event_name,
            'event_type': _event_type,
            'event_date': _event_date,
            'event_last_days': _event_last_days
        })

linggen_events = ["魔道入侵", "兽渊探秘", "云梦试剑", "天地弈局", "虚天殿"]

results_df = pd.DataFrame(results).dropna()
results_df['event_last_days'] = results_df['event_last_days'].astype(int)
results_df = results_df[results_df['event_name'].isin(linggen_events)]

future_events = results_df[results_df['event_last_days'] >= 0].sort_values(by=['event_last_days'], ascending=True)
past_events = results_df[results_df['event_last_days'] < 0].sort_values(by=['event_last_days'], ascending=False)

###########################################################################

items_num_dict = {"魔道入侵": 55, "兽渊探秘": 208,  "云梦试剑": 410, "天地弈局": 572,  "虚天殿": 316} # 材料数量
core_num_dict = {"魔道入侵": 6, "兽渊探秘": 16, "云梦试剑": 40, "天地弈局": 18, "虚天殿": 18} # 四倍数量
tili_num_dict = {"魔道入侵": 0, "兽渊探秘": 0, "云梦试剑": 0, "天地弈局": 0, "虚天殿": 0} # 活动体力次数

cost_days = 0
# events_want_to_confirm = ["魔道入侵", "兽渊探秘", "云梦试剑", "天地弈局", "虚天殿"]
events_want_to_confirm = ["魔道入侵", "云梦试剑", "兽渊探秘", ]
print(tabulate(future_events, headers='keys', tablefmt='psql'))
for future_event in future_events.itertuples(index=True):
    idx, event_name, event_type, event_date, event_last_days = future_event
    if event_name not in events_want_to_confirm:
        continue
    items_num = items_num_dict[event_name]
    core_num = core_num_dict[event_name]
    tili_num = tili_num_dict[event_name]
    inference = daily_work(items_num, core_num, tili_num, event_name, 23)
    
    print("=" * 100)
    print(f"活动: {event_name}, 类型: {event_type}, 还剩: {event_last_days}天, 日期: {event_date}")
    for key, value in inference.items():
        if key == "活动":
            continue
        print(f"{key}: {value}")
    
    cost_days = event_last_days