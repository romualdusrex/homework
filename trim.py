def trim(string):
    result = ""
    k = 0
    for i in string:
        if i == ' ':
            if k == 0:
                k += 1
            else:
                i = ""
        else:
            k = 0
        result = result + i
    return result
print(trim("Your ancestors   knew  death  in ways         you never    will"))