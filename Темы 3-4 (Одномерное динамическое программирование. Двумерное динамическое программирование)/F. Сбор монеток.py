# идем сверху вниз выбирая для каждой ячейки наибольщее кол-во монет,
# так же обрабатываем стены (можно их помечать -бесконечностью)
import math
n = int(input())
dp = []
for _ in range(n):
    row = list(input())
    row[0] = 0 if row[0] == '.' else (1 if row[0] == 'C' else -math.inf)
    row[1] = 0 if row[1] == '.' else (1 if row[1] == 'C' else -math.inf)
    row[2] = 0 if row[2] == '.' else (1 if row[2] == 'C' else -math.inf)
    dp.append(row)

ans = max(dp[0]+[0])

for num_row in range(1, n):
    dp[num_row][0] = max([dp[num_row-1][0], dp[num_row-1][1]])+dp[num_row][0] if dp[num_row][0] != -math.inf else -math.inf
    dp[num_row][1] = max([dp[num_row - 1][0], dp[num_row - 1][1], dp[num_row-1][2]]) + dp[num_row][1] if dp[num_row][1] != -math.inf else -math.inf
    dp[num_row][2] = max([dp[num_row - 1][2], dp[num_row - 1][1]]) + dp[num_row][2] if dp[num_row][2] != -math.inf else -math.inf
    ans = max(dp[num_row]+[ans])


print(ans)
