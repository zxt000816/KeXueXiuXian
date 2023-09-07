from termcolor import colored
import math

task_info = {
    8: {
        'weiwang': 210,
        'gongxian': 40,
    },
    9: {
        'weiwang': 270,
        'gongxian': 60,
    }
}

qifu_weiwang = [180, 180, 360, 180, 180, 360]
qifu_gongxian = [300, 300, 600, 300, 300, 600]
zhenxie_gongxian=300

def zong_men(
    weiwang_now, 
    gongxian_now, 
    weiwang_next_level, 
    target_item_gongxian, 
    num_qifu=6,
    num_task=5,
    task_level=9
):
    ############## 祈福 ##############
    # qifu_weiwang = 180 # 每次祈福获得的威望
    # qifu_gongxian = 300 # 每次祈福获得的贡献

    task_weiwang = task_info[task_level]['weiwang'] # 每次任务获得的威望
    task_gongxian = task_info[task_level]['gongxian'] # 每次任务获得的贡献

    everyday_qifu_weiwang = sum(qifu_weiwang[:num_qifu]) # 每天祈福获得的威望
    everyday_qifu_gongxian = sum(qifu_gongxian[:num_qifu]) # 每天祈福获得的贡献

    everyday_task_weiwang = task_weiwang * num_task # 每天任务获得的威望
    everyday_task_gongxian = task_gongxian * num_task # 每天任务获得的贡献

    everyday_weiwang = everyday_qifu_weiwang + everyday_task_weiwang # 每天获得的威望
    everyday_gongxian = everyday_qifu_gongxian + everyday_task_gongxian # 每天获得的贡献

    necc_days_to_next_level = (weiwang_next_level - weiwang_now) / everyday_weiwang
    necc_days_to_target_item = (target_item_gongxian - gongxian_now) / (everyday_gongxian + zhenxie_gongxian)

    print(colored('升级职位需要的天数：', 'green'), round(necc_days_to_next_level, 2))
    print(colored('获得目标物品需要的天数：', 'green'), round(necc_days_to_target_item, 2))

if __name__ == "__main__":
    weiwang_now = 46995
    weiwang_next_level = 51200
    gongxian_now = 2830
    target_item_gongxian = 7500

    zong_men(
        weiwang_now=weiwang_now,
        gongxian_now=gongxian_now,
        weiwang_next_level=weiwang_next_level,
        target_item_gongxian=target_item_gongxian,
        num_qifu=3,
    )