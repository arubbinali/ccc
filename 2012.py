"""
#1
limit = int(input("Enter the speed limit:   "))
speed = int(input("Enter the recorded speed of the car:   "))
if speed > limit:
    over = speed - limit
    if over >= 1 and over <= 20:
        print("You are speeding and your fine is $100.")
    elif over >= 21 and over <= 30:
        print("You are speeding and your fine is $270.")
    else:
        print("You are speeding and your fine is $500.")
else:
    print("Congratulations, you are within the speed limit!")

#2
r1 = int(input())
r2 = int(input())
r3 = int(input())
r4 = int(input())

if (r1 > r2 and r1 > r3 and r1 > r4) and (r2 > r3 and r2 > r4) and (r3 > r4):
    print("Fish Diving")
elif (r4 > r3 and r4 > r2 and r4 > r1) and (r3 > r2 and r3 > r1) and (r2 > r1):
    print("Fish Rising")
elif r1 == r2 == r3 == r4:
    print("Fish At Constant Depth")
else:
    print("No Fish")
"""