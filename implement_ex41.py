########### 구현 하기 ##################

n = int(input())
x,y = 1,1
plans = input().split()

#이동 방향을 리스트로 표현하고
dx = [0,0,-1,1]
dy = [-1,1,0,0]
move_types = ['L','R','U','D']

for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            #왼쪽 오른쪽 움직일 때 Y 계산
            #위 아래 움직일 때 X 계산
            nx = x + dx[i]
            ny = y + dy[i]
    if nx < 1 or ny <1 or nx > n or ny > n :
        continue
    x,y = nx, ny


################# 4-2 시간 ####################

h = int(input())
count = 0
for i in range(h+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                count += 1
print(count)