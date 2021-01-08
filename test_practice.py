baduk = [[0 for col in range(19)] for row in range(19)]
num = int(input())

for i in range(0,19):
    for j in range(0,19):
        baduk[i][j] = 0

for i in range(num):
    r,c = input().split()
    r = int(r)
    c = int(c)
    baduk[r-1][c-1] = 1

for i in range(19):
    for j in range(19):
        print(baduk[i][j],end = " ")
    print()

