# 00:13 - 1:32  1:49-2:13 3:08-3:21 = 79+24+13 = 116
# одномерное dp
# Делаем массив длинной 199, где индекс - это длина, а занчение - минимальная стоимость этой длины
# 199 - тк мб случай, что мы нашли 99 по маленькой цене, а нам надо 100 и мы можем очень дешево купить еще 99м (оптом) + 1 - нулевая длина (ну, или брать удвоенное значение необходимой длины)
# Идем по ячейкам с право на лево и для каждой ячейки перебираем всевозможные длины
# (и их стоимость соответственно) и выбираем наименьшую стоимость из текущей или
# полученной и это делаем для каждого магазина
import math

def get_cost(buy_len, normal_cost, cost_with_discount, wholesale_len):
    return buy_len * (cost_with_discount if buy_len >= wholesale_len else normal_cost)

dp_costs = [math.inf for _ in range(199)]   # cost - минимальная цена за данную длину, а inf - значит, что еще не получали эту длину;
paths = [[] for _ in range(199)]   # [ [(num_shop, len), (num_shop, len), ...], [...], ...] для каждой длины свой путь получения
dp_costs[0] = 0                    # нулевую длину получаем за 0 бурлей

n, need_len = map(int, input().split())
sum_len = 0
for ind_shop in range(n):
    normal_cost, wholesale_len, cost_with_discount, max_len = map(int, input().split())
    sum_len += max_len
    for i in range(len(dp_costs)-1, 0, -1):   # с права на лево, чтобы не наткнуться на свои же значения и не посчитать длину дважды
        for buy_len in range(1, min([max_len, i]) + 1):
            if dp_costs[i-buy_len] != math.inf:  # не можем прийти из длины, до которой не доходили
                cost_buy = get_cost(buy_len, normal_cost, cost_with_discount, wholesale_len)
                if dp_costs[i - buy_len] + cost_buy < dp_costs[i]:
                    dp_costs[i] = dp_costs[i - buy_len] + cost_buy
                    paths[i] = paths[i-buy_len] + [[ind_shop, buy_len]]

if sum_len < need_len:
    print(-1)
else:
    buyLen_in_shops = [0] * n
    ind_cost = min(enumerate(dp_costs[need_len:]), key = lambda x: x[1])[0] + need_len   # индекс минимальной стоимости
    print(dp_costs[ind_cost])
    for num_shop, buy_len in paths[ind_cost]:
        buyLen_in_shops[num_shop] = buy_len

    print(*buyLen_in_shops)
