# дороги к площадям представляем в виде словаря (граф смежности)
# Обход начинаем с листьев, обходим в ширину (len = 1)
# Для каждой вершины храним максимальную очередь со всех направлений
# Постепенное "схлопывание" - обрабатываем вершины, у которых все соседи, кроме одного обработаны
# учитываем, что идти надо в обе стороны
# PS лучше смотрите решение, как в разборе у Михаила Густокашина

def solution(n, people, edges):
    if n == 1:
        return 1
    graf = {}   # ключ - номер площади, значение - номера площадей, в которые можно прийти
    for v1,v2 in edges:
        graf[v1] = graf.get(v1, set())
        graf[v1].add(v2)
        graf[v2] = graf.get(v2, set())
        graf[v2].add(v1)

    number_people_squares = [0] + people[::]   # или [::] !!!!!
    max_queryes = [0] + people[::]   # для каждой площади вычисляем максимальную очередь, но очередь из жителей данной площади то же надо учитывать (у них отдельный вход)
    count_left_neighbours = [0]*(n+1)    # считаем кол-во оставшихся приходов (соседей от которых мы еще не пришли)
    next_squares = set()  # обрабатываем новые вершины (площади)
    for key in graf:
        count_left_neighbours[key] = len(graf[key])
        if len(graf[key]) == 1:
            next_squares.add(key)

    roads_traveled = set()  # пары вершин между которыми уже прошлись
    while next_squares:
        new_squeres = set()
        for square in next_squares:
            del_vert = set()
            for neighbour_square in graf[square]:
                if (not (neighbour_square, square) in roads_traveled and (count_left_neighbours[square] == 1)) or count_left_neighbours[square] == 0:
                    roads_traveled.add((square, neighbour_square))
                    del_vert.add(neighbour_square)
                    count_left_neighbours[neighbour_square] -= 1
                    come_people = number_people_squares[square] # пришло из square в neighbour_square
                    if (neighbour_square, square) in roads_traveled:   # но надо вычесть если мы уже посчитали из neighbour_square в square, иначе дважды одних и тех же людей посчитаем
                        come_people -= number_people_squares[neighbour_square]

                    max_queryes[neighbour_square] = max(max_queryes[neighbour_square], come_people)   # выбираем большую очередь: то сколько пришло с другой дороги или с текущей
                    number_people_squares[neighbour_square] += come_people
                    if count_left_neighbours[neighbour_square] <= 1:
                        new_squeres.add(neighbour_square)

            graf[square] -= del_vert  # просто обнулить !!! ИЛИ БЕЗ ЭТОЙ СТРОКИ !!! чтобы не идти по той же дороге вновь

        next_squares = new_squeres

    min_ind = 1
    for i in range(1, n+1):
        if max_queryes[i] < max_queryes[min_ind]:
            min_ind = i

    return min_ind

n = int(input())
populations = list(map(int, input().split()))
edges = [list(map(int, input().split())) for _ in range(n-1)]

print(solution(n, populations, edges))
