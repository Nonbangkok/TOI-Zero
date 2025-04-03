def calculate_tax(year,cc):
    if year <= 1990:
        if cc <= 1500:
            return 1250
        elif cc <= 2000:
            return 1400
        else:
            return 2000
    elif 1991 <= year <= 1999:
        if cc <= 1500:
            return 1100
        elif cc <= 2000:
            return 1300
        else:
            return 1700
    else:
        if cc <= 1500:
            return 1000
        elif cc <= 2000:
            return 1200
        else:
            return 1500

year,cc = int(input()),int(input())
print(calculate_tax(year,cc))