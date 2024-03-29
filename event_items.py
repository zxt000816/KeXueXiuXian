events = ["魔道入侵", "兽渊探秘", "云梦试剑", "天地弈局", "虚天殿"]

event_core_num = {
    "魔道入侵": 29,
    "兽渊探秘": 80,
    "云梦试剑": 40,
    "天地弈局": 80,
    "虚天殿": 38
}

event_score_per_core = {
    "魔道入侵": 9000 / event_core_num["魔道入侵"],
    "兽渊探秘": 9000 / event_core_num["兽渊探秘"],
    "云梦试剑": 9000 / event_core_num["云梦试剑"],
    "天地弈局": 9000 / event_core_num["天地弈局"],
    "虚天殿": 9000 / event_core_num["虚天殿"]
}

event_core_needed_items = {
    "魔道入侵": 350,
    "兽渊探秘": 305,
    "云梦试剑": 450,
    "天地弈局": 600,
    "虚天殿": 900
}

tili_needed_items = {
    "魔道入侵": 120,
    "云梦试剑": 150,
    "天地弈局": 200,
    "虚天殿": 300
}

hourly_harvest_num = {
    "魔道入侵": 4,
    "兽渊探秘": 8,
    "云梦试剑": 6,
    "天地弈局": 16,
    "虚天殿": 12
}

jiasu_harvest_num = {
    "魔道入侵": [
        96, 192, 288, 384, 480, 576, 672, 768, 864, 960, 
        1056, 1152, 1248, 1344, 1440, 1536, 1632, 1728, 1824, 1920, 
        2016, 2112, 2208, 2304, 2400, 2496, 2592
    ],
    "兽渊探秘": [
        192, 384, 576, 768, 960, 1152, 1344, 1536, 1728, 1920, 
        2112, 2304, 2496, 2688, 2880, 3072, 3264, 3456, 3648, 3840, 
        4032, 4224, 4416, 4608, 4800, 4992, 5184
    ],
    "云梦试剑": [
        144, 288, 432, 576, 720, 864, 1008, 1152, 1296, 1440, 
        1584, 1728, 1872, 2016, 2160, 2304, 2448, 2592, 2736, 2880, 
        3024, 3168, 3312, 3456, 3600, 3744, 3888
    ],
    "天地弈局": [
        384, 768, 1152, 1536, 1920, 2304, 2688, 3072, 3456, 3840, 
        4224, 4608, 4992, 5376, 5760, 6144, 6528, 6912, 7296, 7680, 
        8064, 8448, 8832, 9216, 9600, 9984, 10368
    ],
    "虚天殿": [
        288, 576, 864, 1152, 1440, 1728, 2016, 2304, 2592, 2880, 
        3168, 3456, 3744, 4032, 4320, 4608, 4896, 5184, 5472, 5760, 
        6048, 6336, 6624, 6912, 7200, 7488, 7776
    ]
}

