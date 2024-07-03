# 입력 색종이 
paper_n = int(input())

# 100x100 도화지 만들기
paper = [[0]*100 for _ in range(100)] 

for _ in range(paper_n):
		# 좌표 입력
    x, y = map(int, input().split())
    # 해당 좌표에 1을 찍어줌
    for i in range(x, x+10):
        for j in range(y, y+10):
            paper[i][j] = 1

result_sum = 0
# 1이 찍힌 점들의 합
for i in range(100):
    result_sum += sum(paper[i])

print(result_sum)