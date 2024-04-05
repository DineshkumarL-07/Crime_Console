from model import victimmodel
from tabulate import tabulate

class Victim:
    def __init__(self):
        print("1) VIEW VICTIM DATA\n2) ADD VICTIM DATA\n3) UPDATE VICTIM DATA\n4) REMOVE VICTIM DATA\n5) SEARCH VICTIM DATA")
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
        print("Select the format you want to view victim data")
        print("1) In Table Format\n2) In Normal Format")
        temp = int(input("\nEnter Your Format choice:"))
        obj = victimmodel.VictimModel()
        rows = obj.view()
        if temp == 1:
            header = ["VICTIM_ID", "VICTIM_NAME", "VICTIM_AGE", "VICTIM_GENDER", "VICTIM_ADDRESS", "VICTIM_AADHAAR",
                      "VICTIM_DESCRIPTION"]
            print(tabulate(rows, header, tablefmt="rounded_grid"))
        elif temp == 2:
            for row in rows:
                print(f'VICTIM_ID: {row.VICTIMID}\nVICTIM_NAME: {row.V_NAME}\nVICTIM_AADHAAR: {row.V_AADHAAR}\nVICTIM_AGE: {row.V_AGE}\nVICTIM_GENDER: {row.V_GENDER}\nVICTIM_ADDRESS: {row.V_ADDRESS}\nVICTIM_DESCRIPTION: {row.V_DISCRIPTION}\n')
        else:
            print("Invalid choice")
    def adddata(self):
        print("Enter The Victim Details")
        name = input("Enter The Victim Name: ")
        age = input("Enter The Victime Age: ")
        gender = input("Enter The Victim Gender: ")
        Address = input("Enter The Victim Address: ")
        aadhaar = input("Enter The Victim Aadhaar Number: ")
        description = input("Enter The Victim's Description: ")
        obj = victimmodel.VictimModel()
        temp = obj.insert(name, age, gender, Address, aadhaar, description)
        if temp == False:
            print("Error Occured while adding! Enter an valid data")
            self.adddata()
        else:
            print("Victim Details was Added Successfully")

    def updatedata(self):
        id = int(input("Enter the Victim Id or Criminal Name to where you would like to update: "))
        col = input("Enter The Column Name that you would like to update:  ")
        val = input("Enter The Column Value that you would like to update: ")
        obj = victimmodel.VictimModel()
        temp = obj.update(id, col, val)
        if temp:
            print("Updated Successfully")
        else:
            print("Victim Id or Victim name Not Found or Wrong Column")
    def removedata(self):
        id = eval("Enter Victim ID to Victim Name to Remove The Data: ")
        obj = victimmodel.VictimModel()
        temp = obj.delete_specific(id)
        if temp:
            print("The Victim Detail Was Removed Successfully")
        else:
            print("Victim Id not found, Enter an valid Id")
    def searchdata(self):
        col = input("Enter The Column Name:  ")
        val = input("Enter The Column Value: ")
        obj = victimmodel.VictimModel()
        temp = obj.view_specific(col, val)
        if temp:
            header = ["VICTIM_ID", "VICTIM_NAME", "VICTIM_AGE", "VICTIM_GENDER", "VICTIM_ADDRESS", "VICTIM_AADHAAR",
                      "VICTIM_DESCRIPTION"]
            print(tabulate(temp, header, tablefmt="rounded_outline"))
        else:
            print("Value not found, Try enter a valid data")