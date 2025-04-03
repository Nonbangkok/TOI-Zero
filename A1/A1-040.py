calories = [100,120,200,60]
print(f"Bye Bye \nTotal Calories: {sum(calories[n-1] for n in iter(lambda:int(input()),5))}")