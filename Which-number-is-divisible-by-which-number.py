try:
    print("Enter the number of apples harry have")
    apples = int(input())
    print("Enter mn numbers")
    mn = int(input())
    print("Enter mx numbers")
    mx = int(input())
    if mn >= mx:
        print("This is not a range, because mn is greater than mx")
        exit()
    for n in range(mn, mx+1):
        div = apples/n
        if mn<mx:
            if str(div).endswith(".0"):
                print(f"{n} is a divisor of {apples}")
            else:print(f"{n} is  not a divisor of {apples}")
except ValueError as e:
    print("Only numbers",e)
