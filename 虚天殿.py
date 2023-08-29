"""
金色怪物: 50点积分, 50点纳元晶 (4倍: 200点积分, 200点纳元晶)
红色怪物: 75点积分, 60点纳元晶 (4倍: 300点积分, 240点纳元晶)
"""

from termcolor import colored

current_score = 6010
current_rank_score = 28310

target_score = 9000
target_rank_score = 31000

target_score_need_core_item_num = (target_score - current_score) / 240
target_rank_score_need_core_item_num = (target_rank_score - current_rank_score) / 300

print(colored(f"达到{target_score}纳元晶需要的四倍的数量: {target_score_need_core_item_num}", 'green'))
print(colored(f"达到{target_rank_score}点积分需要的四倍的数量: {target_rank_score_need_core_item_num}", 'green'))

# target_score_need_item_num = (target_score - current_score) / 60
# target_rank_score_need_item_num = (target_rank_score - current_rank_score) / 75

# print(colored(f"达到{target_score}积分在不使用四倍的情况下挑战的次数: {target_score_need_item_num}", 'green'))
# print(colored(f"达到{target_rank_score}点积分在不使用四倍的情况下挑战的次数: {target_rank_score_need_item_num}", 'green'))