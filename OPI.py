from datetime import datetime
class Citizen:
  def __init__(self, State, Birth,Income):
    self.State = State
    self.Birth = Birth
    self.Income=Income
  def toAge(self):
        dob = datetime.strptime(self.Birth, "%d.%m.%Y")
        current_date = datetime.now()
        age = current_date.year - dob.year - ((current_date.month, current_date.day) < (dob.month, dob.day))
        return age



def CalculateTaxes(Citizen):
    if Citizen.State == 'Texas':
        return Citizen.Income*0.17

    elif Citizen.State== "California":
        return Citizen.Income*0.32

    elif Citizen.State == "Alaska":
        return Citizen.Income * 0.15

    elif Citizen.State == "Arizona":
        if Citizen.Income<30000:
            return 0
        else:
            return Citizen.Income*0.22

    elif Citizen.State == "Pennsylvania":
        if Citizen.toAge() < 31:
            return Citizen.Income*0.17
        elif Citizen.toAge() > 76:
            return Citizen.Income * 0.15
        else:
            return Citizen.Income * 0.22
    elif Citizen.State == "Montana":
        if Citizen.Income < 100000:
            return Citizen.Income * 0.22
        else:
            return Citizen.Income * 0.22

C=Citizen("Pennsylvania", "21.04.1990", 50000)
print(CalculateTaxes(C))