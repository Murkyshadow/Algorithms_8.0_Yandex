# 17:16-18:03 18:37-18:57 = 47+20 = 67 - сложное решение с кучей (неудача)
# 3:15 - 4:00 - переписал код
# С помощью бин поиска перебираем все возможные масштабы, чтобы проверить подходит ли этот
# масштаб или нет, просто пытаемся жадно вместить слова с учетом масштаба

def checking_scale(scale):
    WEIGHT, HEIGHT = 0, 1
    max_weight, max_height = w, h   # размер поля
    now_text_w, now_text_h, now_line_w = words[0][WEIGHT], words[0][HEIGHT], words[0][WEIGHT]
    before_word_h = words[0][HEIGHT]
    for i, word in enumerate(words[1:]):    # расставляем слова с учетом заданных границ
        w_word, h_word = word
        if before_word_h != h_word or (now_line_w + w_word)*scale > max_weight:            # переходим на новую строку, если слово вылезает за границы (по ширине) или оно другой высоты
            now_text_h += h_word
            now_line_w = 0
        now_line_w += w_word
        now_text_w = max([now_text_w, now_line_w])
        before_word_h = h_word

    if now_text_w*scale <= max_weight and now_text_h*scale <= max_height:   # уместили текст (и по ширине и по высоте)
        return True
    return False    # не уместили


n, w, h = map(int, input().split())
words = []
for _ in range(n):
    words.append(list(map(int, input().split())))

left = 0.000001
right = 10**9   # тут прикинем, а что если взять наименьшее слово и наибольшее поле, то во сколько раз его можно увеличить?
mid = (left+right) / 2  # наш приблизительный масштаб

for _ in range(60): # bin_search, ищем нужный масштаб, 60 тк 10**9 * 10**6 (макс * точность) логарифм дает ~60
    if checking_scale(mid): # если с данным масштабом слов весь текст можно уместить в поле, то увеличиваем масштаб слов (отбрасываем меньший масштаб, с которым тем более можно уместить текст в поле)
        left = mid
    else:
        right = mid
    mid = (left+right) / 2

print(mid)