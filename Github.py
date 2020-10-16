import requests
class Github:
    def __init__(self):
        self.api_url ='https://api.github.com'
        
    def getUser(self,username):
        response = requests.get(self.api_url + '/users/' + username)
        return response.json()

    def getRepo(self,username):
        response= requests.get(self.api_url + '/users/' + username + '/repos')
        return response.json()

    def createRepo(self,name,token):

        response = requests.post(self.api_url + '/user/repos?access_token=' + token,json={

                "name": name,
                "description": "This is your repository",
                "homepage": "https://github.com",
                "private": True,
                "has_issues": True,
                "has_projects": True,
                "has_wiki": True

        })

        return response.json()

github = Github()
while True:
    secim = input( '1-Find User \n2-Get Repositories \n3- Create Repository \n 4-Exit\n Seçim:')
    
    if secim == '4':
        break
    else:
        if secim == '1':
            username = input('username: ')
            result = github.getUser(username)
            print(f" name: {result['name']} public repos: {result['public_repos']} follower: {result['followers']}")
        elif secim == '2':
            username = input('username : ')
            result = github.getRepo(username)
            for repo in result:
                print(repo['name'])
          #  print(f"repositories: {result['repos']}")
        elif secim == '3':
            name = input('repo name: ')
            token = input('token id: ')
            result = github.createRepo(name,token)
            print(result)
        else:
            print('Yanlış bir seçim')