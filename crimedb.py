from model import criminalmodel,victimmodel,crimemodel
from tabulate import tabulate
class CrimeDb:

    def __init__(self):
        id = int(input("Enter Crime ID To View Overall Crime Details: "))
        obj1 = criminalmodel.CriminalModel()
        criminalname = obj1.get_id(id)
        obj2 = victimmodel.VictimModel()
        victimidname = obj2.getid(id)
        header = ["CRIME_ID","VICTIM_NAME","CRIMINAL_NAME","DATE_OF_CRIME","POLICESTATION_ID","CRIME_DETAILS","CRIME_STATUS"]
        obj3 = crimemodel.CrimeModel()
        row = obj3.overview(id)
        rows = []
        rows.append(str(id))
        rows.append(victimidname)
        rows.append(criminalname)
        for i in range(4):
            rows.append(row[0][i])
        ans = []
        ans.append(rows)
        print(tabulate(ans,header,tablefmt="rounded_grid"))