# как числа фибоначи
n = int(input())
dp = [1, 1, 2]
now_step = 2
while now_step < n:
    dp.append(dp[now_step]+dp[now_step-1]+dp[now_step-2])
    now_step += 1


print(dp[n])
