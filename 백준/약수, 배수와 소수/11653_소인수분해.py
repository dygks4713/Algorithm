import sys
input = sys.stdin.readline

n = int(input())
for i in range(2, n+1): # 2부터 n까지 하나씩 나눠보기
    while n%i == 0: # i로 나눌 수 없을 때까지 나누기
        print(i)
        n /=i 
    if n==1:
        break