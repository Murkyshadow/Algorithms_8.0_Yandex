# 5:15 - 5:35
# Решать будем серез сортировку событий. Будет 2 события:
# 1) конец рейса
# 2) начало рейса
# в каждом событии храним время события, тип события и где мы сейчас находимся
# (если начало, то от куда едем, если конец, то куда приехали: A или В)
# далее отсортируем их по времени и идем считая свободные автобусы у каждого офиса: начался рейс, то смотрим есть ли
# у данного офиса свободные автобусы, если нет, то прибавляем 1 к свободным автобусам данного офиса и отправляем его
# в рейс (-1 от свободных автобусов), если были свободные автобусы, то просто отправляем его в рейс (-1),
# если рейс закончился, то прибавляем +1 к свободным автобусам данного офиса, в конечном итоге все автобусы станут
# свободными (закончат рейсы), ответ равен сумме свободных автобусов

def create_events(num_times, start_office, end_office): # создаем ивенты начала / конца рейсов
    for i in range(num_times):  # Обрабатываем расписание из офиса A
        st, end = map(time_to_minute, input().split('-'))
        events.append([st, START, start_office])  # TIME, TYPE_EVENT, WHERE bus
        events.append([end, END, end_office])

events = []
time_to_minute = lambda t: int(t.split(':')[0])*60 + int(t.split(':')[1])
END, START = 0, 1
create_events(int(input()), start_office='A', end_office='B')
create_events(int(input()), start_office='B', end_office='A')
count_free_bus = {'A':0, 'B':0}  # считаем кол-во автобусов в офисах А и В на текущий момент
for time, type, where_bus in sorted(events):
    if type == START:
        if count_free_bus[where_bus] == 0:   # не хватает автобусов - нужно больше автобусов
            count_free_bus[where_bus] += 1
        count_free_bus[where_bus] -= 1   # отправился автобус
    else:   # приехал
        count_free_bus[where_bus] += 1

print(count_free_bus['A'] + count_free_bus['B'])
