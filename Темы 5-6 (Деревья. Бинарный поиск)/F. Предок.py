# 2:15 - 2:55
# дан массив чисел A, где А[i] - номер ролителя, а i - номер вершины (те вершина А[i] родитель вершины i), i нумеруется с 1го
# дерево храним в словаря, где ключ - это родитель, а значение - это массив детей
# далее записываем все запросы в словарь (вместе с index запроса) и рекурсивно обходим дерево параллельно, храня всех
# предков данной вершины и при этом обрабатывая запросы для данной вершины, ответ записываем в список ответов по сохраненному index запроса
import sys
sys.setrecursionlimit(10**6)

n = int(input())
tree = {}
for child, parent in enumerate((map(int, input().split())), 1):
    tree[parent] = tree.get(parent, [])
    tree[parent].append(child)

def bypass_tree(root, parents):
    if root in queries: # обрабатываем запросы
        for parent_or_not, ind_query in queries[root]:
            ans[ind_query] = int(parent_or_not in parents)

    if not root in tree:    # листок
        return
    parents.add(root)
    for child in tree[root]:
        bypass_tree(child, parents)
    parents.remove(root)

all_parents = {}
root = tree[0][0]
m = int(input())
queries = {}    # храним запросы, чтобы потом их во время обхода обработать, ключ вершина, а значение массив вершин - потенциальных предков, которые надо проверить
ans = [0] * m
for ind_query in range(m):
    parent_or_not, child = map(int, input().split())
    queries[child] = queries.get(child, [])
    queries[child].append((parent_or_not, ind_query))    # родитель или же нет?

bypass_tree(root, set())
print(*ans, sep='\n')