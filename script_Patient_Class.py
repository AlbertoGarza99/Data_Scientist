class Patient:
  def __init__(self, name, age, sex, bmi, num_of_children, smoker):
    self.name = name
    self.age = age
    self.sex = sex
    self.bmi = bmi
    self.num_of_children = num_of_children
    self.smoker = smoker

  def estimated_insurance_cost(self):
    estimated_cost= (250*(self.age)) - (128*(self.sex)) + (370*(self.bmi)) + (425*(self.num_of_children)) + (24000*(self.smoker)) - (12500)
    print("{Name}’s estimated insurance costs is {Cost} dollars.".format(Name = self.name, Cost = estimated_cost))

  def update_age(self, new_age):
    self.age = new_age    
    print("{Name} is now {New_age} years old.".format(Name = self.name, New_age = self.age))
    self.estimated_insurance_cost()

  def update_num_children(self, new_num_children):
    self.num_of_children = new_num_children
    if self.num_of_children == 1:
      print("{Name} has {Children} child.".format(Name = self.name, Children = self.num_of_children))
    else:
      print("{Name} has {Children} children.".format(Name = self.name, Children = self.num_of_children))
    self.estimated_insurance_cost()

  def update_bmi(self, new_bmi):
    self.bmi = new_bmi
    print("{Name} has now a bmi of {bmi}.".format(Name = self.name, bmi = self.bmi))

  def smoking_status(self, new_smoking_status):
    self.bmi = new_smoking_status
    print("{Name} has {Smoke} child.".format(Name = self.name, Smoke = self.smoker))
  
  def patient_information(self):
    patient_information = {"Name": self.name, "Age": self.age, "Sex": self.sex, "BMI": self.bmi, "Numer of Children": self.num_of_children, "Smoker": self.smoker}
    return patient_information

Full_dictionary_patients = {}
def update_dictionary(medical_record):
  for record in medical_record:
    patient = Patient(record[0], record[1], record[2], record[3], record[4], record[5])
    data = patient.patient_information()
    print(data)
    Full_dictionary_patients.update({data["Name"]: data})


patient1 =[["John Doe", 25, 1, 22.2, 0, 0]]
patients = [["Michael Jefferson", 45, 1, 27.2, 2, 1], ["Veronica Mills", 56, 0, 18.2, 4, 1]]

update_dictionary(patient1)
update_dictionary(patients)

print("\n")
print(Full_dictionary_patients)

print("\n")
print(Full_dictionary_patients["Veronica Mills"])
