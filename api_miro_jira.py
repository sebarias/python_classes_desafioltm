import json
import requests
import sys
import re

#variables globales
board_id = "o9J_krUi7fI="
dict_colors = {"#23bfe7":"front","#ff9d48":"backend","#f16c7f":"QA","#fff9b1":"story","#d5f692":"task"}
stories = []
project_jira = "17602"
dict_task_type ={5: "Sub-Task", 3 : "Task", 10000 : "Epic", 100001 : "Story", 1 : "Bug"}
dict_estimate = {"xs": "2h", "s": "4h", "m":"1d", "l": "1d 4h", "xl":"2d", "xxl":"3d"}
auth_jira = ""
auth_miro = ""

def mostrar_menu(saldo = 0):
    print('¡Bienvenido!. Escoja una opción:')
    print('-' * 20)
    print('1) Obtener data de miró')
    print('2) Transforamr data de miró a Jira')
    print('3) Enviar data a Jira cuando las HU ya existen')
    print('4) Salir')
    print()

def request_to_jira(uri,payload):
    url = "http://jira.bch.bancodechile.cl:8080/rest/api/2/{}".format(uri)
    headers = {'Content-Type':'application/json', 'Authorization': auth_jira}
    querystring = {"":""}
    response = requests.request("POST", url, data=payload, headers=headers, params=querystring)
    #print(response.text)
    results = json.loads(response.text)
    return results

def request_to_miro(uri):
    url = "https://api.miro.com/v1/{}".format(uri)
    headers = {'authorization': auth_miro}
    response = requests.request("GET", url, headers=headers)
    results = json.loads(response.text)
    return results

def return_stikers_data(data, id):
    result = {}
    for dt in data:
        if(dt["id"] == id and dt["type"] == "sticker"):
            # obtener el tamaño de text
            # obtener el texto sin <p>
            postit = re.sub('</*.?>','',dt["text"].lower()).split("size")
            result["text"] = postit[0]
            if(len(postit) > 1):
                result["size"] = postit[1].replace(":","").replace(" ","").upper()
            #hacer por color y asociar al tipo de tarea
            result["type"] = dict_colors[dt["style"]["backgroundColor"]]
    return result

def create_story(summary):
    issue_type = { "id" : "10001"}
    project = { "id" : project_jira}
    fields = {"project":project , "summary":summary, "issuetype":issue_type}
    payload = { "fields" : fields}
    #uri = "issue"
    #return request_to_jira(uri,payload)
    return payload

def create_jira_issues(stories):
    stories_jira = []
    for st in stories:
        story = create_story(st["title"])
        stories_jira.append(story)
    pl = { "issueUpdates" : stories_jira}
    print(json.dumps(pl))
    uri = "issue/bulk"
    return request_to_jira(uri,json.dumps(pl))

def push_story_onjira(story):
    uri = "issue"
    issue = create_story(story["title"])
    return request_to_jira(uri,json.dumps(issue))

def push_subtask_onjira(parent_jira_id, story):
    children = story["children"]
    issues = []
    for k, value in children.items():
        labels = []
        if(value["type"] != "story"):
            summary = value["text"]
            issuetype = {"id":"5"}
            labels.append(value["type"])
            estimate = dict_estimate[value["size"].lower()]
            time_tracking = {"originalEstimate":estimate, "remainingEstimate": estimate}
            project = {"id":project_jira}
            parent = {"id": parent_jira_id}
            fields = {"project":project, "parent":parent, "summary": summary, "issuetype": issuetype, "labels": labels, "timetracking": time_tracking}
            issues.append({"fields": fields})
    uri = "issue/bulk"
    payload = json.dumps({"issueUpdates":issues})
    return request_to_jira(uri, payload)


# inicio de main 
opt_menu = ""

while opt_menu != '4':
    mostrar_menu() # Se llama a la función
    
    opt_menu = input()

    if opt_menu == '1':
        auth_miro = input('ingrese autorización de miro: ')
        auth_jira = input("Ingrese auth de jira: ")
        resource = "boards/{}/widgets/".format(board_id)
        response = request_to_miro(resource)
        
        data = response["data"]
        
        story_names = []
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
            print("story: ", story)
            print("/n")
            stories.append(story)
    elif opt_menu == '2':
        #auth_jira = input("Ingrese auth de jira: ")
        if(len(stories) > 0):
            # print("creando historias")
            # rs = push_story_onjira(stories[2])
            # print(rs)
            # id = rs["id"]
            # rs2 = push_subtask_onjira(id, stories[2])2
            # print(rs2)
            
            
            for story in stories:
                print(story['title'])
                #  rs = push_story_onjira(story)
                #  print(rs)
                #  id = rs["id"]
                #  rs2 = push_subtask_onjira(id, story)
                #  print(rs2)
        else:
            print("no hay historias que crear.")
    elif opt_menu == '3':
        #si las hu estan creadas en jira, en el nombre del frame colocar el id de jira.
        print(3)
        for story in stories:
            #print(story['title'])
            id = story['title']
            rs2 = push_subtask_onjira(id, story)
            print(rs2, "\n")
        

    elif opt_menu == '4':
        print('Saliendo')
    else:
        print('Opción inválida\n')
print()
