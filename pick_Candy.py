h = 0
w = 0
h,w = input("배열의 높이와 너비").split()
h = int(h)
w = int(w)
xy = []
#좌표생성
for i in range(h):
    xy.append([])
    for j in range(w):
        xy[i].append(0)


n = 0 # 막대의 개수
n = int(input("막대의 개수를 입력하시오"))

l = 0 #막대의 길이
d = 0 #세로 가로
x = 0
y = 0

while n:
    l = int(input("1. 막대의 길이를 입력하시오"))

    while (l > w  or l > h):
        l = int(input("막대의 길이를 재입력 하시오"))

    d = int(input("2. 가로또는 세로를 지정하시오 0:가로 1:세로"))
    while( (d!=0 and d!=1)==1):
        d = int(input("0또는 1을 입력하시오"))

    x = int(input("3. x좌표를 입력하시오"))-1
    while x<1 or x > 100-h :
        x = int(input("x좌표를 재입력하시오"))-1

    y = int(input("4. y좌표를 입력하시오"))-1
    while y<1 or y>100-h:
        y = int(input("y좌표를 재입력하시오"))-1


    for i in range(l):
        if(d == 0):  #가로
            xy[x][y+i] = 1

        elif ( d== 1):
            xy[x+i][y] = 1

    for i in range(h):
        for j in range(w):
            print(xy[i][j] , end='')
        print()







