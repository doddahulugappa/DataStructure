def task1_furthest_distance(list1, start_point):
    left = list1[:start_point]
    right = list1[start_point:]
    l_dist = 0
    r_dist = 0
    original = start_point
    for i in reversed(left):
        if i < list1[start_point]:
            start_point -= 1
            l_dist += 1
        else:
            break
    start_point = original
    for j in right[1:]:
        if j < list1[start_point]:
            start_point += 1
            r_dist += 1
        else:
            break
    return max([l_dist, r_dist])


def task2_find_best_start_point(list1):
    furthest_distance = {}
    for i in range(1, len(list1)):
        start_point = i
        copy_start_point = i
        left = list1[:start_point]
        right = list1[start_point:]
        l_dist = 0
        r_dist = 0
        for k in reversed(left):
            if k < list1[start_point]:
                start_point -= 1
                l_dist += 1
            else:
                break
        start_point = copy_start_point
        for j in right[1:]:
            if j < list1[start_point]:
                start_point += 1
                r_dist += 1
            else:
                break
        max_distance = max([l_dist, r_dist])
        furthest_distance[start_point] = max_distance
    max_value = max(furthest_distance.values())
    filtered_dict = {key: value for key, value in furthest_distance.items() if value == max_value}
    return min(filtered_dict.keys())


list2 = [0, 1, 2, 2, 4, 3, 3, 7, 7, 6, 6, 3, 3, 0]
print(task1_furthest_distance(list2, 1), 1)
print(task1_furthest_distance(list2, 4), 4)
print(task1_furthest_distance(list2, 2), 2)
print(task1_furthest_distance(list2, 3), 3)
print(task1_furthest_distance(list2, 5), 5)
print(task1_furthest_distance(list2, 6), 6)
print(task1_furthest_distance(list2, 7), 7)
print(task1_furthest_distance(list2, 8), 8)
print(task1_furthest_distance(list2, 9), 9)
print(task1_furthest_distance(list2, 10), 10)
print(task1_furthest_distance(list2, 11), 11)
print(task1_furthest_distance(list2, 12), 12)
print("="*100)
print(task2_find_best_start_point(list2))
