from person import person
from customer import customer

if __name__ == "__main__":
    print("Enter details")
    fn = input("First Name : ")
    ln = input("Last Name : ")
    age = input(" Age : ")
    gender = input("Gender : ")
    idtype = input("ID Type : ")
    idno = input("ID Number : ")
    uid = input("User ID : ")
    pwd = input("Password : ")

c1 = customer(fn, ln, gender, age, uid, pwd, idtype, idno)
print("Account created Successfuly")
print("Account details are : ")
c1.detail()
