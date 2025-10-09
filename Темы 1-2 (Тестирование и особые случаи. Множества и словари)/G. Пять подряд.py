# ну, тут вроде все просто строки и столбцы получаем и проверяем есть ли в них 5 подряд
# сложность возникает с диагоналями и тут есть несколько способов их перебрать:
# 1) у диагоналей есть свойство y-x=cons для каждой диагонали и y+x = const для обратных диагоналей  (этот вариант и реализован)
# и таким образом перебирая все значения в матрице мы можем легко понять к какой диагонали относится ячейка 
# (хотя хранить все диавгонали будет затратно, поэтому просто храним кол-во повторяющизся символов и последний символ в диагонали) 
# 2) как-то перебирать диагонали изменяя x, y на один
# 3) см. разбор задач лектора

rows, cols = map(int, input().split())
matrix = []
def check_5_successively(s):
    if len(s) < 5:
        return False
    count = 1
    for i, sym in enumerate(s[1:], 1):
        if sym == s[i-1] and sym != '.':
            count += 1
            if count == 5:
                return True
        else:
            count = 1
    return False

ans = 'No'
for _ in range(rows):
    s = input()
    matrix.append(s)
    if check_5_successively(s):
        ans = 'Yes'

get_col = lambda num_col, matrix: [row[num_col] for row in matrix]
for num_col in range(cols):
    if check_5_successively(get_col(num_col, matrix)):
        ans = 'Yes'

diagonals = {}  # у каждой диагонали храним [last_sym, count_repeat]
reverse_diagonals = {}
for num_col in range(cols):
    for num_row in range(rows):
        num = matrix[num_row][num_col]
        diagonals[num_col - num_row] = diagonals.get(num_col - num_row, ['', 1])                   # по всей диагонали x - y = const
        diagonals[num_col - num_row][1] = diagonals[num_col - num_row][1]+1 if diagonals[num_col - num_row][0] == matrix[num_row][num_col] else 1
        diagonals[num_col - num_row][0] = matrix[num_row][num_col]

        reverse_diagonals[num_col + num_row] = reverse_diagonals.get(num_col + num_row, ['', 1])     # по всей диагонали x + y = const
        reverse_diagonals[num_col + num_row][1] = reverse_diagonals[num_col + num_row][1]+1 if reverse_diagonals[num_col + num_row][0] == matrix[num_row][num_col] else 1
        reverse_diagonals[num_col + num_row][0] = matrix[num_row][num_col]

        if diagonals[num_col - num_row][1] == 5 and diagonals[num_col - num_row][0] != '.' \
                or reverse_diagonals[num_col + num_row][1] == 5 and reverse_diagonals[num_col + num_row][0] != '.':
            ans = 'Yes'

print(ans)

# get_diagonal = lambda num_st_col, num_st_row, matrix: [matrix[num_st_row + shift][num_st_col + shift] for shift in range(min([rows - num_st_row, cols - num_st_col]))]
# get_reverse_diagonal = lambda num_st_col, num_st_row, matrix: [matrix[num_st_row + shift][num_st_col - shift] for shift in range(min([rows - num_st_row, num_st_col+1]))]
#
# for num_col in range(cols):
#     if check_5_successively(get_col(num_col, matrix)) or check_5_successively(get_diagonal(num_col, 0, matrix)) or check_5_successively(get_reverse_diagonal(num_col, 0, matrix)):
#         ans = 'Yes'
#
# for num_row in range(rows):
#     if check_5_successively(get_reverse_diagonal(cols-1, num_row, matrix)) or check_5_successively(get_diagonal(0, num_row, matrix)):
#         ans = 'Yes'

