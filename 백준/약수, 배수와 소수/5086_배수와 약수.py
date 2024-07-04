a, b = 1, 1
while a == 1 and b == 1:
    input_a, input_b = map(int, input().split())
    if input_a > input_b:
        if input_a % input_b == 0:
            print("multiple")
        else:
            print("neither")
    
    if input_a < input_b:
        if input_b % input_a == 0:
            print("factor")
        else:
            print("neither")
    if input_a == 0 and input_b == 0:
        break
    