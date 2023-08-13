from termcolor import colored
import math
import matplotlib.pyplot as plt
from typing import List, Dict, Tuple, Union

# 魔道入侵道具
modao_sibei = 350  # 四倍
modao_cumoling = 120 # 次数
modap_tainyanfu = 20 # 天眼符
# 兽渊道具
shouyuan_tancanfu = 305 # 探查符
# 云梦道具
yunmeng_sibei = 450 # 四倍
yunmeng_lunjianling = 150 # 次数
# 天地弈局道具
yiqi_sibei = 600 # 四倍
yiqi_xianyihe = 200 # 次数
yiqi_maifu = 750

#### 已有四倍 ###
num_owed_modao_sibei = 5
num_owned_shouyuan_tancanfu = 6
num_owed_yunmeng_sibei = 3
num_owed_yiqi_sibei = 3

#### 获取次数 ###
num_modao_sibei_to_get = 35 - num_owed_modao_sibei
num_shouyuan_tancanfu_to_get = 90 - num_owned_shouyuan_tancanfu
num_yunmeng_sibei_to_get = 40 - num_owed_yunmeng_sibei
num_yiqi_sibei_to_get = 80 - num_owed_yiqi_sibei

# 获取五行灵根
## 魔道
to_9000_modao = modao_sibei * num_modao_sibei_to_get + modao_cumoling * 35
to_9000_modao_only_sibei = modao_sibei * num_modao_sibei_to_get
## 兽渊
to_9000_shouyuan = shouyuan_tancanfu * num_shouyuan_tancanfu_to_get
## 云梦
to_9000_yunmeng = yunmeng_sibei * num_yunmeng_sibei_to_get + yunmeng_lunjianling * 40
to_9000_yunmeng_only_sibei = yunmeng_sibei * num_yunmeng_sibei_to_get
## 天地弈局
to_9000_yiqi = yiqi_sibei * num_yiqi_sibei_to_get + yiqi_xianyihe * 80
to_9000_yiqi_only_sibei = yiqi_sibei * num_yiqi_sibei_to_get

# 冲榜积分
# 待填充
tianleizu_hour = 4 # 天雷竹每小时产量
xinghaihuoshu_hour = 8 # 星海火树每小时产量
xuanyuhulu_hour = 6 # 玄玉葫芦每小时产量
lingyanshenshu_hour = 16 # 灵眼神树每小时产量

tanleiju_jiasu_shouhuo = [
    96, 192, 288, 384, 480, 576, 672, 768, 864, 960, 
    1056, 1152, 1248, 1344, 1440, 1536, 1632, 1728, 1824
] # 天雷竹加速
xinghaihuoshu_jiasu_shouhuo = [
    192, 384, 576, 768, 960, 1152, 1344, 1536, 1728, 1920,
    2112, 2304, 2496, 2688, 2880, 3072, 3264, 3456, 3648
] # 星海火树加速
xuanyuhulu_jiasu_shouhuo = [
    144, 288, 432, 576, 720, 864, 1008, 1152, 1296, 1440,
    1584, 1728, 1872, 2016, 2160, 2304, 2448, 2592, 2736
] # 玄玉葫芦加速
lingyanshenshu_jiasu_shouhuo = [
    384, 768, 1152, 1536, 1920, 2304, 2688, 3072, 3456, 3840,
    4224, 4608, 4992, 5376, 5760, 6144, 6528, 6912, 7296
] # 灵眼神树加速
jiasu_linshi = [
    0, 8, 20, 36, 56, 80, 108, 140, 176, 216, 
    260, 308, 360, 416, 476, 540, 608, 680, 756
] # 加速19次所消耗的灵石

def local_work(
    items_num_now: Dict, # 当前拥有的道具数量
    jiasu_select: str # 选择加速的道具
):
    # 当前拥有的道具数量
    tianleizu_now = items_num_now['tianleizu']
    xinghaihuoshu_now = items_num_now['xinghaihuoshu']
    xuanyuhulu_now = items_num_now['xuanyuhulu']
    lingyanshenshu_now = items_num_now['lingyanshenshu']

    # 根据选择的加速道具，计算每天的产量
    if jiasu_select == 'tianleizu':
        tianleizu_eveyrday = tianleizu_hour * 24 + tanleiju_jiasu_shouhuo[-1] + 625
        xinghaihuoshu_everyday = xinghaihuoshu_hour * 24
        xuanyuhulu_everyday = xuanyuhulu_hour * 24
        lingyanshenshu_everyday = lingyanshenshu_hour * 24
    elif jiasu_select == 'xinghaihuoshu':
        tianleizu_eveyrday = tianleizu_hour * 24
        xinghaihuoshu_everyday = xinghaihuoshu_hour * 24 + xinghaihuoshu_jiasu_shouhuo[-1] + 1125
        xuanyuhulu_everyday = xuanyuhulu_hour * 24
        lingyanshenshu_everyday = lingyanshenshu_hour * 24
    elif jiasu_select == 'xuanyuhulu':
        tianleizu_eveyrday = tianleizu_hour * 24
        xinghaihuoshu_everyday = xinghaihuoshu_hour * 24
        xuanyuhulu_everyday = xuanyuhulu_hour * 24 + xuanyuhulu_jiasu_shouhuo[-1] + 875
        lingyanshenshu_everyday = lingyanshenshu_hour * 24
    elif jiasu_select == 'lingyanshenshu':
        tianleizu_eveyrday = tianleizu_hour * 24
        xinghaihuoshu_everyday = xinghaihuoshu_hour * 24
        xuanyuhulu_everyday = xuanyuhulu_hour * 24
        lingyanshenshu_everyday = lingyanshenshu_hour * 24 + lingyanshenshu_jiasu_shouhuo[-1] + 2250

    # 计算获取五行灵根所需的天数
    necc_days_modao = (to_9000_modao - tianleizu_now) / tianleizu_eveyrday
    necc_days_modao_only_sibei = (to_9000_modao_only_sibei - tianleizu_now) / tianleizu_eveyrday
    necc_days_shouyuan = (to_9000_shouyuan - xinghaihuoshu_now) / xinghaihuoshu_everyday
    necc_days_yunmeng = (to_9000_yunmeng - xuanyuhulu_now) / xuanyuhulu_everyday
    necc_days_yunmeng_only_sibei = (to_9000_yunmeng_only_sibei - xuanyuhulu_now) / xuanyuhulu_everyday
    necc_days_yiqi = (to_9000_yiqi - lingyanshenshu_now) / lingyanshenshu_everyday
    necc_days_yiqi_only_sibei = (to_9000_yiqi_only_sibei - lingyanshenshu_now) / lingyanshenshu_everyday

    print(colored(f"获取魔道争锋-五行灵根需要的天数, 考虑次数的情况下: {necc_days_modao}, 不考虑次数的情况下: {necc_days_modao_only_sibei}", "green" if jiasu_select == 'tianleizu' else "red"))
    print(colored(f"获取兽渊-五行灵根需要的天数: {necc_days_shouyuan}", "green" if jiasu_select == 'xinghaihuoshu' else "red"))
    print(colored(f"获取云梦-五行灵根需要的天数, 考虑次数的情况下: {necc_days_yunmeng}, 不考虑次数的情况下: {necc_days_yunmeng_only_sibei}", "green" if jiasu_select == 'xuanyuhulu' else "red"))
    print(colored(f"获取天地弈局-五行灵根需要的天数, 考虑次数的情况下: {necc_days_yiqi}, 不考虑次数的情况下: {necc_days_yiqi_only_sibei}", "green" if jiasu_select == 'lingyanshenshu' else "red"))

