# тут надо порисовать эти повороты и развороты и можно будет заметить, что любой сдиг в лево, в право, в низ, в верх занимает 3 движения
# так же первый угол (когда мы менем направления движения) занимает всего 1 действие
# и единственное, что остается обработать - это случаии когда стартовый x или y совпадает с финальным 
def solution():
    count_action = 0
    st_x, st_y = map(int, input().split(' '))
    end_x, end_y = map(int, input().split(' '))
    s_x = abs(st_x - end_x)
    s_y = abs(st_y - end_y)
    if s_x == 0 and s_y == 0:
        return 0
    elif s_x == 0:
        s_y -= 1
        return s_y * 3
    elif s_y == 0:
        s_x -= 1
        return s_x * 3

    s_y -= 1
    count_action += s_y * 3
    s_x -= 1
    count_action += 1
    count_action += s_x * 3
    return count_action


print(solution())
