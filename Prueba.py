import json

#Ejecución de Pytest: pytest-3 prubapytest.py
class Prueba:
    datos=[]
    def __init__(self):
        with open('datos.json') as f:
            self.datos = json.load(f)

    def devuelveTrue(self):
        return True

    def getTipoActividad(self):
        return self.datos["Actividad"]["tipo"]
