hrs = float(input("Enter Hours:"))
rate = float(input("Enter Rate:"))
if hrs <= 40:
    pay = hrs * rate
else:
    pay = 1.5 * rate * (hrs - 40) + 40*rate
print(pay)
