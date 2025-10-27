# Будем использовать префексную сумму, в которой будем хранить кол-во подходящих участников
# с начала очереди, до текущего элемента, если пришел новый кандидат, то добавляем новый эл. в преф. сумму
# если из начала очереди ушло k кандидат, то нам просто не надо учитывать k первых кандидат (просто вычтем
# одну преф сумму из другой, чтобы обрезать начало)

n, min_professionalism = map(int, input().split())
pref_sum = [0]
candidates = list(map(int, input().split()))
for i in range(n):
    prof = candidates[i]
    if prof >= min_professionalism:
        pref_sum.append(pref_sum[-1]+1)
    else:
        pref_sum.append(pref_sum[-1])

count_leave = 0
ans = []
for _ in range(int(input())):
    event = list(map(int, input().split()))
    if event[0] == 1:   # в конец очереди пришел кандидат
        prof = event[1]
        if prof >= min_professionalism:
            pref_sum.append(pref_sum[-1] + 1)
        else:
            pref_sum.append(pref_sum[-1])
    elif event[0] == 2: # из начала очереди ушел кандидат
        count_leave += 1
    elif event[0] == 3: # Маша спрашивает сколько подходящий кандидатов
        k = event[1]
        ans.append(pref_sum[k+count_leave] - pref_sum[count_leave])

print(*ans, sep='\n')


