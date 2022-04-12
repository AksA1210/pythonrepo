with open("iris.json") as f:
  str_data = f.read()
  Line_list = str_data.split("\n")
  print(Line_list)

with open("iris.json") as f:
import json
data = json.load(f)
print("sepalLength\tsepalWidth\tpetalLength\tpetalWidth")
for i in data:
  if i['species'] == 'setosa':
    print(i['sepalLength'],"\t\t",i['sepalWidth'],"\t\t",i['petalLength'],"\t\t",i['petalWidth'])

species = []
for j in data:
  if j['species'] not in species:
    species.append(j['species'])
print(species)
Max_PA = list()
Max_SA = list()
c = 0
for Species in species:
  Max_PA.append(100)
  Max_SA.append(0)
  for j in data:
    if j['species'] == Species:
      if (j['petalLength'] * j['petalWidth']) < Max_PA[c]:
        Max_PA[c] = round(j['petalLength'] * j['petalWidth'],2) 
      if (j['sepalLength'] * j['sepalWidth']) > Max_SA[c]:
        Max_SA[c] = round(j['sepalLength']* j['sepalWidth'],2)
  c+=1
print(Max_SA)
print(Max_PA)
for i in data:
  x = 0
  TArea = i['sepalLength']*i['sepalWidth'] + i['petalLength']*i['petalWidth']
  i['TotalArea'] = round(TArea,2)

#TO sort the list of Dictionaries
for _ in data:
  for i in range(0,len(data)-1) :
    d1 = data[i]
    d2 = data[i+1]
    if d1['TotalArea'] > d2['TotalArea']:
      data[i],data[i+1] = data[i+1],data[i]
for i in data:
  print(i)    
