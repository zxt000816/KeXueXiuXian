primary = 1350
first_time = 2630 - primary
second_time = 4090 - 2630
third_time = 5550 - 4090
fourth_time = 7090 - 5550

print("First time: " + str(first_time))
print("Second time: " + str(second_time))
print("Third time: " + str(third_time))
print("Fourth time: " + str(fourth_time))

(first_time + second_time + third_time + fourth_time) / 4

max([first_time, second_time, third_time, fourth_time])

min([first_time, second_time, third_time, fourth_time])