"""
金色怪物: 50点积分, 50点纳元晶 (4倍: 200点积分, 200点纳元晶)
红色怪物: 75点积分, 60点纳元晶 (4倍: 300点积分, 240点纳元晶)
"""

# from termcolor import colored

current_score = 6010
current_rank_score = 33480

target_score = 9000
target_rank_score = 45460

target_score_need_core_item_num = (target_score - current_score) / 240
target_rank_score_need_core_item_num = (target_rank_score - current_rank_score) / 300

# print(colored(f"达到{target_score}纳元晶需要的四倍的数量: {target_score_need_core_item_num}", 'green'))
# print(colored(f"达到{target_rank_score}点积分需要的四倍的数量: {target_rank_score_need_core_item_num}", 'green'))

def XuTianDianChongBang(current_score, current_rank_score, target_score, target_rank_score):
    target_score_need_core_item_num = (target_score - current_score) / 240
    current_rank_score_after_buy_core_item = current_rank_score + target_score_need_core_item_num * 300

    target_rank_score_need_core_item_num = (target_rank_score - current_rank_score) / 300
    current_score_after_buy_core_item = current_score + target_rank_score_need_core_item_num * 240
    
    return {
        'target_score_need_core_item_num': target_score_need_core_item_num,
        'current_rank_score_after_buy_core_item': current_rank_score_after_buy_core_item,
        'target_rank_score_need_core_item_num': target_rank_score_need_core_item_num,
        'current_score_after_buy_core_item': current_score_after_buy_core_item
    }