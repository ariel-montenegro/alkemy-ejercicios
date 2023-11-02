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
        


        

    
        