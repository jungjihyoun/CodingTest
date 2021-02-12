
############### p.92 큰 수의 법칙#########################
### map , list 사용 개념


N = 0  #리스트의 개수
M = 0  #더해지는 횟수
K = 0  #연속 가능한 최대 횟수
num_list = []

N,M,K = map(int,(input().split()))
num_list = list(map(int , input().split()))
num_list.sort()
print(num_list)

result = 0
while True:
    for i in range(K):
        if M == 0 :
            break
        result += num_list[N-1]
        M -= 1
    if M == 0 :
        break
    result += num_list[N-2]
    M -= 1

print(result)


########### 입력값이 커지면 시간 초과 될 수 있다
########### 이럴 땐 반복되는 값에 집중한다. -> 수열을 찾을 수 있네 ?

print("수열로 파악하는 방법")

n, m , k = map(int,input().split())
data = list(map(int,input().split()))

data.sort()

first = data[n-1]
second = data[n-2]

count = int(m/(k+1))*k + m % (k+1)

result = 0
result += count * first
result += (m-count) * second

print(result)



