from person import person


class customer(person):
    customers = 0

    def __init__(self, fname, lname, gender, age, uid, pwd, idtype, idno):
        super().__init__(fname, lname, age, gender, idtype, idno)
        self.uid = uid
        self.pwd = pwd
        self.idtype = idtype
        self.idno = idno
        self.cid = getCustomerID()
        self.acno = getAcccountNumber()
        person.people += 1

    # def getAcccountNumber(self):
    #     while True:
    #         acno = random.randint(1000,9999)
    #         if

    def getCustomerID(self):
        pass

    def detail(self):
        super().detail()
        print(f"Account Number : {self.acno}")
        print(f"Customer ID : {self.cid}")
