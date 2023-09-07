from termcolor import colored

################# 灵石消费 #################
## 经验
jingyan_needed_lingshi = 100 + 150

## 宗门祈福
qifu_needed_lingshi = [0, 150, 200, 250, 300, 350]
# weiwang = [180, 180, 360, 360, 360, 360]
# gongxian = [300, 300, 600, 600, 600, 600]

def qifu_lingshi_expectation_by_times():
    for i in range(len(qifu_needed_lingshi)):
        every_day_cost = sum(qifu_needed_lingshi[:i+1])
        print("祈福", i+1, "次需要", every_day_cost, "灵石")

def qifu_lingshi(times):
    return sum(qifu_needed_lingshi[:times])

## 宗门任务
task_needed_lingshi = [0, 25, 50, 75, 100, 125, 150]

def task_lingshi(times):
    return sum(task_needed_lingshi[:times])

def task_lingshi_expectation_by_times():
    for i in range(len(task_needed_lingshi)):
        every_day_cost = sum(task_needed_lingshi[:i+1])
        print("刷新", i+1, "次任务需要", every_day_cost, "灵石")

## 神物园
# 19次加速
shenwuyuan_needed_lingshi = 756

################# 灵石获取 #################
zhenxie = 300 # 镇邪
mozu = 300 # 魔祖

zhouka = 300 # 周卡
yueka = 450 # 月卡
chongzhi = 60 # 充值

def get_lingshi():
    return sum([zhenxie, mozu, zhouka, yueka, chongzhi])

if __name__ == '__main__':
    qifu_num = 3
    task_num = 2

    everyday_cost_qifu_laman = qifu_lingshi(6)
    everyday_cost_qifu_economic = qifu_lingshi(qifu_num)
    everyday_cost_task = task_lingshi(task_num)

    everyday_cost = everyday_cost_qifu_economic + everyday_cost_task
    everyday_cost_laman = everyday_cost_qifu_laman + everyday_cost_task

    consider_exp_lingshi = True
    print(colored(f"拉满的话每天消耗{everyday_cost_laman}灵石 ({everyday_cost_qifu_laman}灵石祈福，{everyday_cost_task}灵石任务)", "green"))
    print(colored(f"经济祈福的话每天消耗{everyday_cost}灵石 ({everyday_cost_qifu_economic}灵石祈福，{everyday_cost_task}灵石任务)", "green"), '\n')
    if consider_exp_lingshi:
        print(colored(f"考虑经验并且拉满的话每天消耗{everyday_cost_laman + jingyan_needed_lingshi}灵石 ({everyday_cost_qifu_laman}灵石祈福，{everyday_cost_task}灵石任务，{jingyan_needed_lingshi}灵石经验)", "green"))
        print(colored(f"考虑经验并且经济祈福的话每天消耗{everyday_cost + jingyan_needed_lingshi}灵石 ({everyday_cost_qifu_economic}灵石祈福，{everyday_cost_task}灵石任务，{jingyan_needed_lingshi}灵石经验)", "green"), '\n')
    
    everyday_get = get_lingshi()
    print(colored(f"每天获得{everyday_get}灵石", "red"))
    print(colored(f"拉满每天能够省下来{everyday_get - everyday_cost_qifu_laman}灵石", "red"))
    print(colored(f"经济祈福每天能够省下来{everyday_get - everyday_cost_qifu_economic}灵石", "red"))