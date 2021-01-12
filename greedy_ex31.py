#거슬러 줘야 할 동전의 최소 개수를 구해라 / N은 항상 10의 배수이다

n = 0 #거슬러 줘야 할 돈
count = 0

n = int(input("거슬러 줘야 할 돈은 얼마인가요?"))

coin = [500,100,50,10]

for i in coin:
    count += n//i
    n %= i

print(count)