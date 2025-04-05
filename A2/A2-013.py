kaimuk = {'H':5,'O':3,'J':2}
tea = {'R1':12,'R2':18,'R3':25,'T1':15,'T2':20,'T3':30,'M1':10,'M2':15,'M3':20}

k,v = input().split()
v = int(v)

a,b,c = input().split()
a += b
c = int(c)

print(kaimuk[k]*v+tea[a]*c)