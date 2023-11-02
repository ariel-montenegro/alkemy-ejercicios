class Bicicleta:
    
    velocidad = 0
    dos_ruedas = True
    
    def __init__(self, color, rodado, marca) -> None:
        self.color = color
        self.rodado = rodado
        self.marca = marca
        
    
    def avanzar(self):
        self.velocidad = 100
        
        
    def willy(self):
        self.dos_ruedas = False
        
    
    def frenar(self):
        self.velocidad = 0
        

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
        

    
        