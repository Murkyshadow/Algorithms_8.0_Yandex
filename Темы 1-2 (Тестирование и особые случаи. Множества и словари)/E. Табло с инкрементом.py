# 0:30
cycle = {2:[20, 4], 0:[0, 1]}   # с какой цифры начинается:[сколько прибавляется за цикл, длина цикла]
LEN_CYCLE, ADD_PER_CYCLE = 1, 0
n, lost_time = map(int, input().split())
now_num = n
while lost_time and not now_num % 10 in cycle:
    now_num += now_num%10
    lost_time -= 1

if lost_time:
    num_cycles = lost_time // cycle[now_num%10][LEN_CYCLE]
    now_num += num_cycles * cycle[now_num%10][ADD_PER_CYCLE]
    lost_time = lost_time % cycle[now_num%10][LEN_CYCLE]
    for _ in range(lost_time):
        now_num += now_num % 10

print(now_num)
