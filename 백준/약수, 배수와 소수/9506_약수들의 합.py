result = 0

while True:
    st = []
    n = int(input())
    if n == -1:
        break

    for i in range(1, n):
        if n%i == 0:
            st.append(i)
        
    if sum(st) == n:
        print(n, "=", end=" ")
        print(*st, sep="+") # 리스트나 튜플에 있는 요소를 함수에 개별 인자로 전달할 때 *를 사용
    else:
        print("%d is NOT perfect." %n)