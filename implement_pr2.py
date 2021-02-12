#############왕실의 나이트#####################
#이동할 방향이 한정되어 있다면 미리 리스트로 정의하자
#아스킬 코드가 나온다면 ord 를 사용하여 숫자로

input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1

#나이트가 이동할 수 있는 방향
steps = [(-2,-1),(-2,1),(-1,2),(-1,-2),(1,-2),(1,2),(2,-1),(2,1)]

result = 0
for step in steps:
    next_row = row + step[0]
    next_col = column+ step[1]

    if next_row >= 1 and next_col <= 8 and next_col >= 1 and next_col <= 8:
        result += 1
print(result)

