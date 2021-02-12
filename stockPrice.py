def solution(prices):
    count = 0
    answer = []
    temp = 0

    for i in range(0, len(prices)):
        for j in range(i+1, len(prices)):
            if( prices[i] <= prices[j]):
                count = count + 1
        answer.append(count)
        count = 0


    print(answer)
    return answer

solution([1, 2 , 3 , 2,  3 ])