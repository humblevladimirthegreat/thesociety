from http.client import HTTPSConnection
import json

# User ID: 151069
# Authorization Token: 7a43a937-6f23-4e2a-8d52-d5f1f65b1639


def getFieldData(authorization):
    authstring = 'Bearer ' + authorization
    connection = HTTPSConnection('hackillinois.climate.com')
    headers = {'Authorization': authstring,
               'Content-type': 'application/json',
               'Accept': 'application/json'}

    connection.request('GET', '/api/fields?includeBoundary=true', headers=headers)
    response = connection.getresponse()
    data = response.read().decode()
    print(data)
    connection.close()
    return json.loads(data)


def saveFieldData(fielddata, filename):
    text = json.dumps(fielddata)
    file = open(filename, 'w')
    file.write(text)
    file.close()

def getCoordinates(fieldData):
    return fieldData['coords']

fieldData = getFieldData('7a43a937-6f23-4e2a-8d52-d5f1f65b1639')
print(fieldData)
saveFieldData(fieldData, 'field_data.json')