from termcolor import colored
import math
import matplotlib.pyplot as plt
from typing import List, Dict, Tuple, Union

# 冲榜积分
# 待填充

events = ["魔道争锋", "兽渊", "云梦", "天地弈局", "虚天殿"]
event_core_num = {
    "魔道争锋": 35,
    "兽渊": 90,
    "云梦": 40,
    "天地弈局": 80,
    "虚天殿": 38
}
event_core_needed_items = {
    "魔道争锋": 350,
    "兽渊": 305,
    "云梦": 450,
    "天地弈局": 600,
    "虚天殿": 900
}
tili_num_info = {
    "魔道争锋": 35,
    "云梦": 40,
    "天地弈局": 80,
    "虚天殿": 38
} # 活动体力次数
tili_needed_items = {
    "魔道争锋": 120,
    "云梦": 150,
    "天地弈局": 200,
    "虚天殿": 300
}

hourly_harvest_num = {
    "魔道争锋": 4,
    "兽渊": 8,
    "云梦": 6,
    "天地弈局": 16,
    "虚天殿": 12
}

jiasu_harvest_num = {
    "魔道争锋": [96, 192, 288, 384, 480, 576, 672, 768, 864, 960, 1056, 1152, 1248, 1344, 1440, 1536, 1632, 1728, 1824],
    "兽渊": [192, 384, 576, 768, 960, 1152, 1344, 1536, 1728, 1920, 2112, 2304, 2496, 2688, 2880, 3072, 3264, 3456, 3648],
    "云梦": [144, 288, 432, 576, 720, 864, 1008, 1152, 1296, 1440, 1584, 1728, 1872, 2016, 2160, 2304, 2448, 2592, 2736],
    "天地弈局": [384, 768, 1152, 1536, 1920, 2304, 2688, 3072, 3456, 3840, 4224, 4608, 4992, 5376, 5760, 6144, 6528, 6912, 7296],
    "虚天殿": [288, 576, 864, 1152, 1440, 1728, 2016, 2304, 2592, 2880, 3168, 3456, 3744, 4032, 4320, 4608, 4896, 5184, 5472]
}

faze_harvest_num = {
    "魔道争锋": 625,
    "兽渊": 1125,
    "云梦": 875,
    "天地弈局": 2250
    # "虚天殿": 待填充
}
def local_work(
    items_num: int,
    core_num: int,
    tili_num: int,
    event_name: str
):
    if event_name not in events:
        raise ValueError(f"event_name must be one of {events}")

    needed_core_num = event_core_num[event_name]
    core_num_to_get = needed_core_num - core_num
    core_needed_items_num_unit = event_core_needed_items[event_name]
    every_day_harvest_num = hourly_harvest_num[event_name] * 24 + jiasu_harvest_num[event_name][-1] + faze_harvest_num[event_name]

    if event_name != "兽渊":
        tili_num_to_get = tili_num_info[event_name] - tili_num
        tili_needed_items_num_unit = tili_needed_items[event_name]
        to_9000 = core_num_to_get * core_needed_items_num_unit + tili_num_to_get * tili_needed_items_num_unit
        to_9000_without_tili = core_num_to_get * core_needed_items_num_unit
        print(f"活动: {event_name}, 需要的道具数量: {to_9000}, 不考虑体力的情况下: {to_9000_without_tili}")
    else:
        to_9000 = core_num_to_get * core_needed_items_num_unit
        print(f"活动: {event_name}, 需要的道具数量: {to_9000}")

    print(colored(f"当前道具数量: {items_num}", 'green'))
    print(colored(f"每天的收获数量: {every_day_harvest_num}", 'green'))
    necc_days = round((to_9000 - items_num) / every_day_harvest_num, 2)
    necc_days_without_tili = round((to_9000_without_tili - items_num) / every_day_harvest_num, 2)
    print(f"活动: {event_name}, 需要的天数: {necc_days}, 不考虑体力的情况下: {necc_days_without_tili}")

if __name__ == "__main__":
    items_num = 10570
    core_num = 15
    tili_num = 16

    i = 3
    event_name = ["魔道争锋", "兽渊", "云梦", "天地弈局", "虚天殿"][i]
    local_work(items_num, core_num, tili_num, event_name)