"""Juan Lopez tiene 25 años y es de profesión Abogado. Por la
tarde, después de trabajar, sale a caminar. También tiene una
bicicleta amarilla marca “Massino” y a veces sale a dar
vueltas en ella."""

class Persona:
    
    def __init__(self, nombre, edad, profesion) -> None:
        self.nombre = nombre
        self.edad = edad
        self.profesion = profesion
        
    def caminar():
        print('estoy caminando')
    
    def andar_bici():
        print('estoy andando en bici')        