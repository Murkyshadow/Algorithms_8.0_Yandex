# 0 - корень дерева (столица), является предком для всех
# мы можем менять баланс на любом участке от столицы до любого города на +-1
# поэтому начнем менять баланс с листков, для этого:
# рекурсивно обходим дерево и из каждого поддерева возвращаем, то на сколько надо изменить баланс
# в ответ прибавляем кол-во изменний
def bypass_tree(root):
    global ans
    change_balance_city = 0     # то на сколько надо изменить баланс
    for child in tree[root]:
        change_child_balance = bypass_tree(child)
        change_balance_city += change_child_balance

    balance_cities[root] += change_balance_city # изменяем свой баланс на то на сколько изменился баланс у детей
    change_balance_city += -balance_cities[root]    # так же и свой баланс свести к нулю надо
    ans += abs(balance_cities[root])    # считаем кол-во изменений
    return change_balance_city

n = int(input())
root = 0    # столица
tree = [[] for i in range(n)]   # дерево
for child in range(1, n):
    parent = int(input())
    tree[parent].append(child)

balance_cities = list(map(int, input().split()))
ans = 0 # считаем эдикты (кол-во изменений)
bypass_tree(root)

print(ans)
