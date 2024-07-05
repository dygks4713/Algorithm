n, k = map(int, input().split())

stack = 0

for i in range(n):
    if n%(i+1) == 0:
        stack += 1
    if stack == k:
        print(i+1)
        break

if stack < k:
    print(0)