def can_brick_pass(A, B, C, D, E):
    brick = sorted([A, B, C])
    hole = sorted([D, E])


    if brick[0] <= hole[0] and brick[1] <= hole[1]:
        return "YES"
    return "NO"


A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())


print(can_brick_pass(A, B, C, D, E))
