from http.client import HTTPSConnection
import json

# User ID: 151069
# Authorization Token: 7a43a937-6f23-4e2a-8d52-d5f1f65b1639
auth_token = '7a43a937-6f23-4e2a-8d52-d5f1f65b1639'
hard_id = 151069

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

def getFieldDataById(authorization, user_id):
    authstring = 'Bearer ' + authorization
    connection = HTTPSConnection('hackillinois.climate.com')
    headers = {'Authorization': authstring,
               'Content-type': 'application/json',
               'Accept': 'application/json'}

    connection.request('GET', '/api/fields?includeBoundary=true&userId=%s'%user_id, headers=headers)
    response = connection.getresponse()
    data = response.read().decode()
    print(data)
    connection.close()
    return json.loads(data)
    
    
def getUserId(authorization, email):
    authstring = 'Bearer ' + authorization
    connection = HTTPSConnection('hackillinois.climate.com')
    headers = {'Authorization': authstring,
               'Content-type': 'application/json',
               'Accept': 'application/json'}
    #email = email.replace("@", 
    connection.request('GET', '/users/details?email='+email, headers=headers)
    response = connection.getresponse()
    data = response.read().decode()
    print(data)
    connection.close()
    the_json = json.loads(data)
    if 'id' in the_json:
        return the_json['id']
    else:
        return 0


def saveFieldData(fielddata, filename):
    text = json.dumps(fielddata)
    file = open(filename, 'w')
    file.write(text)
    file.close()

def getCoordinates(fieldData):
    return fieldData['coords']

#user_id = getUserId(auth_token, 'humblevladimirthegreat@gmx.com')
#print ('user_id = %s'%user_id)
#fieldData = getFieldDataById(auth_token, hard_id)
#print(fieldData)

fieldData = getFieldData('7a43a937-6f23-4e2a-8d52-d5f1f65b1639')
print(fieldData)
saveFieldData(fieldData, 'field_data.json')
