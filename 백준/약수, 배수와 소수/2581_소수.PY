# 자연수 M과 N이 주어질 때 M이상 N이하의 자연수 중 소수인 것을 모두 골라 이들 소수의 합과 최솟값을 찾는 프로그램

m = int(input())
n = int(input())

divisor_list = []

for i in range(m, n+1): 
    if i > 1:
        error = 0
        for j in range(2, i):
            if i%j == 0:
                error += 1
            if error > 1:   
                break
        if error == 0:
            divisor_list.append(i)
if len(divisor_list) > 0:
    print(sum(divisor_list))
    print(min(divisor_list))
else:
    print(-1)