A = ['a','e','i','o','u']
a = input()

def chk():
    for i in A:
        if a == i:
            return "yes"
    return "no"

print(chk())