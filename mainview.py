from controller import usercontroller, reportdata,crime,criminal,victim,crimedb

print("---------------------------------------------- WELCOME TO CRIME DATA MANAGEMENT --------------------------------------")
print("1) SIGN UP\n2) LOG IN\n3) EXIT\n")
choice = int(input("Enter your choice: "))
if choice == 1:
    temp = usercontroller.User()
    temp.signup()
if choice == 2:
    tempp = usercontroller.User()
    tempp.login()
    if tempp:
        print("1) CRIME DATA OPERATIONS\n2) CRIMINAL DATA OPERATIONS\n3) VICTIM DATA OPERATIONS\n4) FINAL REPORT OF CRIME DATA\n5) VIEW OVERALL CRIME\n6) ADD USER DATA\n7) EXIT")
        # print("1) VIEW DATA\n2) ADD DATA\n3) SERACH DATA\n4) REMOVE DATA\n5) UPDATE DATA\n6) REPORT\n7) ADD USER\n8) VIEW OVERALL CRIME DETAIL\n9) EXIT")
        opt = int(input("Enter your option: "))
        while opt != 7:
            ans = crime.Crime() if opt == 1 else criminal.Criminal() if opt == 2 else victim.Victim if opt == 3 else reportdata.ReportData if opt == 4 else crimedb.CrimeDb() if opt == 5 else tempp.signup() if opt == 6 else  print("Invalid option")
            opt = int(input("Enter your option: "))
else:
    print("-------------------------------------------------- Thank You -------------------------------------------------------")
