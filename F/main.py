a, b, c, d = list(map(int, input().split()))


def optimal_param(length1, width1, length2, width2):
    min_l = float("inf")
    min_w = float("inf")
    for i in [[length1, length2, width1, width2], [length1, width2, width1, length2],
              [width1, length2, length1, width2], [width1, width2, length1, length2]]:
        len_stola = max(i[0], i[1])
        width = i[2] + i[3]
        if min_l * min_w > len_stola * width:
            min_l = len_stola
            min_w = width
    return min_l, min_w


print(*optimal_param(a, b, c, d))
