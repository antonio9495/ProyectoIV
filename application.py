from flask import *
from src.Prueba import Prueba
import json
app=Flask(__name__)

prueba = Prueba("data/datos.json")

@app.route("/", methods=['GET'])
def index():
    return jsonify(status='OK')

@app.route("/status", methods=['GET'])
def status():
    return jsonify(status='OK')

    
@app.route('/getInfoDato/<idobjeto>',methods=['GET'])
def getInfoDato(idobjeto):
    datoMuestra = prueba.getInfoDato(idobjeto)
    return jsonify(datoMuestra)

@app.route('/searchP/<idPos>',methods=['GET'])
def searchP(idPos):
    if((prueba.buscarPosicion(idPos))[0]):
        dataP = json.dumps((prueba.buscarPosicion(idPos))[1])
        dataP += "actividades asociadas a la posicion "
        for p in (prueba.ActividadesAsociadasAposicion(idPos))[1]:
            dataP += p
            dataP += " "
        return jsonify(dataP)
    else:
        return jsonify("No existe una posición con ese valor.")

@app.route('/searchA/<idAct>',methods=['GET'])
def searchA(idAct):
    if((prueba.buscarActividad(idAct))[0]):
        dataA = json.dumps((prueba.buscarActividad(idAct))[1])
        dataA += "posiciones asociadas a la actividad "
        for a in (prueba.PosicionesAsociadasAactividades(idAct))[1]:
            dataA += a
            dataA += " "
        return jsonify(dataA)
    else:
        return jsonify("No existe una actividad con ese valor.")




if __name__ == "__main__":
  app.run(debug = True, host='0.0.0.0')
