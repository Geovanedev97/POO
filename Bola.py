class Bola:
    def __init__(self, cor, circuferencia, material):
        self.cor = cor
        self.circuferencia = circuferencia
        self.material = material

    def TrocaMaterial(self, novo_material):
        self.material = novo_material

bola1 = Bola("Azul", 12, 'couro')
bola1.TrocaMaterial("Plastico")
print(bola1.material)