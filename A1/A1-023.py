number,unit = int(input()),input()

if unit == 'F':
    number = 5*(number-32)/9

if number >= 100:
    print("gas")
elif number > 0:
    print("liquid")
else:
    print("solid")