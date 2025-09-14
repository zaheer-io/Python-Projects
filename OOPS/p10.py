class Hospital:
    def __init__(self):
        self.hName = input("Enter hospital name: ")

    def showHospitalName(self):
        print(f"Hospital name: {self.hName}")


class Department:
    def __init__(self):
        self.depName = input("Enter department name: ")

    def printDepartemntName(self):
        print(f"Department name : {self.depName}")

class Patient(Hospital, Department):
    def __init__(self):
        Hospital.__init__(self)
        Department.__init__(self)

        self.name = input("Enter patient name: ")
        self.age = int(input("Enter patient age: "))
        self.gender = input("Enter patient gender: ")
        self.admDate = input("Enter date of admission: ")
        self.bedNo = int(input("Enter bed no: "))
        self.dischargeDate = ""

    def fullSummary(self):
        print(f"Patient name: {self.name}")
        print(f"Patient age: {self.age}")
        print(f"Patient Gender: {self.gender}")
        print(f"Patient Admission date: {self.admDate}")
        print(f"Patient Bed number: {self.bedNo}")
        if self.dischargeDate != "":
            print(f"Patient Discharge date: {self.dischargeDate}")
        else:
            print(f"Patient Discharge date: Not discharged")
        Hospital.showHospitalName(self)
        Department.printDepartemntName(self)
        Hospital().showHospitalName()

    def setDischarge(self):
        self.dischargeDate = input("Enter discharge date: ")


obj = Patient()
print("\n")
obj.fullSummary()
print("\n")
obj.setDischarge()
print("\n")
obj.fullSummary()