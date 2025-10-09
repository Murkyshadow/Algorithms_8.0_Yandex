# 20:20 - 20:34
n = int(input())
m = list(map(int, input().split()))
Vasya_mushrooms = m[0::2]
Masha_mushrooms = m[1::2]
max_Masha = max(Masha_mushrooms)
min_Vasya = min(Vasya_mushrooms)

ans = sum(Vasya_mushrooms) - sum(Masha_mushrooms)
if max_Masha > min_Vasya:
    ans -= min_Vasya*2
    ans += max_Masha*2
print(ans)
