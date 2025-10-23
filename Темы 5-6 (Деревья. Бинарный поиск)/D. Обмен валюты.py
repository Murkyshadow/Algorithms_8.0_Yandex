# 21:45-22:19 - bin search, 22:19-23:09 00:00-00:25
# можно и через бинарный поиск для каждой таблички искать наиболее подходящую
# а можно через 2 указателя, что вроде немного проще:
# сортируем таблички, а потом за O(n) ищем для 1ой таблички ближайшую табличку к
# заданному курсу, а для следующей табличке нужная табличка будет
# где-то рядом, тк массив отсортирован и мы ее фактически за O(1) сможем найти
# так же учтем, что перед сортировкой надо пронумеровать таблички
import math

n, need_p = map(int, input().split())
nums_1 = list(map(lambda x: [int(x[1]), x[0]], [(i,n) for i,n in enumerate(input().split(), 1)])) # пронумеруем перед сортировкой
nums = sorted(nums_1)

cur_2 = 1
ans = (0,0,math.inf)    # cur_1, cur_2, min p
for cur_1 in range(n):
    left_p = right_p = math.inf
    while 1:
        new_p = abs(nums[cur_1][0] / nums[cur_2][0] - need_p)
        if cur_2-1 >= 0:
            left_p = abs(nums[cur_1][0] / nums[cur_2-1][0] - need_p)
        if cur_2+1 < len(nums):
            right_p = abs(nums[cur_1][0] / nums[cur_2+1][0] - need_p)

        if left_p < new_p and cur_2-1 >= 0:
            new_p = left_p
            cur_2 -= 1
        elif right_p <= new_p and cur_2+1 < len(nums):
            new_p = right_p
            cur_2 += 1
        else:
            break

    if cur_2 == cur_1:  # мы не можем одну и ту же табличку взять дважды, поэтому берем рядом (слева или справа)
        left_p = right_p = math.inf
        if cur_2-1 > 0:
            left_p = abs(nums[cur_1][0] / nums[cur_2-1][0] - need_p)
        if cur_2+1 < len(nums):
            right_p = abs(nums[cur_1][0] / nums[cur_2+1][0] - need_p)
        if left_p < right_p and cur_2-1 > 0 and left_p < ans[2]:
            ans = (nums[cur_1][1], nums[cur_2-1][1], left_p)
        elif cur_2+1 < len(nums) and right_p < ans[2]:
            ans = (nums[cur_1][1], nums[cur_2+1][1], right_p)
    elif new_p < ans[2]:
        ans = (nums[cur_1][1], nums[cur_2][1], new_p)

print(ans[0], ans[1])