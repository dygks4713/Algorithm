a = int(input())
b = int(input())
c = int(input())

mul = a*b*c
mul_list = []

for i in str(mul): # 입력된 숫자를 문자열로 변환후, 자리수별로 분리
    mul_list.append(i)

result = [0]*10 # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0] 생성

passing = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in range(len(mul_list)):
    result[passing.index(int(mul_list[i]))] += 1 # result에 각 해당하는 자리수에 1 더함

for i in range(len(result)):
    print(result[i])