import random as rd

l = [{"account no.": 123, "name": "Amit", "password": "abc", "balance": 13216.45},
     {"account no.": 456, "name": "Jack", "password": "efg", "balance": 1206.45},
     {"account no.": 789, "name": "Celina", "password": "ijk", "balance": 193036.45}]


def pwdCheck(pwd):
    i = 0
    while True:
        i += 1
        Pwd = input("Enter the password : ")
        if pwd != Pwd:
            if i < 3:
                print("Password is Incorrect\n{} attempts left!".format(3 - i))
                continue
            return False
        return True


def accOptions(d):
    a = int(input("Press 0 to Log Out\nPress 1 to Transfer Amount\nPress 2 to request Amount"))
    if a==1:
        acn = int(input("Enter Benificiary Ac/No. : "))
        for i in l:
            if i["account no."] == acn:
                print("Name = ", i["name"])
                bl = float(input("Enter Amount :"))
                if d["balance"] < bl:
                    print("Insufficient Balance")
                    accOptions(d)
                else:
                    d["balance"] -= bl
                    i["balance"] += bl
                    print("Transaction Successful")
                    print("Transaction ID =  ", rd.randint(100000, 1000000))
                    print("Balance left = ", d["balance"])
                break
        else:
            print("Account number does not exist!")
            accOptions(d)
    if a==2:
        acn = int(input("Enter Ac/No. : "))
        for i in l:
            if i["account no."] == acn:
                print("Name = ", i["name"])
                bl = float(input("Enter Amount :"))
                if i["balance"] < bl:
                    print("Insufficient Balance")
                    accOptions(d)
                else:
                    if pwdCheck(i["password"]):
                        i["balance"] -= bl
                        d["balance"] += bl
                        print("Transaction Successful")
                        print("Transaction ID =  ", rd.randint(1000000, 10000000))
                        print("Balance  = ", d["balance"])
                    break
        else:
            print("Account number does not exist!")
            accOptions(d)
    print("Successfully Log out")


def accDetails(i):
    print("Account Details are : ")
    for x, y in i.items():
        if x == "password":
            continue
        print(x, " = ", y)


def process():
    c = int(input("Press 0 to Create Account\nPress 1 to Login\n"))
    if c:
        uid = input("Enter User ID : ")
        for i in l:
            if i["name"] == uid:
                if pwdCheck(i["password"]):
                    print("Login Successful")
                    accDetails(i)
                    accOptions(i)
                    break
                print("Login Blocked")
                break
        else:
            print("User ID does not exist!")
            process()
    else:
        l.append({"account no.": rd.randint(100, 999), "name": input("Enter Name :"), "password": input("Enter Password :"),
              "balance": 0})
        print("Your Account  Created Successfully")
        for z in l:
            print(z)
        accDetails(l[-1])
        process()


process()
