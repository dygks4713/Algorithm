n, b = map(int, input().split())


num_list = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

tmp = ''
while n:
    tmp = num_list[n%b] + tmp
    n = n//b

print(tmp)