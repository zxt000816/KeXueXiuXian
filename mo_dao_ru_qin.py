def XuTianDian(current_score, current_rank_score, target_score, target_rank_score):
    """
    金色怪物: 50点积分, 50点纳元晶 (4倍: 200点积分, 200点纳元晶)
    红色怪物: 75点积分, 60点纳元晶 (4倍: 300点积分, 240点纳元晶)
    """

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

def MoDaoRuQin(current_score, current_rank_score, target_score, target_rank_score):
    """
    金色怪物: 195点积分, 80点魔晶 (4倍: 780点积分, 320点魔晶)
    """

    target_score_need_core_item_num = (target_score - current_score) / 320
    current_rank_score_after_buy_core_item = current_rank_score + target_score_need_core_item_num * 780

    target_rank_score_need_core_item_num = (target_rank_score - current_rank_score) / 780
    current_score_after_buy_core_item = current_score + target_rank_score_need_core_item_num * 320
    
    return {
        'target_score_need_core_item_num': target_score_need_core_item_num,
        'current_rank_score_after_buy_core_item': current_rank_score_after_buy_core_item,
        'target_rank_score_need_core_item_num': target_rank_score_need_core_item_num,
        'current_score_after_buy_core_item': current_score_after_buy_core_item
    }
