# рекурсивно обходим поле чисел - для каждого числа ищем числа на 1 больше
# если нашли, то идем к этому числу и ищем числа на 1 больше уже для него
# если не нашли, то просто рекурсивно возвращаемся каждый раз прибавляя 1
# если мы идем в число, а ответ для него уже посчитан (длина цепочки), то просто возвращаем эту длину
# если у числа рядом несколько чисел на 1 больше, то возвращаем наибольшую цепочку
import sys
sys.setrecursionlimit(10**6 + 1)    # иначе RE
def get_len_chain(row, col):    # рекурсивно обходим всю цепочку, возвращаяя длины
    if dp[row][col] == -1:  # идем по цепочке, если в ее еще не обходили, иначе просто результат возвращаем
        max_len = 0     # длина цепочки следующего за текущим числом
        for shift_x, shift_y in shift:
            new_row, new_col = row+shift_y, col+shift_x
            if new_col >= 0 and new_col < cols and new_row >= 0 and new_row < rows and matrix[row][col] == matrix[new_row][new_col] - 1:  # смотрим, чтобы за границы не выползало и что число на 1 больше предыдущего
                max_len = max([max_len, get_len_chain(new_row, new_col)])
        dp[row][col] = max_len + 1

    return dp[row][col]


rows, cols = map(int, input().split())
matrix = []

for _ in range(rows):
    matrix.append(list(map(int, input().split())))

shift = [(1,0), (0,1), (-1, 0), (0, -1)]    # смещение по x, y
dp = [[-1]*cols for _ in range(rows)]
ans = 0
for row in range(rows):
    for col in range(cols):
        if dp[row][col] == -1:
            ans = max([get_len_chain(row, col), ans])

print(ans)

