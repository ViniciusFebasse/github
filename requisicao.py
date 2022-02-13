import requests
import shutil
import json
import datetime


class Repositorio:
    def __init__(self, usuario):
        self.usuario = usuario

    def requisita(self):
        resposta = requests.get(f'https://api.github.com/users/{self.usuario}/repos')

        if resposta.status_code == 200:
            conteudo = resposta.json()

            if type(conteudo) is not int:
                for i in range(len(conteudo)):
                    print("Name: ", conteudo[i]['name'])
                    print("Link do GitHub: ", conteudo[i]['owner']['html_url'])
                    print("Link do Repositório: ", conteudo[i]['svn_url'])
                    print("Último Commit: ", conteudo[i]['pushed_at'])
                    print("Language: ", conteudo[i]['language'])
                    print("Disabled: ", conteudo[i]['disabled'])
                    print("Archived: ", conteudo[i]['archived'])
                    print()
            else:
                print(conteudo)

        else:
            print(resposta.status_code)


repositorios = Repositorio("ViniciusFebasse")
repositorios.requisita()