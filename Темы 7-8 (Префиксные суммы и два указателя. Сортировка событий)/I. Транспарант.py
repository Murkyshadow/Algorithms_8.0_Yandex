# 4:00-4:25 + 31м на тесты
# Даны целочисленные точки и необходимо определить между сколькими парами точек квадрат расстояния
# равен D - квадрат длины плаката (целое число)
# Для начала вспомним формулу рассчета расстояния между 2мя точками:
# |x1-x2|**2 + |y1-y2|**2 = D (сумма квадратов катетов равна квадрату гипотенузы)
# Разность иксов и игреков (по модулю) обозначим, как dx, dy --> dx**2 + dy**2 = D
# А сколько существует таких dx, dy квадраты которых будут давать D? А давайте их найдем и
# для каждой точки будем перебирать их (прибавляя), получая координаты новой точки и будем
# быстро проверять существует ли точка, которую мы получили среди данных изначально
# Что бы насчитать все возможные сдвиги (dx, dy) мы просто будем перебирать  числа до 10 000 (тк корень из 10**8 это 10**4)
# находить их квадрат и определять существует ли для этого квадрата второе число, возведя в квадрат которое в сумме получим D
# А что бы быстро проверять новую точку будем хранить исходные точки в сете в виде пары координаты (x, y) словаре {y1: set(x1,x2,...), y2: set(...), ...}
# И какова сложность данного алгоритма? Насчитать сдвиги сможем за 10**4, далее надо пробежаться по всем n точкам и для каждой проветь k сдвигов (dx, dy)
# А сколько таких сдвигов будет в худшем случае? Рассчитать возможно и можно это число, но легче просто перебрать все возможные варианты
# и получим, что в худшем случае для чисел (85399925, 72) (77068225, 72) по 72 комбинации, но так же надо еще учитывать
# и отрицательные сдвиги, те комбинаций будет 72*4 = 288 в худшем случае (хотя максимум 144, иначе при переходе к следующей точке мы затронем и предыдущую)
# то есть примернно 300 * 10**5 = 3 * 10**7 - что в целом еще может зайти на питоне с временым ограничением 7 секунд (хотя не точно), но точно зайдет на pypy
# код перебора всех сдвигов:
# from time import time
# squares = [num**2 for num in range(10**4 + 1)]
# count_sums = {}
# for i, square in enumerate(squares):
#     for square_2 in squares:
#         s = square + square_2
#         if s <= 10**8:
#             count_sums[s] = count_sums.get(s, 0) + 1
# print(time() - t)
# print(len(count_sums))
# print(*sorted(count_sums.items(), key=lambda x:x[1], reverse=True)[:100], sep='\n')

def solution(n,D,coors):
    squares = {num**2:num for num in range(int(D**0.5)+2)}
    offsets = set()
    for square, offset_x in squares.items():    # ищем все смещения
        square_2 = D - square
        if square_2 in squares:
            offset_y = squares[square_2]
            offsets.add((offset_x, offset_y))
            offsets.add((offset_x, -offset_y))
            offsets.add((-offset_x, offset_y))
            offsets.add((-offset_x, -offset_y))

    ans = 0
    while coors:
        x, y = coors.pop()
        for dx, dy in offsets:
            new_x = x + dx
            new_y = y + dy
            if (new_x, new_y) in coors: # есть такая точка
                ans += 1

    return ans

n, D = map(int, input().split())
coors = set()
for _ in range(n):
    x,y = map(int, input().split())
    coors.add((x, y))
print(solution(n,D,coors))



# Для стресс тестирования:
# from random import randint as r
# def generator():
#     n = r(1, 50)
#     d = r(1, 20)
#     return n, d, [(r(-10**1, 10**1), r(-10**1, 10**1)) for _ in range(n)]
#
# def slow_solution(n,D,coors):
#     ans = 0
#     for x,y in coors:
#         for x_2, y_2 in coors:
#             if x != x_2 or y != y_2:
#                 D_2 = abs(x-x_2)**2 + abs(y-y_2)**2
#                 if D_2 == D:
#                     ans += 1
#     return ans / 2

# while 1:
#     n, D, coors = generator()
#     coors = set(coors)
#     ans_1 = slow_solution(n, D, coors)
#     ans_2 = solution(n, D, coors)
#     if ans_1 == ans_2:
#         # print(ans_1)
#         pass
#     else:
#         print(ans_1,ans_2)