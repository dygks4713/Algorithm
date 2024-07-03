n = int(input())

line = 0  # 사선 라인
max_n = 0  # 입력된 숫자(input_num 변수)의 라인에서 숫자들의 합
while n > max_n:
    line += 1  
    max_n += line
    
gap = max_n - n # 해당 라인의 숫자들의 합 - 입력한 수(n)

if line % 2 == 0: # 짝수 라인
    top = line - gap
    under = gap + 1
else: # 홀수 라인
    top =  gap + 1
    under = line - gap

print(f'{top}/{under}')