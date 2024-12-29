int1 = int(input())
int2 = int(input())
k1 = int(input())
k2 = int(input())
min1 = k1 + int1 * (k1 - 1)
max1 = k1 + int1 * (k1 + 1)
min2 = k2 + int2 * (k2 - 1)
max2 = k2 + int2 * (k2 + 1)
if max1 > max2:
    tmax = max2
else:
    tmax = max1
if min1 > min2:
    tmin = min1
else:
    tmin = min2
if tmin > tmax:
    print(-1)
else:
    print(tmin, tmax)