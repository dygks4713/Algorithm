a, b, v = map(int, input().split())

# 올라 가야할 거리 = v - b
# 하루에 올라갈 수 있는 거리 = a - b

if (v-b)%(a-b) == 0:
    print((v-b)//(a-b))
else:
    print((v-b)//(a-b)+1)