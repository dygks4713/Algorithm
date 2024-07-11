x_1, y_1 = map(int, input().split())
x_2, y_2 = map(int, input().split())
x_3, y_3 = map(int, input().split())

result_x, result_y = 0, 0
if x_1 == x_2:
    result_x = x_3
elif x_1 == x_3:
    result_x = x_2
else:
    result_x = x_1

if y_1 == y_2:
    result_y = y_3
elif y_1 == y_3:
    result_y = y_2
else:
    result_y = y_1

print(result_x, result_y)