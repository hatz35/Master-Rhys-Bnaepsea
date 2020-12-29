all_players = list() #List of Objects: Players
import os
import json


with open("record.json") as f:
  data = json.load(f)

print(data)
def add_to_json(newname, newrating):
    data["individuals"]["name"] = newname
    data["individuals"]["rating"] = rating

'''
#After changing data
json.dumps(data, indent = 2)
a = json.dumps(data, indent = 3, sort_keys = True) #optional of course
print (a)

#If you have a separate .json file
with open('filename.json') as f:
  data = json.load(f)

#Creating  a file which doesn't exist already
with open('newfilename.json', 'w') as f:
  json.dump(data, f, indent = 2) #if you want data of this file to be the same as the file you opened just about
'''
