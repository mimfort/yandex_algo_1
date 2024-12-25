def vent(value, need_value, type):
    if type == "freeze":
        value = min(value, need_value)
    elif type == "heat":
        value = max(value, need_value)
    elif type == "auto":
        value = need_value
    return value
val, to_val = list(map(int,input().split()))
name = str(input())
print(vent(value=val, need_value=to_val, type=name))



