# 23:35 - 0:29 понял, что облажался с алгоритмом
# 15:23 - 16:30 + 30минут на стресс тесты
# У нас имеется A, B - множество значений, а n, m их длины
# и нам надо вычислить Σᵢ Σⱼ ((i - j) × |aᵢ - bⱼ|), те перебрать все комбинации чисел из множества A и B
# если перемножить значения то получим ΣᵢΣⱼ((i × |aᵢ - bⱼ| - j × |aᵢ - bⱼ|) = ΣᵢΣⱼ((i × |aᵢ - bⱼ|) - ΣᵢΣⱼ(j × |aᵢ - bⱼ|) =
# = Σᵢ (i × Σⱼ|aᵢ - bⱼ|) - Σⱼ (j × Σᵢ|aᵢ - bⱼ|), но надо как-то быстро вычислять выражение Σ|aᵢ - bⱼ|, но из-за модуля
# нельзя быстро его сосчитать, тк не будешь  знать какое число будет в результате вычитания: положительное или отрицательное
# НО если мы заранее будем знать, что результат будет положительным для этой группы чисел, для той отрицательным,
# то сможем воспользоваться префиксными суммами, то есть нам просто нужно для каждого aᵢ находить все числа из B
# меньше и больше его. Для этого мы отсортируем исходные массивы A, B и с помощью бин поиска будем находить для каждого aᵢ две части B:
# left_b - все числа в B меньше aᵢ длиной = len_l
# right_b - все числа в B больше aᵢ длиной = len_r
# и получим для Σⱼ|aᵢ - bⱼ| = (aᵢ × len_l - sum_left_b) - (aᵢ × len_r - sum_right_b), когда мы вычитаем sum_right_b,
# то все значения будут с минусом, поэтому ставим минус, чтобы получить положительное число (ведь мы убрали модуль)
# те же действия проводим и с Σⱼ|aᵢ - bⱼ| = (bⱼ × len_l - sum_left_a) - (bⱼ × len_r - sum_right_a)
# Σᵢ (i × ((aᵢ × len_l - sum_left_b) - (aᵢ × len_r - sum_right_b))) - Σⱼ (j × ((bⱼ × len_l - sum_left_a) - (bⱼ × len_r - sum_right_a)))
# напомню, что sum_left_b, sum_right_b, sum_left_a, sum_right_a они меняются и что бы вычислить их быстро надо использовать префиксные суммы



def solution(n, A, m, B):
    def bin_search(x, nums):   # для aᵢ находим ind_b где все числа из B левее меньше, а правее больше=
        left = 0
        right = len(nums)-1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid][0] >= x:
                right = mid-1
            else:
                left = mid+1
        return left

    A = sorted([(a_i, i) for i, a_i in enumerate(A)])   # сортируем, чтобы потом бин поиском быстро проходиться
    B = sorted([(b_j, j) for j, b_j in enumerate(B)])

    pref_sum_A = [0]
    for i in range(n):
        pref_sum_A.append(pref_sum_A[-1] + A[i][0])

    pref_sum_B = [0]
    for j in range(m):
        pref_sum_B.append(pref_sum_B[-1] + B[j][0])

    ans = 0
    for ai, i in A:  # найдем Σᵢ (i × ((aᵢ × len_l - sum_left_b) - (aᵢ × len_r - sum_right_b)))
        ind_B_more_ai = bin_search(ai, B)   # индекс первого числа >= ai
        sum_B_nums_less_ai = pref_sum_B[ind_B_more_ai]    # sum_left - сумма чисел меньше ai
        sum_B_nums_more_ai = pref_sum_B[-1] - sum_B_nums_less_ai    # sum_right
        len_l = ind_B_more_ai
        len_r = len(B) - len_l
        ans += i * ((ai*len_l - sum_B_nums_less_ai) - (ai*len_r - sum_B_nums_more_ai))   # (i × ((aᵢ × len_l - sum_left_b) - (aᵢ × len_r - sum_right_b)))
    # повторяем то же самое:
    for bj, j in B:  # найдем -Σⱼ (j × ((bⱼ × len_l - sum_left_a) - (bⱼ × len_r - sum_right_a)))
        ind_A_more_bj = bin_search(bj, A)  # индекс первого числа в A >= bj
        sum_A_nums_less_bj = pref_sum_A[ind_A_more_bj]  # sum_left - сумма чисел меньше ai
        sum_A_nums_more_bj = pref_sum_A[-1] - sum_A_nums_less_bj  # sum_right
        len_l = ind_A_more_bj
        len_r = len(A) - len_l
        ans -= j * ((bj * len_l - sum_A_nums_less_bj) - (bj * len_r - sum_A_nums_more_bj))  # - (j × ((bⱼ × len_l - sum_left_a) - (bⱼ × len_r - sum_right_a))

    return ans

n = int(input())
A = list(map(int, input().split())) # i
m = int(input())
B = list(map(int, input().split())) # j
print(solution(n, A, m, B))


# Для стресс тестов:
# def slow_solution(n, A, m, B):
#     ans = 0
#     #  Σᵢ Σⱼ ((i - j) × |aᵢ - bⱼ|)
#     for i in range(n):
#         for j in range(m):
#             ans += (i-j) * abs(A[i] - B[j])
#     return ans
#
# from random import randint
# def generator_nums():
#     n = randint(90000,100000)
#     A = [randint(1,10000) for _ in range(n)]
#     m = randint(90000,100000)
#     B = [randint(1,10000) for _ in range(m)]
#     return n, A, m, B
#
# import time
# while 1:
#     n, A, m, B = generator_nums()
#     t = time.time()
#     ans_1 = solution(n, A, m, B)
#     t_2 = time.time()
#     ans_2 = slow_solution(n, A, m, B)
#     print(round(t_2-t, 4),  round(t_2 - time.time(), 4), ans_1)
#
#     # if ans_1 != ans_2:
#     #     print(ans_1, ans_2)
#     #     print(n, A, m, B, sep='\n')
#     #     break
#     # else:
#     #     print(True)