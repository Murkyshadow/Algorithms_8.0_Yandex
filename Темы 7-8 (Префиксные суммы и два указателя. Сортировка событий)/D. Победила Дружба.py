# Считаем сумму слева и считаем сумму начиная справо. Изначально сумма равна по одному столу (один слева, один справа)
# Далее прибавляем по одному столу и пересчитываем ответ. Но с какой стороны прибавлять стол? С той где ответ получится меньше (разность сумм по модулю)
# Просто пробуем прибавить и слева стол и справа стол и сравнить 2 ответа (какой лучше там и оставим стол)

n = int(input())
tables = list(map(int, input().split()))
sum_left = tables[0]
sum_right = tables[-1]
cur_left, cur_right = 0, n-1    # в ответ записываем на 1 больше (тк нумерация столов с единицы)
ans = [abs(sum_right-sum_left), cur_left+1, cur_right+1]
while cur_left+1 < cur_right:
    if abs(sum_left+tables[cur_left+1] - sum_right) < abs(sum_left - (sum_right+tables[cur_right-1])):  # лучше будет прибавить слева стол
        cur_left += 1
        sum_left += tables[cur_left]
    else:   # лучше прибавить справа стол
        cur_right -= 1
        sum_right += tables[cur_right]

    new_ans = [abs(sum_left - sum_right), cur_left+1, cur_right+1]
    if new_ans[0] < ans[0]:
        ans = new_ans

print(*ans)


