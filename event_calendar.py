import pandas as pd
import numpy as np
from datetime import datetime
import re

known_events = [
    {'活动': '魔道入侵', '跨服': 1, '开始': '2023-10-30', '结束': '2023-10-30'},
    {'活动': '魔道入侵', '跨服': 2, '开始': '2023-10-31', '结束': '2023-10-31'},
    {'活动': '炼体法相', '跨服': 1, '开始': '2023-10-30', '结束': '2023-10-30'},
    {'活动': '炼体法相', '跨服': 4, '开始': '2023-10-31', '结束': '2023-11-01'},
    {'活动': '虚天殿', '跨服': 2, '开始': '2023-11-01', '结束': '2023-11-02'},
    {'活动': '社团洗灵', '跨服': 2, '开始': '2023-11-02', '结束': '2023-11-03'},
    {'活动': '兽渊探秘', '跨服': 4, '开始': '2023-11-03', '结束': '2023-11-04'},
    {'活动': '瑶池花会', '跨服': 2, '开始': '2023-11-04', '结束': '2023-11-05'},
    {'活动': '天地弈局', '跨服': 1, '开始': '2023-11-05', '结束': '2023-11-05'},
    {'活动': '天地弈局', '跨服': 4, '开始': '2023-11-06', '结束': '2023-11-06'},
    {'活动': '灵宠竞武', '跨服': 2, '开始': '2023-11-06', '结束': '2023-11-07'},
    {'活动': '社团大比', '跨服': 8, '开始': '2023-11-07', '结束': '2023-11-07'},
    {'活动': '云梦试剑', '跨服': 4, '开始': '2023-11-08', '结束': '2023-11-08'},
    {'活动': '炼体法相', '跨服': 2, '开始': '2023-11-08', '结束': '2023-11-09'},
    {'活动': '魔道入侵', '跨服': 1, '开始': '2023-11-09', '结束': '2023-11-09'},
    {'活动': '魔道入侵', '跨服': 16, '开始': '2023-11-10', '结束': '2023-11-10'},
    {'活动': '丹道问鼎', '跨服': 1, '开始': '2023-11-10', '结束': '2023-11-10'},
    {'活动': '丹道问鼎', '跨服': 16, '开始': '2023-11-11', '结束': '2023-11-12'},
    {'活动': '虚天殿', '跨服': 2, '开始': '2023-11-12', '结束': '2023-11-13'},
    {'活动': '社团花会', '跨服': 4, '开始': '2023-11-13', '结束': '2023-11-14'},
    {'活动': '兽渊探秘', '跨服': 2, '开始': '2023-11-14', '结束': '2023-11-15'},
    {'活动': '仙盟争霸', '跨服': 8, '开始': '2023-11-16', '结束': '2023-11-17'},
    {'活动': '洗灵证武', '跨服': 1, '开始': '2023-11-16', '结束': '2023-11-16'},
    {'活动': '洗灵证武', '跨服': 4, '开始': '2023-11-17', '结束': '2023-11-18'},
    {'活动': '升仙会', '跨服': 8, '开始': '2023-11-18', '结束': '2023-11-18'},
    {'活动': '云梦试剑', '跨服': 4, '开始': '2023-11-19', '结束': '2023-11-19'},
    {'活动': '社团灵宠', '跨服': 2, '开始': '2023-11-19', '结束': '2023-11-20'},
    {'活动': '魔道入侵', '跨服': 1, '开始': '2023-11-20', '结束': '2023-11-20'},
    {'活动': '魔道入侵', '跨服': 2, '开始': '2023-11-21', '结束': '2023-11-21'},
    {'活动': '炼体法相', '跨服': 1, '开始': '2023-11-22', '结束': '2023-11-22'},
    {'活动': '炼体法相', '跨服': 8, '开始': '2023-11-23', '结束': '2023-11-24'},
    {'活动': '天地弈局', '跨服': 1, '开始': '2023-11-22', '结束': '2023-11-22'},
    {'活动': '天地弈局', '跨服': 4, '开始': '2023-11-23', '结束': '2023-11-23'},
    {'活动': '虚天殿', '跨服': 8, '开始': '2023-11-24', '结束': '2023-11-26'},
    {'活动': '瑶池花会', '跨服': 1, '开始': '2023-11-25', '结束': '2023-11-25'},
    {'活动': '瑶池花会', '跨服': 4, '开始': '2023-11-26', '结束': '2023-11-27'},
    {'活动': '兽渊探秘', '跨服': 2, '开始': '2023-11-27', '结束': '2023-11-28'},
    {'活动': '丹道问鼎', '跨服': 2, '开始': '2023-11-28', '结束': '2023-11-29'},
    {'活动': '社团大比', '跨服': 8, '开始': '2023-11-29', '结束': '2023-11-29'},
    {'活动': '云梦试剑', '跨服': 2, '开始': '2023-11-30', '结束': '2023-11-30'},
    {'活动': '洗灵证武', '跨服': 2, '开始': '2023-11-30', '结束': '2023-12-01'},
    {'活动': '魔道入侵', '跨服': 1, '开始': '2023-12-01', '结束': '2023-12-01'},
    {'活动': '魔道入侵', '跨服': 4, '开始': '2023-12-02', '结束': '2023-12-03'},
    {'活动': '灵宠竞武', '跨服': 1, '开始': '2023-12-02', '结束': '2023-12-02'},
    {'活动': '灵宠竞武', '跨服': 4, '开始': '2023-12-03', '结束': '2023-12-04'},
    {'活动': '升仙会', '跨服': 8, '开始': '2023-12-03', '结束': '2023-12-03'},
    {'活动': '仙盟争霸', '跨服': 8, '开始': '2023-12-04', '结束': '2023-12-05'},
    {'活动': '玄武相竞舟', '跨服': 4, '开始': '2023-12-04', '结束': '2023-12-06'},
    {'活动': '虚天殿', '跨服': 2, '开始': '2023-12-06', '结束': '2023-12-07'},
    {'活动': '瑶池花会', '跨服': 1, '开始': '2023-12-06', '结束': '2023-12-06'},
    {'活动': '瑶池花会', '跨服': 16, '开始': '2023-12-07', '结束': '2023-12-08'},
    {'活动': '兽渊探秘', '跨服': 16, '开始': '2023-12-08', '结束': '2023-12-09'},
    {'活动': '社团炼体', '跨服': 4, '开始': '2023-12-09', '结束': '2023-12-10'},
    {'活动': '社团大比', '跨服': 8, '开始': '2023-12-10', '结束': '2023-12-10'},
    {'活动': '云梦试剑', '跨服': 4, '开始': '2023-12-11', '结束': '2023-12-11'},
    {'活动': '灵宠竞武', '跨服': 2, '开始': '2023-12-11', '结束': '2023-12-12'},
    {'活动': '魔道入侵', '跨服': 1, '开始': '2023-12-12', '结束': '2023-12-12'},
    {'活动': '魔道入侵', '跨服': 2, '开始': '2023-12-13', '结束': '2023-12-13'},
    {'活动': '社团丹道', '跨服': 4, '开始': '2023-12-13', '结束': '2023-12-14'},
    {'活动': '虚天殿', '跨服': 2, '开始': '2023-12-14', '结束': '2023-12-15'},
    {'活动': '炼骨成圣', '跨服': 0, '开始': '2023-12-14', '结束': '2023-12-18'},
    {'活动': '洗灵证武', '跨服': 1, '开始': '2023-12-15', '结束': '2023-12-15'},
    {'活动': '洗灵证武', '跨服': 8, '开始': '2023-12-16', '结束': '2023-12-17'},
    {'活动': '升仙会', '跨服': 8, '开始': '2023-12-16', '结束': '2023-12-16'},
    {'活动': '兽渊探秘', '跨服': 2, '开始': '2023-12-17', '结束': '2023-12-18'},
    {'活动': '炼体法相', '跨服': 1, '开始': '2023-12-18', '结束': '2023-12-18'},
    {'活动': '炼体法相', '跨服': 4, '开始': '2023-12-19', '结束': '2023-12-20'},
    {'活动': '天地弈局', '跨服': 1, '开始': '2023-12-19', '结束': '2023-12-19'},
    {'活动': '天地弈局', '跨服': 8, '开始': '2023-12-20', '结束': '2023-12-21'},
    {'活动': '瑶池花会', '跨服': 2, '开始': '2023-12-21', '结束': '2023-12-22'},
    {'活动': '封魔正法(五日连充)', '跨服': 0, '开始': '2023-12-21', '结束': '2023-12-27'},
    {'活动': '社团大比', '跨服': 8, '开始': '2023-12-22', '结束': '2023-12-22'},
    {'活动': '魔道入侵', '跨服': 1, '开始': '2023-12-23', '结束': '2023-12-23'},
    {'活动': '魔道入侵', '跨服': 4, '开始': '2023-12-24', '结束': '2023-12-24'},
    {'活动': '丹道问鼎', '跨服': 1, '开始': '2023-12-23', '结束': '2023-12-23'},
    {'活动': '丹道问鼎', '跨服': 4, '开始': '2023-12-24', '结束': '2023-12-25'},
    {'活动': '兽渊探秘', '跨服': 2, '开始': '2023-12-25', '结束': '2023-12-26'},
    {'活动': '仙戏灵龙', '跨服': 4, '开始': '2023-12-25', '结束': '2023-12-27'},
    {'活动': '灵宠竞武', '跨服': 1, '开始': '2023-12-26', '结束': '2023-12-26'},
    {'活动': '云梦试剑', '跨服': 2, '开始': '2023-12-27', '结束': '2023-12-27'},
    {'活动': '灵宠竞武', '跨服': 16, '开始': '2023-12-27', '结束': '2023-12-28'},
    {'活动': '虚天殿', '跨服': 16, '开始': '2023-12-28', '结束': '2023-12-31'},
    {'活动': '百炼金丹', '跨服': 0, '开始': '2023-12-28', '结束': '2023-12-31'},
    {'活动': '炼体秘藏_万毒混元身', '跨服': 0, '开始': '2023-12-28', '结束': '2023-12-29'},
    {'活动': '洗灵证武', '跨服': 2, '开始': '2023-12-29', '结束': '2023-12-30'},
    {'活动': '神阵鉴宝_涅槃珠', '跨服': 0, '开始': '2023-12-30', '结束': '2023-12-31'},
    {'活动': '炼体法相', '跨服': 2, '开始': '2023-12-31', '结束': '2024-01-01'},
    {'活动': '仙盟争霸', '跨服': 8, '开始': '2024-01-01', '结束': '2024-01-02'},
    {'活动': '社团花会', '跨服': 4, '开始': '2024-01-02', '结束': '2024-01-03'},
    {'活动': '升仙会', '跨服': 8, '开始': '2024-01-03', '结束': '2024-01-03'},
    {'活动': '魔道入侵', '跨服': 1, '开始': '2024-01-04', '结束': '2024-01-04'},
    {'活动': '魔道入侵', '跨服': 2, '开始': '2024-01-05', '结束': '2024-01-05'},
    {'活动': '丹道问鼎', '跨服': 1, '开始': '2024-01-04', '结束': '2024-01-04'},
    {'活动': '炼体秘藏_须弥神象功', '跨服': 0, '开始': '2024-01-04', '结束': '2024-01-05'},
    {'活动': '心花似悦', '跨服': 0, '开始': '2024-01-04', '结束': '2024-01-07'},
    {'活动': '丹道问鼎', '跨服': 8, '开始': '2024-01-05', '结束': '2024-01-06'},
    {'活动': '灵装化道', '跨服': 1, '开始': '2024-01-05', '结束': '2024-01-06'},
    {'活动': '兽渊探秘', '跨服': 4, '开始': '2024-01-06', '结束': '2024-01-07'},
    {'活动': '灵宠竞武', '跨服': 1, '开始': '2024-01-07', '结束': '2024-01-07'},
    {'活动': '灵宠竞武', '跨服': 4, '开始': '2024-01-08', '结束': '2024-01-09'},
    {'活动': '云梦试剑', '跨服': 8, '开始': '2024-01-08', '结束': '2024-01-08'},
    {'活动': '灵宠竞武', '跨服': 4, '开始': '2024-01-08', '结束': '2024-01-09'},
    {'活动': '虚天殿', '跨服': 2, '开始': '2024-01-09', '结束': '2024-01-10'},
    {'活动': '社团洗灵', '跨服': 8, '开始': '2024-01-10', '结束': '2024-01-11'},
    {'活动': '天地弈局', '跨服': 1, '开始': '2024-01-11', '结束': '2024-01-11'},
    {'活动': '天河仙会', '跨服': 4, '开始': '2024-01-11', '结束': '2024-01-13'},
    {'活动': '御灵有术', '跨服': 0, '开始': '2024-01-11', '结束': '2024-01-14'},
    {'活动': '天地弈局', '跨服': 4, '开始': '2024-01-12', '结束': '2024-01-12'},
    {'活动': '灵装化道', '跨服': 2, '开始': '2024-01-12', '结束': '2024-01-13'},
    {'活动': '社团大比', '跨服': 8, '开始': '2024-01-13', '结束': '2024-01-13'},
    {'活动': '神阵鉴宝_梵花宝篮', '跨服': 0, '开始': '2024-01-13', '结束': '2024-01-14'},
    {'活动': '云梦试剑', '跨服': 2, '开始': '2024-01-14', '结束': '2024-01-14'},
    {'活动': '瑶池花会', '跨服': 2, '开始': '2024-01-14', '结束': '2024-01-15'},
    {'活动': '魔道入侵', '跨服': 1, '开始': '2024-01-15', '结束': '2024-01-15'},
    {'活动': '魔道入侵', '跨服': 4, '开始': '2024-01-16', '结束': '2024-01-16'},
    {'活动': '丹道问鼎', '跨服': 2, '开始': '2024-01-16', '结束': '2024-01-17'},
    {'活动': '兽渊探秘', '跨服': 2, '开始': '2024-01-17', '结束': '2024-01-18'},
    {'活动': '炼体法相', '跨服': 1, '开始': '2024-01-18', '结束': '2024-01-18'},
    # {'活动': '炼体秘藏_伏火化灵诀', '跨服': 0, '开始': '2024-01-18', '结束': '2024-01-19'},
    # {'活动': '积麟渡厄(五日连充)', '跨服': 0, '开始': '2024-01-18', '结束': '2024-01-24'},
    {'活动': '炼体法相', '跨服': 16, '开始': '2024-01-19', '结束': '2024-01-20'},
    {'活动': '升仙会', '跨服': 8, '开始': '2024-01-19', '结束': '2024-01-19'},
    {'活动': '天地弈局', '跨服': 1, '开始': '2024-01-20', '结束': '2024-01-20'},
    # {'活动': '神阵鉴宝_万仞盘', '跨服': 0, '开始': '2024-01-20', '结束': '2024-01-21'},
    {'活动': '天地弈局', '跨服': 16, '开始': '2024-01-21', '结束': '2024-01-22'},
    {'活动': '灵装化道', '跨服': 1, '开始': '2024-01-21', '结束': '2024-01-21'},
    {'活动': '灵装化道', '跨服': 4, '开始': '2024-01-22', '结束': '2024-01-23'},
    {'活动': '仙戏灵鹿', '跨服': 4, '开始': '2024-01-22', '结束': '2024-01-24'},
    {'活动': '虚天殿', '跨服': 4, '开始': '2024-01-23', '结束': '2024-01-24'},
    {'活动': '社团灵宠', '跨服': 4, '开始': '2024-01-24', '结束': '2024-01-25'},
    {'活动': '社团大比', '跨服': 8, '开始': '2024-01-25', '结束': '2024-01-25'},
    {'活动': '巧夺天装', '跨服': 0, '开始': '2024-01-25', '结束': '2024-01-28'},
    {'活动': '灵缈探宝', '跨服': 0, '开始': '2024-01-25', '结束': '2024-01-26'},
    {'活动': '魔道入侵', '跨服': 1, '开始': '2024-01-26', '结束': '2024-01-26'},
    {'活动': '魔道入侵', '跨服': 8, '开始': '2024-01-27', '结束': '2024-01-27'},
    {'活动': '洗灵证武', '跨服': 1, '开始': '2024-01-26', '结束': '2024-01-26'},
    {'活动': '洗灵证武', '跨服': 4, '开始': '2024-01-27', '结束': '2024-01-28'},
    {'活动': '神阵鉴宝_万森轮盘', '跨服': 0, '开始': '2024-02-10', '结束': '2024-02-11'},
    {'活动': '兽渊探秘', '跨服': 4, '开始': '2024-01-28', '结束': '2024-01-29'},
    {'活动': '瑶池花会', '跨服': 1, '开始': '2024-01-29', '结束': '2024-01-29'},
    {'活动': '瑶池花会', '跨服': 8, '开始': '2024-01-30', '结束': '2024-01-31'},
    {'活动': '云梦试剑', '跨服': 2, '开始': '2024-01-30', '结束': '2024-01-30'},
    {'活动': '仙盟争霸', '跨服': 8, '开始': '2024-01-31', '结束': '2024-02-01'},
    {'活动': '炼体法相', '跨服': 2, '开始': '2024-02-01', '结束': '2024-02-02'},
    {'活动': '炼骨成圣', '跨服': 0, '开始': '2024-02-15', '结束': '2024-02-18'},
    {'活动': '虚天殿', '跨服': 4, '开始': '2024-02-02', '结束': '2024-02-03'},
    {'活动': '社团灵装', '跨服': 4, '开始': '2024-02-03', '结束': '2024-02-04'},
    {'活动': '神阵鉴宝_涅槃珠', '跨服': 0, '开始': '2024-02-17', '结束': '2024-02-18'},
    {'活动': '升仙会', '跨服': 8, '开始': '2024-02-04', '结束': '2024-02-04'},
    {'活动': '魔道入侵', '跨服': 1, '开始': '2024-02-05', '结束': '2024-02-05'},
    {'活动': '魔道入侵', '跨服': 4, '开始': '2024-02-06', '结束': '2024-02-06'},
    {'活动': '丹道问鼎', '跨服': 1, '开始': '2024-02-05', '结束': '2024-02-05'},
    {'活动': '丹道问鼎', '跨服': 4, '开始': '2024-02-06', '结束': '2024-02-07'},
    {'活动': '兽渊探秘', '跨服': 16, '开始': '2024-02-07', '结束': '2024-02-08'},
    {'活动': '洗灵证武', '跨服': 1, '开始': '2024-02-08', '结束': '2024-02-08'},
    {'活动': '洗灵证武', '跨服': 16, '开始': '2024-02-09', '结束': '2024-02-10'},
    {'活动': '云梦试剑', '跨服': 4, '开始': '2024-02-09', '结束': '2024-02-09'},
    {'活动': '天地弈局', '跨服': 1, '开始': '2024-02-10', '结束': '2024-02-10'},
    {'活动': '天地弈局', '跨服': 4, '开始': '2024-02-11', '结束': '2024-02-11'},
    {'活动': '灵宠竞武', '跨服': 2, '开始': '2024-02-11', '结束': '2024-02-12'},
    {'活动': '虚天殿', '跨服': 4, '开始': '2024-02-12', '结束': '2024-02-13'},
    {'活动': '社团炼体', '跨服': 4, '开始': '2024-02-13', '结束': '2024-02-14'},
    {'活动': '社团大比', '跨服': 8, '开始': '2024-02-14', '结束': '2024-02-14'},
    {'活动': '魔道入侵', '跨服': 1, '开始': '2024-02-15', '结束': '2024-02-15'},
    {'活动': '瑶池花会', '跨服': 1, '开始': '2024-02-15', '结束': '2024-02-15'},
    {'活动': '兽渊探秘', '跨服': 4, '开始': '2024-02-17', '结束': '2024-02-18'},
    {'活动': '灵装化道', '跨服': 1, '开始': '2024-02-18', '结束': '2024-02-18'},
    {'活动': '灵装化道', '跨服': 8, '开始': '2024-02-19', '结束': '2024-02-20'},
    {'活动': '云梦试剑', '跨服': 2, '开始': '2024-02-19', '结束': '2024-02-19'},
    {'活动': '云梦试剑', '跨服': 4, '开始': '2024-02-20', '结束': '2024-02-20'},
    {'活动': '仙盟争霸', '跨服': 8, '开始': '2024-02-21', '结束': '2024-02-22'},
    {'活动': '灵宠竞武', '跨服': 1, '开始': '2024-02-21', '结束': '2024-02-21'},
    {'活动': '灵宠竞武', '跨服': 4, '开始': '2024-02-22', '结束': '2024-02-23'},
    {'活动': '百炼金丹', '跨服': 0, '开始': '2024-02-22', '结束': '2024-02-25'},
    {'活动': '天河仙会', '跨服': 4, '开始': '2024-02-22', '结束': '2024-02-24'},
    {'活动': '虚天殿', '跨服': 4, '开始': '2024-02-23', '结束': '2024-02-24'},
    {'活动': '社团洗灵', '跨服': 4, '开始': '2024-02-24', '结束': '2024-02-25'},
    {'活动': '社团大比', '跨服': 16, '开始': '2024-02-25', '结束': '2024-02-25'},
    {'活动': '魔道入侵', '跨服': 1, '开始': '2024-02-26', '结束': '2024-02-26'},
    {'活动': '魔道入侵', '跨服': 16, '开始': '2024-02-26', '结束': '2024-02-27'},
    {'活动': '丹道问鼎', '跨服': 1, '开始': '2024-02-26', '结束': '2024-02-26'},
    {'活动': '丹道问鼎', '跨服': 16, '开始': '2024-02-27', '结束': '2024-02-28'},
    {'活动': '兽渊探秘', '跨服': 2, '开始': '2024-02-28', '结束': '2024-02-29'},
    {'活动': '炼体法相', '跨服': 2, '开始': '2024-02-29', '结束': '2024-03-01'},
    {'活动': '虚天殿', '跨服': 4, '开始': '2024-03-01', '结束': '2024-03-02'},
    {'活动': '社团花会', '跨服': 4, '开始': '2024-03-02', '结束': '2024-03-03'},
    {'活动': '天地弈局', '跨服': 1, '开始': '2024-03-03', '结束': '2024-03-03'},
]

