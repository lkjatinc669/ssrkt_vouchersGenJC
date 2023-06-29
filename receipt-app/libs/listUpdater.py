import json 
import os

print(os.getcwd())

def update(newUnit):
    with open(r"statics/headDept.json", "r+") as file:
        data = json.load(file)

    updateData = data['accountHead']
    updateData.append(newUnit)

    newData = {"accountHead":updateData}

    finalData = json.dumps(newData, indent=4, sort_keys=True)
    with open(r"statics/headDept.json", "w+") as file:
        file.write(finalData)

# update("yssaaash")