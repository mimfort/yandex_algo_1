def sqrt_answer(a,b,c):

    if a ==0 and (b == c**2):
        return "MANY SOLUTIONS"
    elif c < 0 or a == 0:
        return "NO SOLUTION"
    res = (c**2 - b)/a
    if res%1==0:
        return int(res)
    else:
        return "NO SOLUTION"
a = int(input())
b = int(input())
c = int(input())
print(sqrt_answer(a,b,c))