uncertain_events = [
    {'活动': '凤相竞舟', '跨服': 4, '开始': '2023-11-06', '结束': '2023-11-08'},
    {'活动': '仙园游宴(山海套装)', '跨服': 4, '开始': '2023-11-20', '结束': '2023-11-22'},
    {'活动': '仙园游宴(万妖灵塔)', '跨服': 4, '开始': '2023-12-18', '结束': '2023-12-21'},
    {'活动': '虎相竞舟', '跨服': 8, '开始': '2024-01-01', '结束': '2024-01-03'},
    {'活动': '奇技诛魔_风后奇门', '跨服': 4, '开始': '2024-01-08', '结束': '2024-01-10'},
    {'活动': '仙园游宴(天海套装)', '跨服': 4, '开始': '2024-01-15', '结束': '2024-01-17'},
    {'活动': '麒麟相竞舟', '跨服': 8, '开始': '2024-02-12', '结束': '2024-02-14'},
    {'活动': '奇技诛魔_通神箓', '跨服': 4, '开始': '2024-02-19', '结束': '2024-02-21'},
    {'活动': '仙宴游宴(风吟套装)', '跨服': 4, '开始': '2024-02-26', '结束': '2024-02-28'},
]

known_events = known_events + uncertain_events

data = pd.DataFrame(known_events)
today = datetime.today().replace(hour=0, minute=0, second=0, microsecond=0)

