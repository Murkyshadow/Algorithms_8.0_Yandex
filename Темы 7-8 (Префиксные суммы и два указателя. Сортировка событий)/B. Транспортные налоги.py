# Нам даны отсортированные ставки (мощность/ставка) и для каждой машины дана мощность (не указано, что отсортирована)
# отсортируем мощности автомобилей и будем идти 2мя указателямя (один указывает на ставки, а 2ой на мощность автомобиля)
# и для каждой мощности автомобиля будем искать подходящую ставку (двигая 1ый указатель вправо пока мощность машины не станет строго больше), если нашли,
# то записываем произведение в ответ и переходим к след. машине
# Эту задачу можно и через бин поиск решить
import math

bets = [list(map(int, input().split())) for _ in range(int(input()))]
power_cars = sorted([[int(input()), i] for i in range(int(input()))])
POWER, BET, IND = 0, 1, 1
cur_car = 0
cur_bet = 0
bets.append([math.inf, math.inf])
ans = [None] * len(power_cars)
while cur_car < len(power_cars):
    while bets[cur_bet+1][POWER] < power_cars[cur_car][POWER]:  # следующая мощность у ставки будет меньше мощности машины
        cur_bet += 1
    ans[power_cars[cur_car][IND]] = power_cars[cur_car][POWER]*bets[cur_bet][BET]
    cur_car += 1

print(*ans, sep='\n')

