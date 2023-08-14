# def cal_exp_of_gongfa(gongfa_level, gongfa_steps, gongfa_start_exp):
#     gongfa_level_exp = {3: 20, 4: 100}    
#     accum = gongfa_level_exp[gongfa_level]
#     exp_to_learn = gongfa_start_exp
    
#     for i in range(gongfa_steps):
#         exp_to_learn += (gongfa_start_exp + accum*(i+1))

#     return exp_to_learn

# import math
# def cal_time_of_gongfa(learn_rate_30_sec, gonfa_level, gongfa_steps, gongfa_start_exp):
#     learn_rate = learn_rate_30_sec * 2
#     exp_to_learn = cal_exp_of_gongfa(gonfa_level, gongfa_steps, gongfa_start_exp)
#     print('需要的经验：', exp_to_learn)
#     time_needed = exp_to_learn / learn_rate
#     print('需要的时间(分钟为单位)：', round(time_needed, 1))
#     time_needed = time_needed / 60
#     print('需要的时间(小时为单位)：', round(time_needed, 1))
#     time_needed = time_needed / 24
#     print('需要的时间(天为单位)：', round(time_needed, 1))

# if __name__ == "__main__":

#     learn_rate_30_sec = 148.8
#     cal_time_of_gongfa(learn_rate_30_sec, 3, 40-106, 2860)

# 废弃