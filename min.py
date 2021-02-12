def minNumb (list):
    min = list[0]
    for i in list[1:]:
        if i < min:
            min = i
    return(min)

print(minNumb([1, -2, 4, -5, 10, -3, 15]))
