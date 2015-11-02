import urllib.request
import json
a = "features"
b = "properties"
c = "title"
d = "coughing"

def hello():
    #symptom=raw_input(enter symptom:)
    with open("symptom.json") as json_file:
        theJSON = json.load(json_file)
        for i in theJSON[a]:
            if i[b][d] >= 5.0:
                print (i[b][c])
hello()
        