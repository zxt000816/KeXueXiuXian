events = ["魔道入侵", "兽渊探秘", "云梦试剑", "天地弈局", "虚天殿"]

event_core_num = {
    "魔道入侵": 29,
    "兽渊探秘": 80,
    "云梦试剑": 40,
    "天地弈局": 80,
    "虚天殿": 38
}

target_points = 14000
for event in events:
    points_per_event_core = 9000 / event_core_num[event]
    print(f"{event}, 每个四倍/探查获得的兑换积分: ", points_per_event_core)
    print(f"{event}, 达到14000积分需要的四倍/探查数量: ", round(target_points / points_per_event_core, 1))