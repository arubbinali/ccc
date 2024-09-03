"""
#1
m1 = input()
m2 = input()
m3 = input()
m4 = input()
m5 = input()
m6 = input()
results = [m1, m2, m3, m4, m5, m6]
print(results)
wins = 0
lost = 0
for x in results:
    if x == "W":
        wins += 1
    if x == "L":
        lost += 1

if wins > 4:
    print("1")
elif wins > 2:
    print("2")
elif wins > 0:
    print("3")
else:
    print("-1")

#2
row1 = input()
row2 = input()
row3 = input()
row4 = input()

Row1 = list(row1.split(" "))
Row2 = list(row2.split(" "))
Row3 = list(row3.split(" "))
Row4 = list(row4.split(" "))

for x in range(len(Row1)):
    Row1[x] = int(Row1[x])
    Row2[x] = int(Row2[x])
    Row3[x] = int(Row3[x])
    Row4[x] = int(Row4[x])

row_sum1 = sum(Row1)
row_sum2 = sum(Row2)
row_sum3 = sum(Row3)
row_sum4 = sum(Row4)

column_sum1 = Row1[0] + Row2[0] + Row3[0] + Row4[0]
column_sum2 = Row1[1] + Row2[1] + Row3[1] + Row4[1]
column_sum3 = Row1[2] + Row2[2] + Row3[2] + Row4[2]
column_sum4 = Row1[3] + Row2[3] + Row3[3] + Row4[3]

if row_sum1 == column_sum1 and row_sum2 == column_sum2 and row_sum3 == column_sum3 and row_sum4 == column_sum3:
    print("magic")
else:
    print("not magic")
"""
#3
word = input()  #banana
count = 0
first = [elem for elem in word]
second = [word[elem] for elem in range(len(word) - 1, -1, -1)]

print(f"{first}\n{second}\n{count}")







