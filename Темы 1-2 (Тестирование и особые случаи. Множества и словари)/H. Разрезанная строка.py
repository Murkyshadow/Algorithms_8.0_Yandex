# Вот что от нас хотят в выводе: пронумеруйте каждый кусок и расставьте эти номера в правильном порядке
# Так и сделаем, единственное надо учитывать, что куски могут повторяться, соответственно повторяющиеся номера записываем в список
# а что бы вывести нужный номер, просто оригинальную строку тоже нарезаем на куски и по этим кускам получаем номер
l, n = map(int, input().split())
len_piece = l // n
piece_num = {}
s  = input()
for i in range(1,n+1):
    piece = input()
    piece_num[piece] = piece_num.get(piece, []) + [i]

ans = []
for i in range(1,n+1):
    piece = s[(i-1)*len_piece:i*len_piece]
    ans.append(piece_num[piece].pop())
    
print(*ans)
