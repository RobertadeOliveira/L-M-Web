class Camera:
    def __init__(self, nome, filmando=False):
        self.nome = nome
        self.filmando = filmando

        print(f'Câmera {nome} criada!')
    
    def filmar(self):
        if self.filmando == False:
            self.filmando = True
            print(f'Câmera {self.nome} está filmando!')
            return
        print(f'A câmera {self.nome} já está em uso!')
    
    def fotografar(self):
        if self.filmando:
            print(f'A {self.nome} não pode fotografar no momento!')
            return
        print(f'Câmera {self.nome} está fotografando!')
        
    def para_filmar(self):
        if self.filmando:
            print(f'Câmera {self.nome} está parando de filmar!')
            self.filmando = False
            return
        print(f'Câmera {self.nome} não está filmando!')

c1 = Camera('Canon')
c1.filmar()
c1.filmar()
c1.fotografar()
c1.para_filmar()
c1.fotografar()