offset1 = pd.Timedelta(days=11) # 服务器之间的时间差
offset2 = pd.Timedelta(days=8) # 为了16跨匹配产生的时间差

data['开始'] = pd.to_datetime(data['开始'])
data['结束'] = pd.to_datetime(data['结束'])

data = data.sort_values(by=['开始'])

# 给开始和结束时间加上8天
data['开始'] = data['开始'] + offset1 + offset2
data['结束'] = data['结束'] + offset1 + offset2

data['剩余天数(开始)'] = (data['开始'] - today).dt.days
data['剩余天数(结束)'] = (data['结束'] - today).dt.days

event_names = []
for _tuple in data[['活动', '跨服']].itertuples():
    event_name, num_of_servers = _tuple[1], _tuple[2]
    if num_of_servers == 1:
        event_names.append(f"{event_name}预赛")
    elif num_of_servers == 0:
        event_names.append(event_name)
    else:
        event_names.append(f"{event_name}跨服[{num_of_servers}]")

data['活动'] = event_names
data['剩余天数(开始)'] = data['剩余天数(开始)'].apply(lambda x: f"{x}天")
data['剩余天数(结束)'] = data['剩余天数(结束)'].apply(lambda x: f"{x}天")
data = data[['活动', '剩余天数(开始)', '开始', '结束', '剩余天数(结束)']]

