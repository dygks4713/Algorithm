# f(n) = a1*n + a0, g(n) = n
# O(g(n)) = {f(n) | 모든 n ≥ n0에 대하여 f(n) ≤ c × g(n)인 양의 상수 c와 n0가 존재한다}
# O(n) 정의를 만족하려면 우선 f(n0) <= cg(n0)가 만족되어야 한다. 
# 또한 모든 n >= n0에 대해  f(n) <= cg(n)가 만족되어야 하므로 c는 무조건 a1보다 크거나 같아야 한다. 
# O(n) 정의를 만족하면 if (a1 * n0 + a0 <= c * n0) and (a1 <= c)

a1, a0 = map(int, input().split())
c = int(input())
n0 = int(input())

if (a1*n0 + a0) <= c*n0 and (a1 <= c):
    print(1)
else:
    print(0)