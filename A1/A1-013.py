def solve(password = ["H","4567"]):
    char,digit = input(),input()
    if char != password[0] and digit != password[1]:
        return "safe locked"
    elif char != password[0]:
        return "safe locked - change char"
    elif digit != password[1]:
        return "safe locked - change digit"
    return "safe unlocked"

print(solve())