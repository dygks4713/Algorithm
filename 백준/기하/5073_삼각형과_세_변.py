# 각 입력에 맞는 결과 (Equilateral, Isosceles, Scalene, Invalid) 를 출력
while 1:
    line_list = list(map(int, input().split())) # 3개 입력
    a, b, c = sorted(line_list, reverse=True) # 내림차순으로 정렬후 반환

    if a == 0 and b == 0 and c == 0:    # 0 3개 입력: 종료
        break

    elif a >= b + c: # 세 변의 길이가 삼각형의 조건을 만족하지 못하는 경우에는 "Invalid" 를 출력
        # 가장 긴 변의 길이보다 나머지 두 변의 길이의 합이 길지 않으면 삼각형의 조건을 만족하지 못한다.
        print("Invalid")

    elif a == b == c:                   # Equilateral :  세 변의 길이가 모두 같은 경우
        print("Equilateral")

    elif a == b or a == c or b == c:    # Isosceles : 두 변의 길이만 같은 경우
        print("Isosceles")
    else:                               # Scalene : 세 변의 길이가 모두 다른 경우
        print("Scalene")