def is_correct(a:int,b:int,c:int) -> str:
    if a+b+c- max(a,b,c) > max(a,b,c):
        return "Yes"
    else:
        return "No"
first = int(input())
second = int(input())
third = int(input())
print(is_correct(first,second,third))
