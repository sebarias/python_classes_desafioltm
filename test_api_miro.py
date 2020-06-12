import json
import requests
import sys

#auth_code = "Bearer {}".format(sys.argv[1])
auth_code = "Bearer e8747311-77ea-43f4-b880-1794331c84ad"
board_id = "o9J_krVvvXs="
resource = "boards/{}/widgets/".format(board_id)

def request(uri, auth):
    url = "https://api.miro.com/v1/{}".format(uri)
    headers = {'authorization': auth}
    response = requests.request("GET", url, headers=headers)
    #print(response.text)
    results = json.loads(response.text)
    return results

def return_stikers_data(data, id):
    result = {}
    for dt in data:
        if(dt["id"] == id):
            result["text"] = dt["text"]
            result["color"] = dt["style"]["backgroundColor"]
            
            
    return result


#results = llamar("oauth-token",auth_code)
#team = results["team"]

#print("team id: {}".format(team["id"]))
#print(results.keys())
#print(results.values())

response = request(resource,auth_code)
data = response["data"]
story_names = []
stories = []

#filtro usando filter sobre data, para sacar solo los elementos de tipo "frame" y  que tengan hijos.

data_filter = list(filter(lambda elem: elem["type"]  == "frame" and len(elem["children"])  > 0, data))

#recorro la lista filtrada para obtener los elementos que necesito como nombre, id, y sus items asociados. luego genero una nueva lista con estos elementos.
for dt in data_filter:
    story = {}
    story_names.append(dt["title"])
    story["title"] = dt["title"]
    story["children"] = {}
    story["id"] = dt["id"]
    if(len(dt["children"]) > 0):
        for child in dt["children"]:
            story["children"][child] = return_stikers_data(data, child)
    stories.append(story)
#print(stories)

data_filter = list(filter(lambda elem: elem["type"]  == "frame" and len(elem["children"])  > 0, data))
print(len(data_filter))