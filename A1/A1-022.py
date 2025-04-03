def get_zodiac_sign(day,month):
    zodiac_dates = [
        (20,1,"aquarius"),(19,2,"pisces"),(21,3,"aries"),(20,4,"taurus"),
        (21,5,"gemini"),(22,6,"cancer"),(23,7,"leo"),(23,8,"virgo"),
        (23,9,"libra"),(24,10,"scorpio"),(22,11,"sagittarius"),(22,12,"capricorn")
    ]
    
    for start_day,start_month,sign in zodiac_dates:
        if (month == start_month and day >= start_day) or (month == start_month % 12 + 1 and day < start_day):
            return sign

day,month = int(input()),int(input())
print(get_zodiac_sign(day,month))