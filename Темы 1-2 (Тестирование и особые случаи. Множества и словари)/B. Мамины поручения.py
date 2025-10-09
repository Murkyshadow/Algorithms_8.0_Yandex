# 20:37-20:50   21:43-22:04 = 32

a, b, c, v0, v1, v2 = map(int, input().split())
v = [v0, v1, v2]
now_v = v0
count_items = 0

s_home_shop = min([a, b+c])
s_home_wb = min([b, a+c])
s_shop_wb = min([c, a+b])

# c двумя покупками: home -> wb -> shop -> home или home -> shop -> wb -> home
ans = min([s_home_wb/v[0] + s_shop_wb/v[1] + s_home_shop/v[2], s_home_shop/v[0] + s_shop_wb/v[1] + s_home_wb/v[2]])
# с одной покупкой: home -> wb -> home -> shop -> home
ans = min([ans, s_home_wb/v[0] + s_home_wb/v[1] + s_home_shop/v[0] + s_home_shop/v[1]])
print(ans)