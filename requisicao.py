import requests
import datetime as dt


class Repositorio:
    def __init__(self, usuario):
        self.usuario = usuario
        self.colecao = []

    def requisita(self):
        resposta = requests.get(f'https://api.github.com/users/{self.usuario}/repos')

        if resposta.status_code == 200:
            conteudo = resposta.json()

            if type(conteudo) is not int:
                for i in range(len(conteudo)):
                    name = conteudo[i]['name']
                    link_github = conteudo[i]['owner']['html_url']
                    link_repos = conteudo[i]['svn_url']
                    last_com = conteudo[i]['pushed_at'][:10]

                    data = dt.datetime.strptime(last_com, "%Y-%m-%d")
                    data_f = dt.datetime.strftime(data, "%d/%m/%Y")

                    language = conteudo[i]['language']
                    disabled = conteudo[i]['disabled']
                    archived = conteudo[i]['archived']
                    description = conteudo[i]['description']

                    # print("Nome: ", name)
                    # print("Descrição: ", description)
                    # print("Link do GitHub: ", link_github)
                    # print("Link do Repositório: ", link_repos)
                    # print("Data: ", data, type(data))
                    # print("Data Formatada: ", data_f, type(data_f))
                    # # print("Último Commit: ", last_com, type(last_com))
                    # print("Language: ", language)
                    # print("Disabled: ", disabled)
                    # print("Archived: ", archived)
                    # print()

                    dicionario = {"nome": name, "descricao": description, "github": link_github,
                                  "link_repos": link_repos, "data": data, "data_f": data_f,
                                  "language": language, "disabled": disabled, "archived": archived}

                    self.colecao.append(dicionario)

            else:
                print(conteudo)

        else:
            print(resposta.status_code)

        print(self.colecao)
        return self.colecao


repositorios = Repositorio("ViniciusFebasse")
repositorios.requisita()