import datetime


class person:
    persons = 0

    def __init__(self, fname, lname, dob, gender, idtype, idno):
        self.fname = fname
        self.lname = lname
        self.dob = dob
        self.idtype = idtype
        self.idno = idno
        self.gender = gender
        self.age = (datetime.datetime.today()-dob).days//365
        person.persons += 1

    def detail(self):
        print(f"Name : {self.fname} {self.lname}")
        print(f"Date of Birth : {self.dob}")
        print(f"Age : {self.age}")
        print(f"Gender : {self.gender}")
        print(f"ID Proof type : {self.idtype}")
        print(f"ID Proof Number : {self.idno}")
