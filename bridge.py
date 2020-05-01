import sys

end_side = []
#modify to create starting conditions, integers only
start_side = [1, 2, 7, 10]
total_time = 0

def max_tuple(x: int, y: int):
    if x > y:
        return x
    else:
        return y

def get_min_list(side_list: list):
    min_time = side_list[0]
    for x in side_list[1:]:
        if x < min_time:
            min_time = x

    return min_time

def get_max_list_tuple(side_list: list):

    max_time_1 = side_list[0]
    max_time_2 = sys.maxsize

    for x in side_list[1:]:
        if x > max_time_1 and x < max_time_2:
            max_time_2 = x
        elif x > max_time_1:
            max_time_1 = x

    return max_time_1, max_time_2


def cross_bridge(start: list, end: list):
    global total_time
    if len(end_side) == 0:
        x = get_min_list(start)
        start.remove(x)
        y = get_min_list(start)
        start.remove(y)
        total_time += max_tuple(x, y)
        end.append(x)
        end.append(y)
    else:
        x, y = get_max_list_tuple(start)
        total_time += max_tuple(x, y)
        start.remove(x)
        start.remove(y)
        end.append(x)
        end.append(y)


def move_lamp_back(start: list, end: list):
    global total_time
    min_time = get_min_list(end_side)
    total_time += min_time
    end.remove(min_time)
    start.append(min_time)

#main loop
while True:
    print("\nStart side: " + str(start_side))
    print("End side: " + str(end_side) + "\n"
                                         "")
    if len(start_side) == 0:
        print("\nTOTAL TIME: " + str(total_time) + "\n")
        break
    else:
        cross_bridge(start_side, end_side)
        if len(start_side) != 0:
            move_lamp_back(start_side, end_side)
