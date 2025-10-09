# 16:40 -

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