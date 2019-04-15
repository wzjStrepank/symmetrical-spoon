demo_dict = {"a": 1, "b": 3, "d": 6, "e": 3, "f": 2, "c": 5}
dict_list = list(demo_dict.items())

a = sorted(dict_list,key=lambda x: x[1])
print(a)

# 冒泡排序
def bubble_sort(target_list):
    for i in range(len(target_list)-1,0,-1):
        for j in range(i):
            if target_list[j][1] > target_list[j+1][1]:
                target_list[j], target_list[j+1] = target_list[j+1], target_list[j]
    return target_list


print(bubble_sort(dict_list))

# 选择排序
def choose_sort(target_list):
    for i in range(len(target_list)-1,0,-1):
        max_index = i
        for j in range(i+1):
            if target_list[j][1] > target_list[max_index][1]:
                max_index = j
            target_list[i], target_list[max_index] = target_list[max_index], target_list[i]
    return target_list


print(choose_sort(dict_list))