# Дан массив А - кол-во переработок каждого сотрудника
# Необходимо для i-ного сотрудника вычислить сколько перед ним (j < i) сотрудников с j+Aj > i и умножить это число на Аi
# Просто для каждого сотрудника рассчитаем сколько сотрудников он обгонит (его индекс + переработка > i).
# К примеру, i сотрудник будет больше от i+1 до i+Ai (кроме случая, когда Ai = 0 тк больше самого себя он не будет)
# То есть идем по сотрудникам (их переработкам) и тянем за собой счетчик с кол-вом с большей суммой (>j+Aj),
# перешли к новому сотруднику прибавили 1 рассчитали до какого индекса он будет больше (до i+Ai не включительно),
# и идем дальше, если встречаем, что кто-то закончился, то вычитаем 1

def solution(n, recycling):
    hard_worker_leave = [0] * n  # hard worker - работяга (кол-во людей с большим j+Aj), которые перестали быть работягами для i-ного
    now_num_hard_worker = 0
    ans = 0
    for i, r in enumerate(recycling):
        now_num_hard_worker -= hard_worker_leave[i]
        if r != 0:
            ans += now_num_hard_worker*r
            now_num_hard_worker += 1
            if i+r < n:
                hard_worker_leave[i+r] += 1
    return ans

n = int(input())
recycling = list(map(int, input().split()))
print(solution(n, recycling))

# Для стресс тестирования:
# def solution_brute_force(n, recycling):
#     ans = 0
#     for i in range(n):
#         counter = 0
#         for j, r in enumerate(recycling[:i]):
#             if j+r > i:
#                 counter += 1
#         ans += counter*recycling[i]
#     return ans
#
# from random import randint
# def generator():
#     n = randint(1000000,1000000)
#     a = [randint(0,n) for _ in range(n)]
#     return n, a
# from time import time
# while 1:
#     n, recycling = generator()
#     t = time()
#     ans_my = solution(n, recycling)
#     print(round(time() - t, 4))
#     ans_slow = solution_brute_force(n, recycling)
#     if ans_my != ans_slow:
#         print(ans_my, ans_slow)
#         print(n)
#         print(*recycling)
#         break
#     else:
#         print(ans_my, ans_slow)

