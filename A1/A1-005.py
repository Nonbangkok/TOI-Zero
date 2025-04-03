seasons = ["winter","spring","summer","fall"]
m,d = int(input()),int(input())

if m % 3 == 0 and d >= 21:
    print(seasons[m//3])
else:
    print(seasons[m//3-(m%3==0)])