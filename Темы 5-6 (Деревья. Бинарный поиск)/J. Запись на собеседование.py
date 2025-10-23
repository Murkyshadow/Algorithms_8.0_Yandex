# 19:10 - 19:30   19:45-20:20 20:50-21:15  = 20 + 35 + 25 = 80м
# Суть задачи: распределить места так, чтобы среди всех кандидатов максимальное недовольство было минимальным.
# Будем с помощью бин поиска искать такое недовольство k и для каждого k будем проверять, а можно ли разместить студентов при этом получив недовольство не больше k?
# Для проверки k будем использовать метод 2х указателей (cur_1, cur_2), 
# где cur_1 будет бегать по оставшимся местам, а cur_2 по кандидатам
# и пытаемся жадно разместить кандидатов в каждый день (те пока есть кандидаты запоняем ими все дни, пока кандидаты не
# кончатся, кончились, тогда к следующим кандидатам переходим, если в текущий день не влезают кандидаты, то переходим к следующему дню)
# если мест не хватает, то двигаем cur_1 правее, если всех уместили, то двигаем cur_2 (по факту просто жадно распределяем кандидатов)
# при этом расстояние между cur_1 и cur_2 должно быть меньше или равно k  |cur_1 - cur_2| <= k
# PS данное решение не проходит python (только pypy), тк тут происходит копирование lost_candidates, lost_places
# Так что если избавится от этого копирования, то зайдет и на pypy

def check_k(k, lost_candidates, lost_places, n):
    cur_place, cur_candidate = 0, 0
    candidates = list(lost_candidates)
    places = list(lost_places)

    while cur_place < n and cur_candidate < n:
        if candidates[cur_candidate] > places[cur_place]:  # кандидатов больше, чем мест
            candidates[cur_candidate] -= places[cur_place]
            places[cur_place] = 0
        else:   # мест >= кандидатов
            places[cur_place] -= candidates[cur_candidate]
            candidates[cur_candidate] = 0

        if candidates[cur_candidate] <= 0:  # ищем не нулевое кол-во кандидатов
            cur_candidate += 1

        while cur_place < n and (places[cur_place] <= 0 or abs(cur_place - cur_candidate) > k):  # ищем не нулевое кол-во мест при этом не дальше чем на k
            cur_place += 1

    return 1 if cur_candidate == len(candidates) else 0

def binary_search(n, lost_candidates, lost_places):
    left = 1
    right = n-1     # расстояние между 1ым и n днем
    while left <= right:
        k = (left + right) // 2
        if check_k(k, lost_candidates, lost_places, n):
            ans = k
            right = k-1
        else:
            left = k+1
    return ans

def solution(n, lost_candidates, lost_places):
    enough_places_for_every_day = True
    for ai, bi in zip(lost_candidates, lost_places):
        if ai > bi:
            enough_places_for_every_day = False

    if enough_places_for_every_day:  # всем хватило мест
        return 0
    elif sum(lost_candidates) > sum(lost_places): # кандидатов больше мест
        return -1
    else:
        return binary_search(n, lost_candidates, lost_places)

n = int(input())
lost_candidates = list(map(int, input().split()))   # количество кандидатов, которые хотят пройти собеседование
lost_places = list(map(int, input().split()))       # количество мест
print(solution(n, lost_candidates, lost_places))

