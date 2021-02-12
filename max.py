def maxNumb (list):
    max = list[0]
    for i in list[1:]:
        if i > max:
            max = i
    return(max)

print(maxNumb([3, -2, 5, -7, 10]))
