largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        num = int(num)
        if smallest is None:
            smallest = num
        elif smallest > num:
            smallest = num
        if largest is None:
            largest = num
        elif largest < num:
            largest = num
    except:
        print("Invalid input")

print("Maximum is", largest)
print("Minimum is", smallest)
