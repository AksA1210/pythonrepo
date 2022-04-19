

import json

def readAsList(filepath):
  with open(filepath) as f:
    jsonList = f.readlines()
  return jsonList

def readAsListOfDict(filepath):
  with open(filepath) as f:
    jsonData = json.load(f)
  return jsonData

def printSetosa(jsonList):
  #printing the details of only setosa.
  print("\nDetails of flowers of species setosa")
  for i in jsonList:
    if(i['species']=='setosa'):
      print(i)

def Sepal_areaAndPetal_area(jsonList):
  listOfSpeciesName = list()
  for i in jsonList:
    listOfSpeciesName.append(i['species'])
  listOfSpeciesName = list(set(listOfSpeciesName))
  sepal_area = []
  petal_area = []
  for i in listOfSpeciesName:
    for j in jsonList:
      if(j['species']==i):
        sepal_area.append(j['sepalLength']*j['sepalWidth'])
        petal_area.append(j['petalLength']*j['petalWidth'])
    print()
    print(i.capitalize())
    print("Maximum Sepal Area in ",i.capitalize()," is ",round(max(sepal_area),2))
    print("Minimum Petal Area in ",i.capitalize()," is ",round(min(petal_area),2))
    sepal_area.clear()
    petal_area.clear()
    
def sortTotal_area(jsonList):
  for i in jsonList:
    total_area = (i['petalLength']*i['petalWidth'])+(i['sepalLength']*i['sepalWidth'])
    i.update({'totalArea':round(total_area,2)})
  sorted_list = sorted(jsonList,key=lambda i:i['totalArea'])
  print("\nList sorted on the basis of total area")
  for i in sorted_list:
    print(i)

filePath = 'iris.json'
jsonList = readAsList(filePath)
print("List with each line as element\n")
for line in jsonList:
  print(line)

jsonData = readAsListOfDict(filePath)
print("\nList of Dictionaries")
for i in jsonData:
  for key, values in i.items():
    print(key.capitalize()+" : ",values,end=" , ")
  print()

printSetosa(jsonData)
Sepal_areaAndPetal_area(jsonData)
sortTotal_area(jsonData)
