

def repl(string):
    result = ""
    for i in string:
        if i == "e":
            i = "E"
        result = result + i
    return result

print(repl("Your ancestors knew death in ways you never will"))




