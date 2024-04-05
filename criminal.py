from model import criminalmodel
from tabulate import tabulate

class Criminal:
    def __init__(self):
        print("1) VIEW CRIMINAL DATA\n2) ADD CRIMINAL DATA\n3) UPDATE CRIMINAL DATA\n4) REMOVE CRIMINAL DATA\n5) SEARCH CRIMINAL DATA")
        choice = int(input("Enter your choice: "))
        while True:
            temp = self.viewdata() if choice == 1 else self.adddata() if choice == 2 else self.updatedata() if choice == 3 else self.removedata() if choice == 4 else self.searchdata() if choice == 5 else print("Invalid choice")
            do = input("Do you want to continue the crime operations (yes/no) ?")
            if do == "no" or do == "No":
                break
            else:
                choice = int(input("Enter your choice: "))
                continue

    def viewdata(self):
        print("Select the format you want to view criminal data")
        print("1) In Table Format\n2) In Normal Format")
        temp = int(input("\nEnter Your Format choice:"))
        obj = criminalmodel.CriminalModel()
        rows = obj.view()
        if temp == 1:
            header = ["CRIMINAL_ID", "CRIMINAL_NAME", "CRIMINAL_AADHAAR", "CRIMINAL_AGE", "CRIMINAL_GENDER",
                      "CRIMINAL_ADDRESS", "POLICE_STATION_NAME", "CRIMINAL_IDENTIFICATION_MARK"]
            print(tabulate(rows, header, tablefmt="rounded_grid"))
        elif temp == 2:
            for row in rows:
                print(
                    f'CRIMINAL_ID: {row.CRIMINALID}\nCRIMINAL_NAME: {row.CRIMINALNAME}\nCRIMINAL_AADHAAR: {row.CRIMINALAADHAAR}\nCRIMINAL_AGE: {row.CRIMINALAGE}\nCRIMINAL_GENDER: {row.CRIMINALGENDER}\nCRIMINAL_ADDRESS: {row.CRIMINALADDRESS}\nPOLICE_STATION_NAME: {row.POLICESTATIONID}\nCRIMINAL_IDENTIFICATION_MARK: {row.BIRTHMARK}\n')
        else:
            print("Invalid choice")

    def adddata(self):
        print("Enter The Criminal Details")
        name = input("Enter The Criminal Name: ")
        aadhaar = input("Enter The Criminal Aadhaar Number: ")
        age = input("Enter The Criminal Age: ")
        gender = input("Enter The Criminal Gender: ")
        Address = input("Enter The Criminal Address: ")
        police = input("Enter The Police Station Name: ")
        birthmark = input("Enter The Birthmark Of The Criminal: ")
        obj = criminalmodel.CriminalModel()
        temp = obj.insert(name, aadhaar, age, gender, Address, police, birthmark)
        if temp == False:
            print("Error Occured while adding! Enter an valid data")
            self.adddata()
        else:
            print("Criminal Details was Added Successfully")

    def updatedata(self):
        id = int(input("Enter the Criminal Id or Criminal Name to where you would like to update: "))
        col = input("Enter The Column Name that you would like to update:  ")
        val = input("Enter The Column Value that you would like to update: ")
        obj = criminalmodel.CriminalModel()
        temp = obj.update(id, col, val)
        if temp:
            print("Updated Successfully")
        else:
            print("Criminal Id or Criminal name Not Found or Wrong Column")

    def removedata(self):
        id = eval("Enter Criminal ID or Criminal Name to Remove The Data: ")
        obj = criminalmodel.CriminalModel()
        temp = obj.delete_specific(id)
        if temp:
            print("The Criminal Detail Was Removed Successfully")
        else:
            print("Criminal Id not found, Enter an valid Id")

    def searchdata(self):
        col = input("Enter The Column Name:  ")
        val = input("Enter The Column Value: ")
        obj = criminalmodel.CriminalModel()
        temp = obj.view_specific(col, val)
        if temp:
            header = ["CRIMINAL_ID", "CRIMINAL_NAME", "CRIMINAL_AADHAAR", "CRIMINAL_AGE", "CRIMINAL_GENDER",
                      "CRIMINAL_ADDRESS", "POLICE_STATION_NAME", "CRIMINAL_IDENTIFICATION_MARK"]
            print(tabulate(temp, header, tablefmt="rounded_outline"))
        else:
            print("Value not found, Try to enter a valid data")
