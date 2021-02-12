################### 숫자 카드 게임 #######################
### 굳이 minlist를 만들지 말아야 함 .
### 그냥 한 줄씩 생성할 때 바로 최소 값을 저장해 두고 그 다음 행의 최소값과 비교를 해서 max를 업데이트 시키자!!
# 1 . 행렬 만들기
n , m = map(int,input().split())
matrix = []

for i in range(n):
    matrix.append(0)
    user = list(map(int, input().split()))
    matrix[i] = user

# 2 . N(행)을 고른 후 가장 작은 수 뽑는데, 최종적으로 가장 높은 숫자를 뽑아야 함 최소값을 비교해서
min_list = []

for i in range(n):
    min = matrix[i][0]
    for j in range(m):
        if ( min > matrix[i][j]):
            min = matrix[i][j]
    min_list.append(min)

result = min_list[0]
for i in min_list:
    if ( min_list[0] < i):
        result = i

print(result)


############# 예시답안 : min() 함수를 이용하여 #######################
result = 0
for i in range(n):
    data = list(map(int,input().split()))
    #현재 줄에서 가장 작은 수 찾기
    min_value = min(data)
    #가장 작은 수 중에서 큰 수 찾기 (전 행의 result(max)값과 현재 행의 최소 값을 비교)
    result = max(result,min_value)

print(result)


############ 예시답안 : 2중 반복문 구조 #############################

for i in range(n):
    data = list(map(int,input().split()))
    #현재 줄에서 가장 작은 수 찾기
    min_value = 10001
    for a in data:
        min_value = min(min_value,a)
    result = max(result, min_value)
print(result)





