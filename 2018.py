"""
#1
d1 = int(input())
d2 = int(input())
d3 = int(input())
d4 = int(input())
if (d1 == 8 or d1 == 9) and (d4 == 8 or d1 == 4) and (d2 == d3):
    print("ignore")
else:
    print("answer")

#2
N = int(input())
yesterday = input()        #CC..C
today = input()            #.CC..
count = 0
for check in range(N):
    if (yesterday[check] == today[check]) and yesterday[check] == "C":
        count += 1
print(count)

#3
distances_input = input() #       3 10 12 5
distances = [int(_) for _ in distances_input.split()]

city_1 = [0, 0, 0, 0, 0]
city_2 = [0, 0, 0, 0, 0]
city_3 = [0, 0, 0, 0, 0]
city_4 = [0, 0, 0, 0, 0]
city_5 = [0, 0, 0, 0, 0]

for _ in range(1, 5):
    city_1[_] = city_1[_ -1] + distances[_-1]

#second city
for _ in range(5):
    if _ != 1:
        if _ == 0:
            city_2[_] = distances[_]
        else:
            city_2[_] = city_2[_ -1] + distances[_ -1]

#third city
for _ in range(5):
    if _ > 2:
        if _ == 0:
            city_3[_] = distances[_]
        else:
            city_3[_] = city_3[_ -1] + distances[_ -1]
for _ in range(1, -1, -1):
    city_3[_] = city_3[_ + 1] + distances[_]

#fourth city
for _ in range(5):
    if _ > 3:
        if _ == 0:
            city_4[_] = distances[_]
        else:
            city_4[_] = city_4[_ -1] + distances[_ -1]
for _ in range(2, -1, -1):
    city_4[_] = city_4[_ + 1] + distances[_]

#fifth city
for _ in range(3,-1, -1):
    city_5[_] = city_5[_ + 1] + distances[_]

#outputs
for element in city_1:
    print(element, end = " ")
print()
for element in city_2:
    print(element, end = " ")
print()
for element in city_3:
    print(element, end = " ")
print()
for element in city_4:
    print(element, end = " ")
print()
for element in city_5:
    print(element, end = " ")
"""
#3 Redone using AI
distances = list(map(int, input().split()))
city_distances = [[0] * 5 for _ in range(5)]

for i in range(5):
    total_distance = 0
    for j in range(i, 5):
        if i == j:
            city_distances[i][j] = 0
        else:
            total_distance += distances[j-1]
            city_distances[i][j] = total_distance
            city_distances[j][i] = total_distance

# Print the distance table
for row in city_distances:
    print(' '.join(map(str, row)))