def global_work(
    items_num_now: Dict, # 当前拥有的道具数量
    jiansu_plan: Dict # 加速计划
):
    # 获取每个加速道具的加速次数
    tianleizu_plan = jiansu_plan['tianleizu']
    xinghaihuoshu_plan = jiansu_plan['xinghaihuoshu']
    xuanyuhulu_plan = jiansu_plan['xuanyuhulu']
    lingyanshenshu_plan = jiansu_plan['lingyanshenshu']

    # 目前拥有的道具数量
    tianleizu_now = items_num_now['tianleizu']
    xinghaihuoshu_now = items_num_now['xinghaihuoshu']
    xuanyuhulu_now = items_num_now['xuanyuhulu']
    lingyanshenshu_now = items_num_now['lingyanshenshu']

    # 计算每个道具每天的收获量
    tianleizu_eveyrday = tianleizu_hour * 24 + tanleiju_jiasu_shouhuo[tianleizu_plan] + 625*1/7
    xinghaihuoshu_everyday = xinghaihuoshu_hour * 24 + xinghaihuoshu_jiasu_shouhuo[xinghaihuoshu_plan] + 1125*1/7
    xuanyuhulu_everyday = xuanyuhulu_hour * 24 + xuanyuhulu_jiasu_shouhuo[xuanyuhulu_plan] + 875*1/7
    lingyanshenshu_everyday = lingyanshenshu_hour * 24 + lingyanshenshu_jiasu_shouhuo[lingyanshenshu_plan] + 2250*1/7

    # 计算获得五行灵根所需的天数
    necc_days_modao = (to_9000_modao - tianleizu_now) / tianleizu_eveyrday
    necc_days_modao_only_sibei = (to_9000_modao_only_sibei - tianleizu_now) / tianleizu_eveyrday
    necc_days_shouyuan = (to_9000_shouyuan - xinghaihuoshu_now) / xinghaihuoshu_everyday
    necc_days_yunmeng = (to_9000_yunmeng - xuanyuhulu_now) / xuanyuhulu_everyday
    necc_days_yunmeng_only_sibei = (to_9000_yunmeng_only_sibei - xuanyuhulu_now) / xuanyuhulu_everyday
    necc_days_yiqi = (to_9000_yiqi - lingyanshenshu_now) / lingyanshenshu_everyday
    necc_days_yiqi_only_sibei = (to_9000_yiqi_only_sibei - lingyanshenshu_now) / lingyanshenshu_everyday

    print(colored(f"获取魔道争锋-五行灵根需要的天数, 考虑次数的情况下: {necc_days_modao}, 不考虑次数的情况下: {necc_days_modao_only_sibei}", "green"))
    print(colored(f"获取兽渊-五行灵根需要的天数: {necc_days_shouyuan}", "green"))
    print(colored(f"获取云梦-五行灵根需要的天数, 考虑次数的情况下: {necc_days_yunmeng}, 不考虑次数的情况下: {necc_days_yunmeng_only_sibei}", "green"))
    print(colored(f"获取天地弈局-五行灵根需要的天数, 考虑次数的情况下: {necc_days_yiqi}, 不考虑次数的情况下: {necc_days_yiqi_only_sibei}", "green"))

if __name__ == "__main__":
    items_num_now = {
        "tianleizu": 14853,
        "xinghaihuoshu": 1639,
        "xuanyuhulu": 684,
        "lingyanshenshu": 3484
    }
    # jiasu_plan = {
    #     "tianleizu": 4,
    #     "xinghaihuoshu": 5,
    #     "xuanyuhulu": 5,
    #     "lingyanshenshu": 5
    # }

    for key in items_num_now.keys():
        print("=" * 100)
        local_work(items_num_now, key)