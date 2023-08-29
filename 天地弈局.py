from termcolor import colored
from typing import List, Tuple, Dict, Set, Optional, Union
# 第一次不用四倍的普通挑战, 获得了, 45积分, 36棋玉, 54棋符
## 大概率是45阵营棋符, 45个人棋符, 30棋玉

# 计算自己到达目标个人棋符需要的体力次数, 考虑现有的体力次数, 不使用四倍
def cal_tili_num_to_target_qifu(
    qifu_num: int, # 现有个人棋符数量
    target_qifu: int, # 目标个人棋符数量
    tili_num: int = 35, # 现有体力次数
    qifu_per_time: int = 45, # 每次挑战获得的个人棋符数量
) -> int:
    need_tili_num = (target_qifu - qifu_num) / qifu_per_time
    if tili_num is not None:
        need_tili_num -= tili_num
    
    print(colored(f"想要达到棋符数量{target_qifu}, 不使用4倍的情况下, 需要体力次数: {round(need_tili_num, 2)}", "green"))

# 计算自己到达目标个人棋符需要的四倍数量, 考虑现有的四倍数量
def cal_core_num_to_target_qifu(
    qifu_num: int, # 现有个人棋符数量
    target_qifu: int, # 目标个人棋符数量
    qifu_per_time: int = 45, # 每次挑战获得的个人棋符数量
    sibei_num: Optional[int] = None, # 现有四倍数量
) -> int:
    need_si_bei_num = (target_qifu - qifu_num) / (qifu_per_time * 4)
    if sibei_num is not None:
        need_si_bei_num -= sibei_num
    
    print(colored(f"想要达到棋符数量{target_qifu}, 需要四倍数量: {round(need_si_bei_num, 2)}", "green"))

# 计算自己到达目标棋玉的距离需要的四倍数量, 考虑现有的四倍数量
def cal_core_num_to_target_qiyu(
    qiyu_num: int,  # 现有棋玉数量
    target_qiyu: int = 9000, # 目标棋玉数量
    qiyu_per_time: int = 30, # 每次挑战获得的棋玉数量
    sibei_num: Optional[int] = None, # 现有四倍数量
) -> int:
    need_si_bei_num = (target_qiyu - qiyu_num) / (qiyu_per_time * 4)
    if sibei_num is not None:
        need_si_bei_num -= sibei_num
    
    print(colored(f"想要达到棋玉数量{target_qiyu}, 需要四倍数量: {round(need_si_bei_num, 2)}", "green"))

if __name__ == "__main__":
    qifu_num = 3915 # 个人棋符数量
    target_qifu = 19322 # 目标个人棋符数量
    qifu_per_time = 71 # 每次挑战获得的个人棋符数量
    sibei_num = 3
    cal_tili_num_to_target_qifu(
        qifu_num=qifu_num,
        target_qifu=target_qifu,
        tili_num=2,
        qifu_per_time=qifu_per_time
    )

    cal_core_num_to_target_qifu(
        qifu_num=qifu_num,
        target_qifu=target_qifu,
        qifu_per_time=qifu_per_time,
        sibei_num=sibei_num
    )

    # qiyu_num = 1686 # 棋玉数量
    # target_qiyu = 9000 # 目标棋玉数量
    # qiyu_per_time = 30 # 每次挑战获得的棋玉数量
    # cal_core_num_to_target_qiyu(
    #     qiyu_num=qiyu_num,
    #     target_qiyu=target_qiyu,
    #     qiyu_per_time=qiyu_per_time,
    #     sibei_num=sibei_num
    # )