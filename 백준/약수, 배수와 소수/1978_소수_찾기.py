n = int(input())
input_list = list(map(int, input().split())) # 리스트로 여러개 입력
result = 0
for i in input_list:
    divisor = []
    for j in range(1, i+1):
        if i%j == 0: # 약수 구하기
            divisor.append(j) # 구한 약수를 divisor에 추가
    if len(divisor) == 2: # 약수가 2개면 소수
        result += 1
print(result)