import math
t = int(input())
room, floor = 0, 0
for _ in range(t):
    h, w, n = map(int, input().split())
    room = math.ceil(n/h)
    if n%h == 0:
        floor = h
    else:
        floor = n%h

    print(floor*100+room)