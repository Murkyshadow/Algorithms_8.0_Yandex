# 18:52 - 19:10 19:45-20:15
# сначала идем окном по элементам быстро рассчитывая защиту каждой башни
# далее выбираем max(предыдущая защита, либо защита текущей башни + защита, которая была в начале этой башни)
# так же для каждой выбранной защиты мы запоминаем, как мы пришли к такой защите (запоминаем индексы начал башен)
import copy

num_column, weight_tower = map(int, input().split())
weights = list(map(int, input().split()))

defence_towers = []
min_weight = min(weights[:weight_tower])
now_defence = sum(weights[:weight_tower]) * min_weight
defence_towers.append(now_defence)
for i in range(weight_tower, num_column):   # рассчитываем защиту каждой башни
    now_defence //= min_weight
    now_defence -= weights[i-weight_tower]
    now_defence += weights[i]
    min_weight = min(weights[i-weight_tower+1:i+1])
    now_defence *= min_weight
    defence_towers.append(now_defence)

dp = [0] * (num_column+1)
paths = [[] for _ in range(num_column+1)]

for i in range(weight_tower, num_column+1): # выбираем лучшую защиту
    if dp[i-1] > dp[i-weight_tower]+defence_towers[i-weight_tower]:
        dp[i] = dp[i-1]
        paths[i] = copy.deepcopy(paths[i-1])
    else:
        dp[i] = dp[i-weight_tower]+defence_towers[i-weight_tower]
        paths[i] = paths[i-weight_tower]+[i-weight_tower+1]

ind = max(enumerate(dp), key=lambda x: x[1])[0]
print(len(paths[ind]))
print(*paths[ind])