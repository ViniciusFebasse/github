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
                    print()
                    print(conteudo[i])
                    print()
                    print(conteudo[i]['name'])
            else:
                print(conteudo)

        else:
            print(resposta.status_code)


repositorios = Repositorio("ViniciusFebasse")
repositorios.requisita()