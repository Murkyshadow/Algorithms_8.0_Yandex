# Это решение проходит на чистом питоне
# решение аналогично прошлому, но тут мы не копируем каждый раз массивы, а храним рассчеты в 2х переменных

def check_k(k, lost_candidates, lost_places, n):
    cur_place, cur_candidate = 0, 0
    candidates = lost_candidates[cur_candidate]
    places = lost_places[cur_place]
    while cur_candidate < n:
        m = candidates if candidates < places else places
        candidates -= m
        places -= m
        if candidates == 0:
            cur_candidate += 1
            if cur_candidate == n:
                break
            candidates = lost_candidates[cur_candidate]

        if places == 0:
            cur_place += 1
            if cur_place - cur_candidate > k:
                break

        while cur_candidate - cur_place > k:
            places = 0
            cur_place += 1

        if cur_place < n and not places:
            places = lost_places[cur_place]

    return 1 if cur_candidate == len(lost_candidates) else 0

def binary_search(n, lost_candidates, lost_places):
    left = 0
    right = n-1    # расстояние между 1ым и n днем
    ans = -1
    while left <= right:
        k = (left + right) // 2
        if check_k(k, lost_candidates, lost_places, n):
            ans = k
            right = k-1
        else:
            left = k+1
    return ans

n = int(input())
lost_candidates = list(map(int, input().split())) # количество кандидатов, которые хотят пройти собеседование
lost_places = list(map(int, input().split())) # количество мест
print(binary_search(n, lost_candidates, lost_places))