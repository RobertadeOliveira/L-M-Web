class Carro:
    def __init__(this,nomeCarro):
        this.nomeCarro = nomeCarro
        print(nomeCarro)

    def acao(self):
        print(f'{self.nomeCarro} é o seu Carro!')
    
carro = Carro('Chevrolet') 
Carro.acao(carro)