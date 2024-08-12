# 첫째 줄에 입력의 크기 n(1 ≤ n ≤ 500,000)이 주어진다.
# 첫째 줄에 코드1 의 수행 횟수를 출력한다.
# 둘째 줄에 코드1의 수행 횟수를 다항식으로 나타내었을 때, 최고차항의 차수를 출력한다. 단, 다항식으로 나타낼 수 없거나 최고차항의 차수가 3보다 크면 4를 출력한다
# n = int(input())
# sum = 0
# sum_n = 0

# for i in range(1, n-2):
#     for j in range(i+1, n-1):
#         for k in range(j+1, n):
#             sum = (sum + (i * j * k))
#             sum_n = sum_n + 1
#             print(f'sum={sum}, i={i}, j={j}, k={k}, sum_n={sum_n}')
# print(f'최종 {sum}, sum_n={sum_n}')

# 입력 n = 7이면 수행횟수가 35이다. 
# 즉, 1부터 n까지 숫자중 3개의 숫자를 중복 없이, 크기순으로 작성하는 경우의 수가 수행 횟수가 됨
# 123, 124, 125 ... 456
# nC3 = (n!/(n-3)!*3!) = (n)(n-1)(n-2)/6

n = int(input())
print(n*(n-1)*(n-2)//6)
print(3)
