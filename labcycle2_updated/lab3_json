

import json
def read_as_list(filename):
  fp=open(filename,"r")                             
  data=fp.readlines() 			          #The file elements as list elements
  fp.close()
  return data
   
def read_as_dict(filename):
  fp=open(filename,'r')                            
  dictionary=json.load(fp) 	
  return dictionary			 #list of dictionary

def print_details_setosa(data_dict):
  print("\nAll flowers whose species is setosa\n")
  for i in data_dict:					  #'i' is the dictionary element in the list
    if (i['species']=='setosa'):
        print('Sepel length : %f, '%(i['sepalLength']))

def get_areas(data_dict):
  petal_areas=[i['petalLength']*i['petalWidth']  for i in data_dict]
  sepal_areas=[i['sepalLength']*i['sepalWidth'] for i in data_dict]
  return petal_areas,sepal_areas

def get_min_petal_area(petal_areas):
  m1 = min([area for area,species in petal_areas if species=='setosa'])
  m2 = min([area for area,species in petal_areas if species=='setosa'])
  m3 = min([area for area,species in petal_areas if species=='setosa'])

def get_max_sepal_area(sepal_areas):
  m1 = max([area for area,species in sepal_areas if species=='setosa'])
  m2 = max([area for area,species in sepal_areas if species=='setosa'])
  m3 = max([area for area,species in sepal_areas if species=='setosa'])
  


data = read_as_list('iris.json')
for line in data:
  print(line)

data_dict = read_as_dict('iris.json')
for row in data_dict:
  print(row)

print_details_setosa(data_dict)
