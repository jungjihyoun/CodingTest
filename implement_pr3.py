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

#북 = 0 , 동 = 1 , 남 = 2, 서 = 3 방향 정의
dx = [-1,0,1,0]
dy = [0,1,0,-1]


count = 1
turn_time = 0
while True:
    left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    #회전한 이후 정면에 가보지 않은 칸이 존재하는 경우 이동
    if (array[nx][ny] == 0 and check[nx][ny] == False ):
        x = nx
        y = ny
        check[nx][ny] = True
        count += 1
        turn_time +=1
        continue
    else:
        turn_time += 1

    #네 방향 모두 갈 수 없는 경우
    if turn_time == 4:
        nx = x-dx[direction]
        ny = y - dy[direction]
        #뒤로 갈 수 있다면 뒤로 이동
        if array[nx][ny] == 0:
            x = nx
            y = ny
            count += 1
        #뒤에가 바다로 막혀 있는 경우
        else:
            break

        turn_time = 0

print(count)





