import sys

#리스트 컴프리헨션 사용하여 2차원 배열 생성
line = [[0]*10 for _ in range(10)]


for i in range(10):
    #user = input().split()  #split는 공백 #줄바꿈 일 때는 input 여러번
    #sys라이브러리 사용하여 입력을 더 빠르게 받는다
    user = sys.stdin.readline().rstrip().split()
    line[i] = list(map(int,user))

#1이 나올때까지 오른쪽으로 간다
#1이 나오면 밑으로 내려간다. - 오른쪽 길이 나오면 다시 오른쪽, 아님 아래
# 먹이(2)가 나오면 즉시 중단
# 오른쪽 아래 모두 1이면 중단
#1.1 에서 시작

x = 1
y = 1



# while True:
#     if line[x][y]==0 :
#         line[x][y] = 9
#     elif line[x][y]==2 :
#         line[x][y] = 9
#         break
#     if((line[x][y] == 1 and line[x+1][y] ==1) or (x == 9 and y == 9)):
#         break
#     if(line[x][y+1] != 1 ):  # move forward
#         y +=1
#     elif(line[x+1][y] != 1): # move to down
#         x += 1

found = True
index = 1
while found == True:
    for i in range(index,9):
        if line[index][i] == 0:
            line[index][i] = 9
        #범위 설정 잘해야

        if(line[index][i+1] == 2):
            print("먹었습니다! ")
            found = False
            break

        elif (line[index][i+1] != 1):   #오른쪽으로 이동
            line[index][i+1] = 9

        elif (line[index][i+1] == 1):    #아래쪽으로 이동
            if (line[index+1][i] == 1):
                print("game over")
                found = False
                break
            line[index+1][i] = 9
            index += 1

for i in range(10):
    for j in range(10):
        print(line[i][j], end=' ')
    print()