import json
import pickle

#Serializace = převod Python objektu do JSON
#Deserializace = převod JSON do Python objektu

#encdoing - do bytu
with open('data.json','r') as f:
    data =json.load(f)

print(data)
    
novy={"name":"Krystof","age":13,"role":"devOps"}

data.append(novy)

with open('data.json','w') as f:
    json.dump(data,f )
print(data)

# pickle = binarni serializace Python objektu
objekt = {"name": "Robin", "skills": ["Python", "JSON", "pickle"]}


with open('data.pkl','wb') as f:
    pickle.dump(objekt,f)
    
with open('data.pkl','rb') as f :
    bajty = f.read()
print(bajty)