# filter out events that are already over
data = data[data['剩余天数(结束)'].apply(lambda x: x.split('天')[0]).astype(int) >= 0]
data = data[data['剩余天数(开始)'].apply(lambda x: x.split('天')[0]).astype(int) >= 0]

event_col = f"活动 (当前: {datetime.strftime(today, '%Y-%m-%d')})"

data = data.rename(columns={'活动': event_col})

other_events = [
    '凤相竞舟跨服[4]', '玄武相竞舟跨服[4]', '仙园游宴(万妖灵塔)跨服[4]', 
    '仙园游宴(山海套装)跨服[4]', '仙戏灵龙跨服[4]', '虎相竞舟跨服[8]', 
    '仙园游宴(天海套装)跨服[4]', '仙戏灵鹿跨服[4]', '麒麟相竞舟跨服[8]', 
    '奇技诛魔_风后奇门跨服[4]', '奇技诛魔_通神箓跨服[4]', '仙宴游宴(风吟套装)跨服[4]'
] 
lei_chong_events = ['炼骨成圣', '仙戏灵龙', '封魔正法(五日连充)', '百炼金丹', '心花似悦', '御灵有术', '积麟渡厄(五日连充)', 
                    '巧夺天装']
chou_jiang_events = ['炼体秘藏', '天河仙会', '神阵鉴宝', '灵缈探宝']

