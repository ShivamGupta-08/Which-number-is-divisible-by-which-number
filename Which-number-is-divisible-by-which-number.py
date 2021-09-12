print("Enter the number of apples harry have")
apples = int(input())
print("Enter mn numbers")
mn = int(input())
print("Enter mx numbers")
mx = int(input())
x = range(mn, mx+1)
for n in x:
    div = apples/n
    if mn==mx:
        print("This is not a range, and mn is equal to mx")
    if str(div).endswith(".0"):
        print(f"{n} is a divisor of {apples}")
    else:print(f"{n} is  not a divisor of {apples}")
