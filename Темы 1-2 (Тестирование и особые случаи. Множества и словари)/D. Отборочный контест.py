# 0:50

n, k = map(int, input().split())
nums = list(map(int, input().split()))

count_themes = {}
for theme in nums:
    count_themes[theme] = count_themes.get(theme, 0) + 1

num_repeat_themes = k - len(count_themes)
ans = []
lost_task = k
for theme, num in count_themes.items():
    ans += [theme]
    lost_task -= 1
    if not lost_task:
        break
    if num_repeat_themes > 0:
        ans += [theme] * min([num-1, num_repeat_themes])
        num_repeat_themes -= min([num-1, num_repeat_themes])

print(*ans)