def style_important_event(event):
    
    if '社团' in event:
        return 'color: green;' + 'font-weight: bold;'
    elif event in other_events:
        return 'color: blue;'  + 'font-weight: bold;'
    elif event in lei_chong_events:
        return 'color: purple;'  + 'font-weight: bold;'
    # elif event in chou_jiang_events:
    elif re.search("|".join(chou_jiang_events), event) is not None:
        return 'color: brown;' + 'font-weight: bold;'
    elif '[8]' in event or '[16]' in event:
        return 'color: red;' + 'font-weight: bold;'
    else:
        return ''

number_to_chinese = {
    1: '周一',
    2: '周二',
    3: '周三',
    4: '周四',
    5: '周五',
    6: '周六',
    7: '周日',
}

data['开始'] = data['开始'].apply(lambda x: datetime.strftime(x, '%Y-%m-%d') + f" ({number_to_chinese.get(x.weekday() + 1)})")
data['结束'] = data['结束'].apply(lambda x: datetime.strftime(x, '%Y-%m-%d') + f" ({number_to_chinese.get(x.weekday() + 1)})")

data.index = np.arange(1, len(data) + 1)

data.style.applymap(style_important_event, subset=[event_col])
# data.style.applymap(style_important_event, subset=[event_col]).to_html('event_calendar.html', escape=False, index=False)