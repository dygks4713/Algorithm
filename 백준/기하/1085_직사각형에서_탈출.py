# 한수는 지금 (x, y)에 있다. 직사각형은 각 변이 좌표축에 평행하고, 
# 왼쪽 아래 꼭짓점은 (0, 0), 
# 오른쪽 위 꼭짓점은 (w, h)에 있다.
# 직사각형의 경계선까지 가는 거리의 최솟값을 구하라 

x, y, w, h = map(int, input().split()) # (x, y, w, h) 입력

x_result, y_result, result = 0, 0, 0 # x축 거리 결과, y축 거리 결과, 거리 최솟값 결과 

if (w - x) >= x : # x를 기준으로 오른쪽과 왼쪽의 거리 비교
    x_result = x
else:
    x_result = (w - x)

if (h - y) >= y : # y를 기준으로 위쪽과 아래쪽의 거리 비교
    y_result = y
else:
    y_result = (h - y)

if x_result >= y_result: # x, y 거리 비교
    print(y_result)
else:
    print(x_result)