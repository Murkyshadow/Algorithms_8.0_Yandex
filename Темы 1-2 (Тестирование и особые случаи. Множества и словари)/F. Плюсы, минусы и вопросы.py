# 16:43 - 17:10
rows, cols = map(lambda x: int(x), input().split())
get_col = lambda num_col, nums: [row[num_col] for row in nums]
sum_row = []
matrix = []
for num_row in range(rows):
    line = input()
    matrix.append(line)
    sum_row.append(line.count('?') + line.count('+') - line.count('-')) # сумма в строке если заменить вопросы на плюсы

sum_col = []
for num_col in range(cols):
    line = get_col(num_col, matrix)
    sum_col.append(- line.count('?') + line.count('+') - line.count('-')) # сумма в строке если заменить вопросы на минусы

max_dif = sum_row[0] - sum_col[0] - 2
for num_col in range(cols):
    for num_row in range(rows):
        max_dif = max([max_dif, sum_row[num_row] - sum_col[num_col] - (2 if matrix[num_row][num_col] == '?' else 0)])

# print(sum_row, sum_col)
print(max_dif)
