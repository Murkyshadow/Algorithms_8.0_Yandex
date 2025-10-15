# просто храним все индексы, с которых начинается каждое новое слово
# для этого для каждого символа перебираем все слова начинающиеся после каждого возможного пробела
# и проверяем есть ли данное слово в словаре, если да, то нашли новую цепочку слов
s = input()
words = set()
for i in range(int(input())):
    words.add(input())

whitespaces = set([-1]) # индексы символов после которых можно поставить пробел - по факту индекс конца слова
ind_start_word = [-1]*len(s)    # храним индексы начала каждого слова
for i, sym in enumerate(s):
    for st_word in whitespaces: # после пробела начинается слово (поэтому +1)
        new_word = s[st_word+1:i+1]
        if s[st_word+1:i+1] in words:
            ind_start_word[i] = st_word + 1 # записываем индекс начала слова
            whitespaces.add(i)  # индекс символа после которого пробел идет
            break

ans = []
ind_start_word.append(len(s) + 1) # чтобы последнее слово обработать
start_word = ind_start_word[-2]
end_word = ind_start_word[-1]

while end_word != -1:
    ans.append(s[start_word:end_word+1])
    end_word = start_word - 1
    start_word = ind_start_word[end_word]


print(' '.join(ans[::-1]))
