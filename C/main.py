def equal(first:str, second:str)-> str:
    for i in ["(", ")", "-"]:
        first = first.replace(i, "")
        second = second.replace(i,"")
    first = first.replace("+7","8")
    second = second.replace("+7","8")
    if len(first)<11:
        first = "8495" + first
    if len(second)<11:
        second = "8495" + second
    if first==second:
        return "YES"
    return "NO"
ex = input()
for i in range(3):
    number = input()
    print(equal(ex, number))