faze_harvest_num = {
    "魔道入侵": 625,
    "兽渊探秘": 1125,
    "云梦试剑": 875,
    "天地弈局": 2250,
    "虚天殿": 2100
}
def daily_work(
    items_num: int, # 现有材料数量
    core_num: int, # 现有四倍/探查数量
    tili_num: int, # 现有体力次数
    event_name: str, # 活动名称
    jiasu_num: int = 27, # 加速次数
    target_score: int = 9000
):
    if event_name not in events:
        raise ValueError(f"event_name must be one of {events}")

    needed_core_num = target_score / event_score_per_core[event_name] # 需要的四倍数量
    needed_tili_num = needed_core_num # 需要的体力次数(等于四倍数量)
    core_num_to_get = needed_core_num - core_num # 实际需要的四倍数量 = 需要的四倍数量 - 现有四倍数量
    core_needed_items_num_unit = event_core_needed_items[event_name] # 每个四倍/探查需要的材料数量

    # 每天的收获数量 = 每小时的收获数量 * 24 + 加速收获数量 + 法则收获数量
    every_day_harvest_num = hourly_harvest_num[event_name] * 24 + jiasu_harvest_num[event_name][jiasu_num-1] + faze_harvest_num[event_name]

    # 兽渊探秘不需要体力, 其他活动需要体力
    if event_name != "兽渊探秘":
        # 实际需要的体力次数 = 需要的体力次数 - 现有体力次数
        tili_num_to_get = needed_tili_num - tili_num
        tili_needed_items_num_unit = tili_needed_items[event_name] # 每个体力需要的材料数量

        # 实际需要的材料数量 = 实际需要的四倍数量 * 每个四倍/探查需要的材料数量 + 实际需要的体力次数 * 每个体力需要的材料数量
        items_num_to_target_score = core_num_to_get * core_needed_items_num_unit + tili_num_to_get * tili_needed_items_num_unit
        
        # 不考虑体力的实际需要的材料数量 = 实际需要的四倍数量 * 每个四倍/探查需要的材料数量
        items_num_to_target_score_without_tili = core_num_to_get * core_needed_items_num_unit
        
        # 实际需要的天数 = (实际需要的材料数量 - 现有材料数量) / 每天的收获数量
        necc_days = round((items_num_to_target_score - items_num) / every_day_harvest_num, 2)
        
        # 不考虑体力的实际需要的天数 = (不考虑体力的实际需要的材料数量 - 现有材料数量) / 每天的收获数量
        necc_days_without_tili = round((items_num_to_target_score_without_tili - items_num) / every_day_harvest_num, 2)

        return {
            "活动": event_name,
            f"{target_score}兑换积分需要的材料数量": round(items_num_to_target_score, 2),
            f"{target_score}兑换积分需要的材料数量(不考虑体力)": round(items_num_to_target_score_without_tili, 2),
            f"{target_score}兑换积分需要的四倍数量": round(core_num_to_get, 2),
            f"分割线": True,
            f"加速次数": jiasu_num,
            "当前材料数量": items_num,
            "每天的收获数量": every_day_harvest_num,
            f"{target_score}兑换积分需要的天数": necc_days,
            f"{target_score}兑换积分需要的天数(不考虑体力)": necc_days_without_tili
        }
    else:
        # 实际需要的材料数量 = 实际需要的四倍数量 * 每个四倍/探查需要的材料数量
        items_num_to_target_score = core_num_to_get * core_needed_items_num_unit
        necc_days = round((items_num_to_target_score - items_num) / every_day_harvest_num, 2)
        return {
            "活动": event_name,
            f"{target_score}兑换积分需要的材料数量": items_num_to_target_score,
            f"{target_score}兑换积分需要的探查符数量": core_num_to_get,
            f"分割线": True,
            f"加速次数": jiasu_num,
            "当前材料数量": items_num,
            "每天的收获数量": every_day_harvest_num,
            f"{target_score}兑换积分需要的天数": necc_days
        }

if __name__ == "__main__":
    events = ["魔道入侵", "兽渊探秘", "云梦试剑", "天地弈局", "虚天殿"]

    items_num_dict = {"魔道入侵": 133, "兽渊探秘": 185,  "云梦试剑": 718, "天地弈局": 2092,  "虚天殿": 20632} # 材料数量
    core_num_dict = {"魔道入侵": 1, "兽渊探秘": 62, "云梦试剑": 2, "天地弈局": 6, "虚天殿": 2} # 四倍数量
    tili_num_dict = {"魔道入侵": 3, "兽渊探秘": 0, "云梦试剑": 0, "天地弈局": 0, "虚天殿": 0} # 活动体力次数

    for event in events:
        items_num = items_num_dict[event]
        core_num = core_num_dict[event]
        tili_num = tili_num_dict[event]
        inference = daily_work(items_num, core_num, tili_num, event, 19)

        print(inference)

