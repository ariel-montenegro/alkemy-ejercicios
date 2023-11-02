class Animal:
    cantidad_patas = 0
    vertebrado = True

    def comer():
        print('Estoy comiendo')
        
class Perro(Animal):
    
    def __init__(self, nombre, raza) -> None:
        self.nombre = nombre
        self.raza = raza
    
class Aguila(Animal):
    
    def volar():
        print('estoy volando')