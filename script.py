import json
import requests

def forked_repos(user, headers):
    url = "https://api.github.com/users/"+ user + "/repos"
    
    response = requests.request("GET", url, headers=headers)

    results = response.json()
    output = []
    for result in results:
        if result['fork'] == True:
            output.append(result['url'])
    return output

def delete_repo(urls, headers):
    for url in urls:
        response = requests.request("DELETE", url, headers=headers)
        if response.text == "":
            print("[DELETED] :: " + url )
        else:
            print("[Failed to delete] :: " + url )
            


if __name__ == '__main__':

    USER_ID = "" #Enter user id
    TOKEN = "" #Enter API key
    headers = {
    'Authorization': 'Bearer '+ TOKEN
    }
    
    delete_repo(forked_repos(USER_ID, headers),headers)

