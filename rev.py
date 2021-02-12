def rev (list):
    s = len(list)
    new_list = [None]*s

    for i in list:
        s = s - 1
        new_list[s] = i
    return new_list

print(rev([-1, 2, -3, 4, -5]))
