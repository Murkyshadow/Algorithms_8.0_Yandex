# 0:39 - 0:49
import sys
sys.setrecursionlimit(10**6)

def bypass_tree(root):
    global global_time
    global_time += 1
    times_node[root].append(global_time)
    for child in tree[root]:
        bypass_tree(child)
    global_time += 1
    times_node[root].append(global_time)

n = int(input())
tree = [[] for _ in range(n+1)]
for child, parent in enumerate((map(int, input().split())), 1):
    tree[parent].append(child)
root = tree[0][0]

times_node = [[] for _ in range(n+1)] # для каждой ноды time in / time out
global_time = 0
bypass_tree(root)

m = int(input())
ans = [0] * m
TIME_IN, TIME_OUT = 0, 1
for i in range(m):
    parent, child = map(int, input().split())
    ans[i] = int(times_node[parent][TIME_IN] < times_node[child][TIME_IN] < times_node[child][TIME_OUT] < times_node[parent][TIME_OUT])

print(*ans, sep='\n')