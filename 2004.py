"""
#1
import math
n = int(input())
answer = 1
answer ** 2
for answer in n:
    answer **= 2
print(answer)

#2
current_year = int(input("Enter the current year:\n"))
future_year = int(input("Enter a future year:\n"))

print("All positions change in year", current_year)
while current_year < future_year:
    current_year += 60
if current_year > future_year:
        current_year -= 60
print("All positions change in year", current_year)
"""