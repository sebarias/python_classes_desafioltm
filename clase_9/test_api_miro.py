import json
import requests
import sys

auth_code = "Bearer {}".format(sys.argv[1])

def llamar(uri, auth):
    url = "https://api.miro.com/v1/{}".format(uri)
    headers = {'authorization': auth}
    response = requests.request("GET", url, headers=headers)
    #print(response.text)
    results = json.loads(response.text)
    return results




results = llamar("oauth-token",auth_code)
team = results["team"]

#print("team id: {}".format(team["id"]))
print(results.keys())
print(results.values())