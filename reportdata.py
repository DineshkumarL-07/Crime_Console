from model import criminalmodel,victimmodel,crimemodel

class ReportData:
    def __init__(self):
        print("Here, You can made an final report of the crime")
        id = int(input("Enter The Crime ID: "))
        criminal = input("Enter the Criminal ID or Criminal Name: ")
        victim = input("Enter the Victim ID or Victim Name: ")
        if criminal.isnumeric():
            criminal_id = criminal
        else:
            obj = criminalmodel.CriminalModel()
            criminal_id = obj.get_name(criminal)
        if victim.isnumeric():
            victim_id = victim
        else:
            obj = victimmodel.VictimModel()
            victim_id = obj.get_id(victim)
        obj1 = crimemodel.CrimeModel()
        temp = obj1.report(id,criminal_id,victim_id)
        if temp:
            print(f"The Crime Report for Crime ID {id} is added successfully")
        else:
            print("Enter an Valid Data")