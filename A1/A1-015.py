name,sur,age = input(),input(),input()

if len(name) > 5 and len(sur) > 5:
    print(f"{name[:2]}{sur[-1]}{age[-1]}")
else:
    print(f"{name[0]}{age}{sur[-1]}")