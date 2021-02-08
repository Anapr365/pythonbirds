class Pessoa:
    def __init__(self, *filhos,  nome = None, idade=40):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)
    def cumprimentar(self):
        return f'Ola {id(self)}'



if __name__ == '__main__':
    Ana = Pessoa(nome='Ana')
    Paula = Pessoa(Ana, nome= 'paula')
    print(Pessoa.cumprimentar(Paula))
    print(id(Paula))
    print(Paula.cumprimentar())
    print(Paula.nome)
    print(Paula.idade)
    for filho in  Paula.filhos:
        print(filho.nome)
    Paula.sobrenome = 'Rosa'
    del Paula.filhos
    print(Paula.__dict__)
    print(Ana.__dict__)

