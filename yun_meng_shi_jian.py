"""
60点积分, 60点论剑玉 (4倍: 240点积分, 240点纳元晶)
"""

from termcolor import colored

current_score = 3120
current_rank_score = 10240

target_score = 9000
target_rank_score = 13220

target_score_need_core_item_num = (target_score - current_score) / 240
target_rank_score_need_core_item_num = (target_rank_score - current_rank_score) / 240

print(colored(f"达到{target_score}论剑玉需要的四倍的数量: {target_score_need_core_item_num}", 'green'))
print(colored(f"达到{target_rank_score}点积分需要的四倍的数量: {target_rank_score_need_core_item_num}", 'green'))

# target_score_need_item_num = (target_score - current_score) / 60
# target_rank_score_need_item_num = (target_rank_score - current_rank_score) / 75

# print(colored(f"达到{target_score}积分在不使用四倍的情况下挑战的次数: {target_score_need_item_num}", 'green'))
# print(colored(f"达到{target_rank_score}点积分在不使用四倍的情况下挑战的次数: {target_rank_score_need_item_num}", 'green'))