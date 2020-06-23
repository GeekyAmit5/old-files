def computepay(h, r):
    if h <= 40:
        pay = h * r
    else:
        pay = 40 * r + r * (h-40) * 1.5
    return pay


hrs = float(input("Enter Hours:"))
rate = float(input("Enter Rate:"))
print("Pay", computepay(hrs, rate))
