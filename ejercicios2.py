class Animal:
    
    def __init__(self, cantidad_patas, tipo) -> None:
        self.cantidad_patas =cantidad_patas
        self.tipo = tipo
        
    def comer():
        print('Estoy comiendo')
        
class Perro(Animal):
    
    def __init__(self, nombre, raza, cantidad_patas, tipo) -> None:
        super().__init__(cantidad_patas, tipo)
        self.nombre = nombre
        self.raza = raza
    
class Aguila(Animal):
    
    def volar():
        print('estoy volando')