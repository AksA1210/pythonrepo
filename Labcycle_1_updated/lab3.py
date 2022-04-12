'''3. Develop a program to read the employee's name, code, and basic pay and calculate the gross salary, deduction,
and net salary according to the following conditions. Define a function to find each of the components. Finally, generate a payslip.'''

def grosssal():   # to calculate gross salary
  gs=BP+DA+HRA+MA
  return (gs)
def dedn():       # to calculate deduction
  d=PT+PF+IT 
  return(d)
def netsal(gs,d):  # to calculate net salary
  netsal=gs-d
  return(netsal)


empname=input("Enter the name of the employee : ")
empcode=int(input("Enter the code of the employee : "))
BP=int(input("Enter basic pay : "))
if (BP<10,000):
  DA=0.05*BP
  HRA=0.025*BP
  MA=500
  PT=20
  PF=0.08*BP
  IT=0
elif (BP<30,000 and BP>=10,000):
  DA=0.75*BP
  HRA=0.05*BP
  MA=2500
  PT=60
  PF=0.08*BP
  IT=0
elif (BP<50,000 and BP>=30,000 ):
  DA=0.11*BP
  HRA=0.075*BP
  MA=5000
  PT=60
  PF=0.11*BP
  IT=0.11*BP
else:
  DA=0.25*BP
  HRA=0.11*BP
  MA=7000
  PT=80
  PF=0.12*BP
  IT=0.2*BP
GS=grosssal()
D=dedn()
NetSalary=netsal(GS,D)
print("*******************************************PAYSLIP***********************************************************")
print("Name of the employee = ",empname)
print("Code of the employee = ",empcode)
print("Gross salary = ",GS)
print("Deduction = ",D)
print("Net Salary = ",NetSalary)
