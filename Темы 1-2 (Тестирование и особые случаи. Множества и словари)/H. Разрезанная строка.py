# 22:54 - 23:25
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
# print(len(set(ans)))