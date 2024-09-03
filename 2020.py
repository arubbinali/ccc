"""
#1
S = int(input())
M = int(input())
L = int(input())
hapiness = 1 * S + 2 * M + 3 * L
if hapiness >= 10:
    print("happy")
else:
    print("sad")

#2
P = int(input())#10
N = int(input())#2
R = int(input())#1
sum = 0
check = True
iterations = 0
while True:
    N = N * R
    sum += N
    iterations += 1
    if sum >= P:
        break
print(iterations)

#3
number_of_drops = int(input())
x_coordinates = []
y_coordinates = []
for _ in range(number_of_drops):
    coordinates = input()
    index_of_comma = coordinates.index(",")
    x_coordinate = coordinates[: index_of_comma]
    y_coordinate = coordinates[index_of_comma + 1 :]
    x_coordinate = int(x_coordinate)
    y_coordinate = int(y_coordinate)
    x_coordinates.append(x_coordinate)
    y_coordinates.append(y_coordinate)

x_bottom = min(x_coordinates)
y_bottom = min(y_coordinates)
x_top = max(x_coordinates)
y_top = max(y_coordinates)

print(f"{x_bottom - 1}, {y_bottom - 1}\n{x_top + 1}, {y_top + 1}")
"""








