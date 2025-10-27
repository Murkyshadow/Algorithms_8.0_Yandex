# Первое, что пришло в голову - это бин. поиск, поэтому его я и реализовал
# Будем перебирать всевозможные варианты серий и искать минимальную переплату с мин. кол-вом серий
# Наша функция переплаты f(e) = sum(|e-s[i]|*a[i]) (e - число эпизодов) представляет из себя параболу,
# в которой мы будем искать min(e), те представьте параболу (направленную вверх), мы получаем mid (средний индекс - кол-во серий)
# и если справа  f(mid) < f(mid+1), то мы оказались на правой половине параболы (тк правая половина возрастает), ее можно отсечь (right = mid)
# если справа от mid f(mid) > f(mid+1), то мы оказались на левой половине параболы (левая половина убывает) и таким образом мы можем понимать
# с какой стороны надо отсечь половину, а написать функцию получения переплаты от данного эпизода: просто в лоб

def get_total_payment(e):
    total_money = 0
    for j in range(n):
        total_money += abs(e - s[j]) * a[j]
    return total_money

n = int(input())
s = list(map(int, input().split()))
a = list(map(int, input().split()))
left, right = min(s)-1, max(s)+1
while left <= right:
    mid = (left + right) // 2
    total_payment_mid = get_total_payment(mid)
    total_payment_mid_right = get_total_payment(mid+1)
    if total_payment_mid <= total_payment_mid_right:
        right = mid
    else:
        left = mid + 1

print(mid, total_payment_mid)

