import json

#Ejecución de Pytest: pytest-3 prubapytest.py
class Prueba:
    datos=[]
    def __init__(self):
        with open('datos.json') as f:
            self.datos = json.load(f)

    def getInfoDato(self, id):
        if(id in self.datos):
            info = "Información completa del dato: " + id +"\n"
            info += "Información de la actividad :\n"
            info += "\tIdentificador de actividad: " +  self.datos[id]["Actividad"]["idA"]
            info += "\n\tTitulo de la actividad: " + self.datos[id]["Actividad"]["titulo"]
            info += "\n\tTipo de la actividad: " + self.datos[id]["Actividad"]["tipo"]
            info += "\n\tPosiciones asociada: "
            for a in (self.PosicionesAsociadasAactividades(self.datos[id]["Actividad"]["idA"]))[1]:
                info += a
                info += " ,"
            info += "\nInformación de la posición :\n"
            info += "\tIdentificador de la posición: " +  self.datos[id]["Posicion"]["idP"]
            info += "\n\tTitulo de la actividad: " + self.datos[id]["Posicion"]["latitud"]
            info += "\n\tTipo de la actividad: " + self.datos[id]["Posicion"]["longitud"]
            info += "\n\tActividades asociada: "
            for a in (self.ActividadesAsociadasAposicion(self.datos[id]["Posicion"]["idP"]))[1]:
                info += a
                info += " ,"
            info+="\n"
        else:
            info ="No existe un objeto con ese id"
        return info

    def buscarPosicion(self, idp):
        for a in self.datos:
            if(self.datos[a]["Posicion"]["idP"] == idp):
                return (True, self.datos[a]["Posicion"])
        return (False, None)

    def buscarActividad(self, ida):
        for a in self.datos:
            if(self.datos[a]["Actividad"]["idA"] == ida):
                return (True, self.datos[a]["Actividad"])
        return (False, None)

    def ActividadesAsociadasAposicion(self, idp):
        posiciones = []
        if ( (self.buscarPosicion(idp))[0] == True ):
            for a in self.datos:
                if(self.datos[a]["Posicion"]["idP"] == idp):
                    posiciones.append(self.datos[a]["Actividad"]["idA"])
            return (True, posiciones)
        else:
            return (False, None)

    def PosicionesAsociadasAactividades(self, ida):
        posiciones = []
        if ( (self.buscarActividad(ida))[0] == True ):
            for a in self.datos:
                if(self.datos[a]["Actividad"]["idA"] == ida):
                    posiciones.append(self.datos[a]["Posicion"]["idP"])
            return (True, posiciones)
        else:
            return (False, None)


    def crearObjeto(self, actividad, coordenadas):
        id = -1
        dictA ={"idA": "None", "tipo": "None", "titulo": "None" }
        dictP ={"idP": "None","latitud": "None","longitud": "-None"}

        if( type(actividad) == dict and type(coordenadas) == dict):
            if(dictA.keys() == actividad.keys() and dictP.keys() == coordenadas.keys()):
                id = "idobjeto"+ str(len(self.datos)+1)
                self.datos[id] = {"Posicion": {"idP":coordenadas["idP"],"latitud":coordenadas["latitud"],"longitud":coordenadas["longitud"]},
                                    "Actividad": {"idA":actividad["idA"],"tipo":actividad["tipo"],"titulo":actividad["titulo"]}}
        return id
