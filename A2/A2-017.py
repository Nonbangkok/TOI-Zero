noodles = {'SR':60,'ST':80,'MR':80,'MT':100,'LR':100,'LT':120}
toppings = {'P':15,'E':10}

a,b = input().split()
c = input()

print(noodles[a+b] + (int(c[1:])*toppings[c[0]] if c[0] != 'N' else 0))