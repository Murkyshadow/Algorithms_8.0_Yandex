# 1:08 - 1:16

count_syms = {}
s = input()
for sym in s:
    count_syms[sym] = count_syms.get(sym, 0) + 1

lost_syms = len(s)
combinations = 1    # можем ничего не менять
for sym, num in count_syms.items():
    lost_syms -= num    # не имеет смысла менять друг с другом одинаковые символы
    combinations += num * lost_syms # но мы можем их поменять с любым из тех, с которыми еще не меняли

print(combinations)
