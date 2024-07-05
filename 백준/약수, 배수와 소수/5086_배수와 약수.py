a, b = 1, 1
while a == 1 and b == 1:
    input_a, input_b = map(int, input().split())
    if input_a > input_b:
        if input_a % input_b == 0: 
            print("multiple") # 첫 번째 숫자가 두 번째 숫자의 약수라면 multiple
        else: 
            print("neither") # 해당 안되면 neither
    
    if input_a < input_b:
        if input_b % input_a == 0: 
            print("factor") # 첫 번째 숫자가 두 번째 숫자의 약수라면 facto
        else:
            print("neither") # 해당 안되면 neither
    if input_a == 0 and input_b == 0:
        break
    