# 자연수 M과 N이 주어질 때 M이상 N이하의 자연수 중 소수인 것을 모두 골라 이들 소수의 합과 최솟값을 찾는 프로그램

m = int(input())
n = int(input())

divisor_list = []

for i in range(m, n+1): # m부터 n까지

    if i > 1: # 입력된 수가 자연수인지 판별
        error = 0

        for j in range(2, i): # 2부터 i-1까지
            if i%j == 0:    # 나눈 몫이 0이면 error 1개씩 추가
                error += 1
            if error > 1:   # 2부터 i-1까지 나눈 몫이 0이고 error가 1을 넘어서면 반복문 종료(소수 판별)
                break

        if error == 0:      # error가 없으면 소수 리스트(divisor_list)에 추가
            divisor_list.append(i)

if len(divisor_list) > 0:   
    print(sum(divisor_list)) # 소수들의 합
    print(min(divisor_list)) # 소수 리스트 최솟값
else:
    print(-1)   # 리스트 안에 없으면 -1 출력
    print()