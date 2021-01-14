################### 구현 게임 개발 #####################

n , m = map(int,input().split())

check = [[False]* m for _ in range(n)]
x , y , direction  = map(int,input().split())
check[x][y] = True

array = []
for i in range(n):
    array.append(list(map(int,input().split())))

#왼쪽 회전
def left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3


# check = []
# fin = True
# while True:
#     # 북쪽으로 이동하는 경우 . 위에가 바다인지 아닌지
#     if (d == 0):
#         if (load[sx][sy - 1] == 1):
#             d = 3
#             continue
#         sy = sy + dy[2]
#         continue
#     elif (d == 3):
#         if (load[sx - 1][sy] == 1):
#             d = 2
#             continue
#         sx = sx + dx[2]
#         continue
#
#
#
#

