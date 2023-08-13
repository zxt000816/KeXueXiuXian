from termcolor import colored
import math

# weiwang_next_level = 25600 # 升级职位需要的威望
# weiwang_now = 16545 # 当前威望
# gongxian_now = 1770 # 当前贡献
# target_item_gongxian = 7500 # 目标物品需要的贡献值
# zhenxie_gongxian = 300 # 宗门镇邪获得的威望

############## 次数 ##############
# num_qifu = 6 # 每天祈福次数
# num_task = 5 # 每天任务次数

def zong_men(
    weiwang_now, 
    gongxian_now, 
    weiwang_next_level, 
    target_item_gongxian, 
    zhenxie_gongxian=300,
    num_qifu=6,
    num_task=5,
):
    ############## 祈福 ##############
    qifu_weiwang = 180 # 每次祈福获得的威望
    qifu_gongxian = 300 # 每次祈福获得的贡献

    ############## 任务(七阶) ##############
    task_weiwang = 165 # 每次任务获得的威望
    task_gongxian = 20 # 每次任务获得的贡献

    everyday_qifu_weiwang = qifu_weiwang * num_qifu # 每天祈福获得的威望
    everyday_qifu_gongxian = qifu_gongxian * num_qifu # 每天祈福获得的贡献

    everyday_task_weiwang = task_weiwang * num_task # 每天任务获得的威望
    everyday_task_gongxian = task_gongxian * num_task # 每天任务获得的贡献

    everyday_weiwang = everyday_qifu_weiwang + everyday_task_weiwang # 每天获得的威望
    everyday_gongxian = everyday_qifu_gongxian + everyday_task_gongxian # 每天获得的贡献

    necc_days_to_next_level = (weiwang_next_level - weiwang_now) / everyday_weiwang
    necc_days_to_target_item = (target_item_gongxian - gongxian_now) / (everyday_gongxian + zhenxie_gongxian)

    print(colored('升级职位需要的天数：', 'green'), math.ceil(necc_days_to_next_level))
    print(colored('获得目标物品需要的天数：', 'green'), math.ceil(necc_days_to_target_item))

if __name__ == "__main__":
    weiwang_now = int(input('当前威望：'))
    weiwang_next_level = int(input('升级职位需要的威望：'))
    gongxian_now = int(input('当前贡献：'))
    target_item_gongxian = int(input('目标物品需要的贡献值：'))

    zong_men(
        weiwang_now=weiwang_now,
        gongxian_now=gongxian_now,
        weiwang_next_level=weiwang_next_level,
        target_item_gongxian=target_item_gongxian,
    )