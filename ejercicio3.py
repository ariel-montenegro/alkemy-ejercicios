"""Juan Lopez tiene 25 años y es de profesión Abogado. Por la
tarde, después de trabajar, sale a caminar. También tiene una
bicicleta amarilla marca “Massino” y a veces sale a dar
vueltas en ella."""

class Persona:
    
    def __init__(self, nombre, edad, profesion) -> None:
        self.nombre = nombre
        self.edad = edad
        self.profesion = profesion
    
    def trabajar(self):
        return 'Estoy trabajando'
    
    def caminar(self):
        return 'estoy caminando'
    
    def andar_bici(self, bicicleta):
        
        return bicicleta.pedalear()

class Bicicleta:
    
    def __init__(self, marca, color) -> None:
        self.marca = marca
        self.color = color
        
    
    def pedalear(self):
        return 'pedaleando'

persona1 = Persona('Juan Lopez', 25, 'abogado')
bici1 = Bicicleta('mazino', 'amarillo')

print(f'estoy {persona1.andar_bici(bici1)}')

