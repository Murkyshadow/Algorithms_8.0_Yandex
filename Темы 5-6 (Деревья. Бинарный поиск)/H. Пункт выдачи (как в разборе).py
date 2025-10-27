# алгоритм как в разборе https://www.youtube.com/live/TU8eEWYqgdc?si=i4gDhlDPUlKxGWUY&t=3722
# Строим дерево через список, выбираем любую вершину - подвешиваем дерево.
# Рекурсивно обходим дерево и с каждого ребенка возвращаем сумму людей - очередь, а какая очередь будет от предка?
# Все люди минус сумма людей от детей и минус кол-во людей в текущей площади, наибольшее из этих чисел (череди от детей,
# очередь от предка, отдельная очередь текущей площади) и получаем максимум для текущей площади, среди таких максимумов
# ищем минимум - наш ответ (только в ответе указываем индекс этой площади)
import sys
sys.setrecursionlimit(10**6)
import math

def bypass(node):
    global ans
    sum_child = 0
    max_queue = populations[node]
    while tree[node]:
        child = tree[node].pop()
        tree[child].remove(node)    # чтобы потом от ребенка снова в предка не зайти
        child_queue = bypass(child)
        sum_child += child_queue
        max_queue = max(max_queue, child_queue)
    max_queue = max(max_queue, TOTAL_PEOPLES - sum_child - populations[node])   # сравниваем с тем сколько от предка придет
    if ans[0] > max_queue:  # а меньше ли максимальная очередь на этой площади, чем была ранее?
        ans = (max_queue, node)
    return sum_child + populations[node]

n = int(input())
populations = [None] + list(map(int, input().split()))     # кол-во жителей на каждой площади, смещаем на 1 тк нумерация площадей с 1го
TOTAL_PEOPLES = sum(populations[1:])
tree = [set() for _ in range(n+1)]
for _ in range(n-1):
    v1, v2 = map(int, input().split())
    tree[v1].add(v2)
    tree[v2].add(v1)

ans = (math.inf, None)  # в ответе храним минимальную сумму и индекс
root = 1
bypass(root)

print(ans[1])
