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
        'target_score_need_core_item_num': round(target_score_need_core_item_num, 2),
        'current_rank_score_after_buy_core_item': int(current_rank_score_after_buy_core_item),
        'target_rank_score_need_core_item_num': round(target_rank_score_need_core_item_num, 2),
        'current_score_after_buy_core_item': int(current_score_after_buy_core_item)
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
        'target_score_need_core_item_num': round(target_score_need_core_item_num, 2),
        'current_rank_score_after_buy_core_item': int(current_rank_score_after_buy_core_item),
        'target_rank_score_need_core_item_num': round(target_rank_score_need_core_item_num, 2),
        'current_score_after_buy_core_item': int(current_score_after_buy_core_item)
    }

def YunMengShiJian(current_score, current_rank_score, target_score, target_rank_score):
    """
    60点积分, 60点论剑玉 (4倍: 240点积分, 240点纳元晶)
    """
    
    target_score_need_core_item_num = (target_score - current_score) / 240
    current_rank_score_after_buy_core_item = current_rank_score + target_score_need_core_item_num * 240

    target_rank_score_need_core_item_num = (target_rank_score - current_rank_score) / 240
    current_score_after_buy_core_item = current_score + target_rank_score_need_core_item_num * 240
    
    return {
        'target_score_need_core_item_num': round(target_score_need_core_item_num, 2),
        'current_rank_score_after_buy_core_item': int(current_rank_score_after_buy_core_item),
        'target_rank_score_need_core_item_num': round(target_rank_score_need_core_item_num, 2),
        'current_score_after_buy_core_item': int(current_score_after_buy_core_item)
    }

def TianDiYIJu(current_qiyu, current_qifu, target_qiyu, target_qifu, qifu_per_time=90, qi_yu_per_time=30):
    """
    90点积分, 90点个人棋符, 30点棋玉 (不使用四倍)
    score: 棋玉数量
    rank_score: 棋符数量
    """
    
    qifu_sibei = qifu_per_time * 4
    qiyu_sibei = qi_yu_per_time * 4

    target_qiyu_need_core_item_num = (target_qiyu - current_qiyu) / qiyu_sibei
    current_qifu_after_buy_core_item = current_qifu + target_qiyu_need_core_item_num * qifu_sibei

    target_qifu_need_core_item_num = (target_qifu - current_qifu) / qifu_sibei
    current_qiyu_after_buy_core_item = current_qiyu + target_qifu_need_core_item_num * qiyu_sibei
    
    return {
        'target_score_need_core_item_num': round(target_qiyu_need_core_item_num, 2),
        'current_rank_score_after_buy_core_item': int(current_qifu_after_buy_core_item),
        'target_rank_score_need_core_item_num': round(target_qifu_need_core_item_num, 2),
        'current_score_after_buy_core_item': int(current_qiyu_after_buy_core_item)
    }

def chong_bang(event, current_score, current_rank_score, target_score, target_rank_score, qifu_per_time=90, qi_yu_per_time=30):
    if event == "虚天殿":
        return XuTianDian(current_score, current_rank_score, target_score, target_rank_score)
    elif event == "魔道入侵":
        return MoDaoRuQin(current_score, current_rank_score, target_score, target_rank_score)
    elif event == "云梦试剑":
        return YunMengShiJian(current_score, current_rank_score, target_score, target_rank_score)
    elif event == "天地弈局":
        return TianDiYIJu(current_score, current_rank_score, target_score, target_rank_score, qifu_per_time, qi_yu_per_time)