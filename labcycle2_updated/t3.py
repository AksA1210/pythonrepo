with open("iris.json") as f:
  lines= f.read()
  list1=[]
  for i in lines.split(" "):
       list1=list1+[i]
  print(list1,"\n")
  print()
  Line_list = str_data.split("\n")
  print(Line_list)
   
  l= json.load(f)
  print("sepalLength\tsepalWidth\tpetalLength\tpetalWidth")
  for i in l:
      if i['species'] == 'setosa':
  print(i['sepalLength'],"\t\t",i['sepalWidth'],"\t\t",i['petalLength'],"\t\t",i['petalWidth'])

 species = []
for j in l:
  if j['species'] not in species:
    species.append(j['species'])
print(species)
Max_PA = []
Max_SA = []
c = 0
for s in species:
  Max_PA.append(100)
  Max_SA.append(0)
  for j in l:
    if j['species'] == Species:
      if (j['petalLength'] * j['petalWidth']) < Max_PA[c]:
        Max_PA[c] = round(j['petalLength'] * j['petalWidth'],2) 
      if (j['sepalLength'] * j['sepalWidth']) > Max_SA[c]:
        Max_SA[c] = round(j['sepalLength']* j['sepalWidth'],2)
  c+=1
print(Max_SA)
print(Max_PA)
for i in l:
  x = 0
  TArea = i['sepalLength']*i['sepalWidth'] + i['petalLength']*i['petalWidth']
  i['TotalArea'] = round(TArea,2)

for a in l:
  for i in range(0,len(l)-1) :
    p = l[i]
    q = l[i+1]
    if p['TotalArea'] > q['TotalArea']:
      l[i],l[i+1] = l[i+1],l[i]
for i in l:
  print(i)    
