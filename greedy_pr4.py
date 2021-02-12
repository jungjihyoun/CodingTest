################ 1 이 될때까지 ##############################

n , k = map(int,input().split())

count = 0

while True:
    if( n % k == 0 and n != 1):
        n = n //k
        count += 1
    elif n%k != 0 and n != 1:
        n -= 1
        count += 1
    else:
        break
print(count)

############### 모범 답안 ?????????뭐징  ######################################
result = 0
while True:
    target = (n//k) * k
    result += (n - target)
    n = target

    if n < k:
        break
    #k로 나누기
    result += 1
    n //= k

#마지막으로 남은 수에 대하여 1씩 빼기
result += (n-1)
print(result)
