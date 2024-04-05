from model import crimemodel
from tabulate import tabulate

class Crime:
    def __init__(self):
        print("1) VIEW CRIME DATA\n2) ADD CRIME DATA\n3) UPDATE CRIME DATA\n4) REMOVE CRIME DATA\n5) SEARCH CRIME DATA")
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
        print("Select the format you want to view crime data")
        print("1) In Table Format\n2) In Normal Format")
        temp = int(input("\nEnter Your Format choice:"))
        obj = crimemodel.CrimeModel()
        rows = obj.view()
        if temp == 1:
            header = ["CRIME_ID", "CRIME_DATE", "POLICE_STATION_NAME", "CRIME_DETAILS", "CRIME_STATUS", "CRIME_PLACE",
                      "CRIME_WITNESS", "CRIME_EVIDENCE"]
            print(tabulate(rows, header, tablefmt="rounded_grid"))
        elif temp == 2:
            for row in rows:
                print(f'CRIME_ID: {row.CRIMEID}\nCRIME_DATE: {row.DATEOFCRIME}\nPOLICE_STATION_NAME: {row.POLICESTATIONID}\nCRIME_DETAILS: {row.DISCRIPTION}\nCRIME_STATUS: {row.STATUSOFCRIME}\nCRIME_PLACE: {row.PLACEOFCRIME}\nCRIME_WITNESS: {row.WITNESS}\nCRIME_EVIDENCE: {row.EVIDENCE}\n')
        else:
            print("Invalid choice")

    def adddata(self):
        print("Enter The Crime Details")
        date = input("Enter The Crime Date: ")
        police = input("Enter The Police Station Name: ")
        details = input("Enter The Crime Details: ")
        status = input("Enter The Crime Status: ")
        place = input("Enter The Crime Place: ")
        witness = input("Enter The Crime Witness Details: ")
        evidence = input("Enter The Crime Evidence: ")
        obj = crimemodel.CrimeModel()
        temp = obj.insert(date, police, details, status, place, witness, evidence)
        if temp == False:
            print("Error Occured while adding! Enter an valid data")
            self.adddata()
        else:
            print("Crime Details was Added Successfully")

    def updatedata(self):
        id = int(input("Enter the Crime Id to where you would like to update: "))
        col = input("Enter The Column Name that you would like to update:  ")
        val = input("Enter The Column Value that you would like to update: ")
        obj = crimemodel.CrimeModel()
        temp = obj.update(id, col, val)
        if temp == True:
            print("Updated Successfully")
        else:
            print("Crime Id Not Found or Wrong Column")

    def removedata(self):
        id = int(input("Enter Crime ID to Remove The Crime Data : "))
        obj = crimemodel.CrimeModel()
        temp = obj.delete_specific(id)
        if temp:
            print("The Crime Detail Was Removed Successfully")
        else:
            print("Crime Id not found, Enter an valid Id")

    def searchdata(self):
        col = input("Enter The Column Name:  ")
        val = input("Enter The Column Value: ")
        obj = crimemodel.CrimeModel()
        temp = obj.view_specific(col, val)
        if temp:
            header = ["CRIME_ID", "CRIME_DATE", "POLICE_STATION_NAME", "CRIME_DETAILS", "CRIME_STATUS", "CRIME_PLACE",
                      "CRIME_WITNESS", "CRIME_EVIDENCE"]
            print(tabulate(temp, header, tablefmt="rounded_outline"))
        else:
            print("Value not found, Try to enter a valid data")