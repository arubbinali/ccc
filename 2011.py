"""
#1
antenna = int(input("How many antennas?   "))
eyes = int(input("How many eyes?   "))
if antenna >= 3 and eyes <= 4:
    print("TroyMartian")
if antenna <= 6 and eyes >= 2:
    print("VladSaturnian")
if antenna <= 2 and eyes <= 3:
    print("GraemeMercurian")

#2
h = int(input())
M = int(input())
t = 0
for x in range(10):
    t += 1
    A = -6*t**4 + h*t**3 + 2*t**2 + t
    if A <= 0:
        break
if t < M:
    print("The balloon first touches ground at hour:")
    print(t)
else:
    print("The balloon does not touch ground in the given time.")
"""