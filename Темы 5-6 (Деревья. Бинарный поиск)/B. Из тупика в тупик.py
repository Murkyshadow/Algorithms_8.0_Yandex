# начинаем идти со всех листов (те у которых 1 родитель) обходом в ширину (сначала обрабатываем все листы,
# потом всех детей этих листов и только потом детей детей листов) и идем до тех пор пока не встретимся при этом
# таща длину пути, длины пути складываем и получаем ответ (выбираем минимальный ответ из полученных)

n = int(input()) - 1
graf = {}
for _ in range(n):
    v1, v2 = map(int, input().split())
    graf[v1] = graf.get(v1, [])
    graf[v1].append(v2)
    graf[v2] = graf.get(v2, [])
    graf[v2].append(v1)

now_vertexes = set()
visited_vertex = [-1] * (n+2)
for key in graf:
    if len(graf[key]) == 1:
        now_vertexes.add((key, 0))  # начальные точки - тупики
        visited_vertex[key] = 0

MAX_TRANSITIONS = n+2
min_transitions = MAX_TRANSITIONS
while 1:
    new_vert = set()
    for vertex, transitions in now_vertexes:
        visited_vertex[vertex] = MAX_TRANSITIONS    # пишем, что бы не посчитать жто значение (вернуться назад)
        for neighbour_vert in graf[vertex]:
            if visited_vertex[neighbour_vert] == -1:
                new_vert.add((neighbour_vert, transitions+1))
                visited_vertex[neighbour_vert] = transitions+1
            elif neighbour_vert != vertex:
                min_transitions = min([min_transitions, transitions + 1 + visited_vertex[neighbour_vert]])
    if min_transitions != MAX_TRANSITIONS:
        break
    now_vertexes = new_vert

print(min_transitions)

