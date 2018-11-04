from flask import *
from src.Prueba import Prueba
import json
app=Flask(__name__)

prueba = Prueba("data/datos.json")

@app.route('/')
def inicio():
    returnValue = {"status":"OK"}
    return jsonify(returnValue)

@app.route('/getInfoDato/<idobjeto>')
def getInfoDato(idobjeto):
    datoMuestra = prueba.getInfoDato(idobjeto)
    return datoMuestra

@app.route('/searchP/<idPos>')
def searchP(idPos):
    if((prueba.buscarPosicion(idPos))[0]):
        dataP = json.dumps((prueba.buscarPosicion(idPos))[1])
        dataP += "\n actividades asociadas a la posición"
        for p in (prueba.ActividadesAsociadasAposicion(idPos))[1]:
            dataP += p
            dataP += "\n"
        return dataP
    else:
        return ("No existe una posición con ese valor.")
@app.route('/searchA/<idAct>')
def searchA(idAct):
    if((prueba.buscarActividad(idAct))[0]):
        dataA = json.dumps((prueba.buscarActividad(idAct))[1])
        dataA += "\n posiciones asociadas a la actividad"
        for a in (prueba.PosicionesAsociadasAactividades(idAct))[1]:
            dataA += a
            dataA += "\n"
        return dataA
    else:
        return ("No existe una actividad con ese valor.")




if __name__ == "__main__":
  app.run(debug = True, host='0.0.0.0')
