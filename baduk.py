# baduk = [[0 for col in range(19)] for row in range(19)]
# num = int(input())
#
# for i in range(0,19):
#     for j in range(0,19):
#         baduk[i][j] = 0
#
# for i in range(num):
#     r,c = input().split()
#     r = int(r)
#     c = int(c)
#     baduk[r-1][c-1] = 1
#
# for i in range(19):
#     for j in range(19):
#         print(baduk[i][j],end = " ")
#     print()
#

#answer
m = []
for i in range(20):
    m.append([])
    for j in range(20):
        m[i].append(0)

print("test:" , m)

n = int(input())
for i in range(n):
    x, y = input().split()
    m[int(x)][int(y)] = 1

for i in range(1, 20):
    for j in range(1, 20):
        print(m[i][j], end=' ')
    print()