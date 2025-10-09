# 21:02 - 21:
import re

n = int(input())
pattern = r'(\w+)\.(\w+)\(([^)]+)\)'
variables = {}  # variable:[nums] or variable:(variable_orig, st, end)
ORIG_VARIABLE, START, END = 0,1,2
for _  in range(n):
    line = input()
    if 'List' == line[:4]:
        words = line.split(' ') # List a = new List(2,3,5) or List b = a.subList(2,3)
        nums = re.search(r'\w+\(([^)]+)\)', line).groups()
        nums = list(map(int, nums[0].split(',')))
        variable = words[1]
        if words[3] == 'new':    # List a = new List(2,3,5)
            variables[variable] = nums
        else:   # List b = a.subList(2,3)
            variable_orig = words[-1].split('.')[0]
            start, end = nums
            if type(variables[variable_orig]) == type(list()):   # если делаем подсписок оригинального списка
                variables[variable] = (variable_orig, start, end)
            else: # если делаем подсписок подсписка, то ссылаемся на оригинальный, но сдвигаем окно чисел
                start += variables[variable_orig][1] - 1
                end += variables[variable_orig][1] - 1
                variable_orig = variables[variable_orig][0]
                variables[variable] = (variable_orig, start, end)
    else:
        match = re.search(pattern, line)
        variable, method, nums = match.groups()
        nums = list(map(int, nums.split(',')))
        # print(variable, method, nums)
        if method == 'set':
            i,x = nums
            i -= 1
            if type(variables[variable]) == type(list()):   # изначальный массив
                variables[variable][i] = x
            else:   # подмассив, но меняем в оригинальном массиве
                variables[variables[variable][ORIG_VARIABLE]][i+variables[variable][START]-1] = x
        elif method == 'get':
            i = nums[0]
            i -= 1
            if type(variables[variable]) == type(list()):  # изначальный массив
                print(variables[variable][i])
            else:  # подмассив, но обращаемся к оригинальному массиву
                print(variables[variables[variable][ORIG_VARIABLE]][i + variables[variable][START] - 1])
        elif method == 'add' and type(variables[variable]) == type(list()):
            x = nums[0]
            variables[variable].append(x)



# 10
# List a = new List(2,3,5)
# List b = a.subList(2,3)
# b.set(1, 10)
# b.get(1)
# a.get(2)
# List c = b.subList(2,2)

# 12
# List a = new List(2,3,5)
# List b = a.subList(2,3)
# b.set(1, 10)
# b.get(1)
# a.get(2)
# List c = b.subList(2,2)
# c.get(1)
# c.get(1)
# c.set(1,100)
# a.get(3)
# b.get(2)
# c.get(1)