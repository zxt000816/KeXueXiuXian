"""
金色怪物: 195点积分, 80点魔晶 (4倍: 780点积分, 320点魔晶)
"""

from termcolor import colored

current_score = 3960
current_rank_score = 9585

target_score = 9000
target_rank_score = 41437.5

target_score_need_core_item_num = (target_score - current_score) / 320
target_rank_score_need_core_item_num = (target_rank_score - current_rank_score) / 780

print(
    colored(
        f"达到{target_score}纳元晶需要的四倍的数量: {target_score_need_core_item_num}. 买到灵根后, 积分将达到: {current_rank_score + target_score_need_core_item_num * 780}", 
        'green'
    )
)
print(colored(f"达到{target_rank_score}点积分需要的四倍的数量: {target_rank_score_need_core_item_num}", 'green'))

# target_score_need_item_num = (target_score - current_score) / 60
# target_rank_score_need_item_num = (target_rank_score - current_rank_score) / 75

# print(colored(f"达到{target_score}积分在不使用四倍的情况下挑战的次数: {target_score_need_item_num}", 'green'))
# print(colored(f"达到{target_rank_score}点积分在不使用四倍的情况下挑战的次数: {target_rank_score_need_item_num}", 'green'))