# Сначала преобразуем инфиксную запись выражения (стандартный вид) в постфиксную (как это длается см. тут https://www.youtube.com/live/km0E_i8Dtso?si=8GpeQOlFx-FxQYT_&t=1568) с помощью стека
# Далее инфиксную запись преобразуем в дерево в след. порядке:
# Используется стек, но в него мы будем класть не значения, а узлы будущего дерева.
# Читаем выражение (постфиксная запись) слева направо.
# 1) Если встретили переменную (операнд): создаем узел-лист (например, с значением a, b, x, y...) и помещаем его в стек.
# 2) Если встретили оператор (например, +, -, *, ^, /):
# Извлекаем из стека два верхних элемента. Важно: первый извлеченный элемент становится правым потомком, второй — левым.
# Создаем новый узел, где значением является оператор, а левым и правым потомками — извлеченные узлы.
# Помещаем этот новый узел обратно в стек.
# 3) Повторяем шаги, пока не прочитаем все выражение.
# 4) В конце в стеке останется ровно один элемент — это корень всего дерева разбора.
# Дерево построено, но самое сложное его вывести. Для этого будем обходить рекурсивно дерево (сначала в левый узел) и для каждого поддерева рисовать
# его на холсте (массив массивов состоящий из одиночных символов). Нарисовали поддерево вернулись на уровень выше
# при этом запоминая координаты узла (переменной или оператора).
# Далее возвращаем из правого поддерева его холст и координаты узла. А потом просто совмещаем 2 поддерева:
# 1) Для обоих поддеревьев расширяем холст на 2 вверх и прописываем ветвь вверх от узла (вертикальная черта и точка).
# 2) Для левого поддерева откладываем ветвь вправо от точки до конца холста (включительно)
# 3) Для правого поддерева откладываем ветвь влево от точки до начала холста (включительно)
# 4) Далее объединяем массивы наших поддеревьем: left_tree + '-[S]-' + right_tree   (объединение - приписываем справа один массив к другому)
# где S - это узел (переменная или оператор), а его координаты будут равны: y=0 x=len(left_tree[0])-1 + 3
# При объединении мы к левому поддереву добавляем узел (центральная часть) и правое поддерево, но надо понимать,
# что высота левого и правого поддеревьев отличается, поэтому подгоняем оба массива до максимального размера (max_h) - заполняем пробелами
# После полного обхода получаем холст с полным деревом
import sys
sys.setrecursionlimit(10**6)

def infix_to_postfix(s):    # преобразуем инфиксную запись выражения (стандартный вид) в постфиксную
    stack = []
    ans = []
    priorities = {'+':1, '-':1, '*':2, '/':2, '^':3}
    for sym in s:
        if sym == '(':  # кладем в стек
            stack.append('(')
        elif sym in ['+', '-', '*', '/']:   # операция выталкивает в ответ все операции из стека с большим или равным приоритетом и кладется в стек
            sym_prioriti = priorities[sym]
            while stack and stack[-1] in priorities and priorities[stack[-1]] >= sym_prioriti: # выталкивает приоритеты >= sym_prioriti
                ans.append(stack.pop())
            stack.append(sym)
        elif sym == '^':    # степень - правоассоциативна -> выталкивает в ответ все операции из стека с большим приоритетом и кладется в стек
            sym_prioriti = priorities[sym]
            while stack and stack[-1] in priorities and priorities[stack[-1]] > sym_prioriti:
                ans.append(stack.pop())
            stack.append(sym)
        elif sym == ')':    # закрывающая скобка выталкивает в ответ все операции до открывающей скобки
            while stack[-1] != '(':
                ans.append(stack.pop())
            stack.pop()
        else:   # операнд (строчная англ. буква) - сразу в ответ
            ans.append(sym)
    while stack:
        ans.append(stack.pop())
    return ans

class node():
    def __init__(self, sym, right_child=None, left_child=None):
        self.sym = sym
        self.right_child = right_child
        self.left_child = left_child

def get_print_tree(root):   # получаем холст (массив массивов) с деревом, рекурсивно его обходя
    def insert_offshoot(canvas_tree, x_node, direction_offshoot):  # рисует ответвление (хвостик) над левым и правым поддеревьями
        canvas_tree.insert(0, [' '] * len(canvas_tree[0]))
        canvas_tree.insert(0, [' '] * len(canvas_tree[0]))
        canvas_tree[0][x_node] = '.'
        canvas_tree[1][x_node] = '|'
        x_node += direction_offshoot
        while x_node >= 0 and x_node < len(canvas_tree[0]):
            canvas_tree[0][x_node] = '-'
            x_node += direction_offshoot

    if not root.sym in ['+', '-', '*', '/', '^']:   # значит тут буква (переменная) --> лист дерева
        return [[root.sym]], 0           # возвращаем холст с переменной и координату по иксу (указывающую на узел на холсте)

    canvas_left_tree, x_node_left_tree = get_print_tree(root.left_child)
    canvas_right_tree, x_node_right_tree = get_print_tree(root.right_child)

    insert_offshoot(canvas_left_tree, x_node_left_tree, 1)   # рисует ответвление (хвостик) над левым поддеревом
    insert_offshoot(canvas_right_tree, x_node_right_tree, -1)  # рисует ответвление (хвостик) над правым поддеревом

    max_height = max(len(canvas_right_tree), len(canvas_left_tree))
    while len(canvas_left_tree) < max_height:  # добавляем недостающие строки, чтобы выравнять высоты
        canvas_left_tree.append([' '] * len(canvas_left_tree[0]))
    while len(canvas_right_tree) < max_height:
        canvas_right_tree.append([' '] * len(canvas_right_tree[0]))

    mid_node = [[' ']*5 for _ in range(max_height)]
    mid_node[0] = ['-', '[', root.sym, ']', '-']
    x_new_node = len(canvas_left_tree[0])-1 + 3     # координата нового узла на холсте

    for h in range(max_height):  # склеиваем полученные массивы
        canvas_left_tree[h] += mid_node[h]
        canvas_left_tree[h] += canvas_right_tree[h]

    return canvas_left_tree, x_new_node

def postfix_to_tree(postfix):
    stack = []
    for sym in postfix:
        if sym in ['+', '-', '*', '/', '^']:
            new_node_operator = node(sym, right_child=stack.pop(), left_child=stack.pop())
            stack.append(new_node_operator)
        else:   # операнд (строчная англ. буква) - сразу в стек
            stack.append(node(sym))
    return stack[0] # ссылка на корень

s = input()
postfix = infix_to_postfix(s)
root = postfix_to_tree(postfix) # остался ровно один элемент
tree_for_print = get_print_tree(root)[0]
for line in tree_for_print:

    print(*line, sep='')
