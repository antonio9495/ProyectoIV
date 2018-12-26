import json, requests
from requests import *

url ="https://mysterious-bastion-92654.herokuapp.com/"

def testInicio():
    response = requests.get(url)
    assert response.status_code == 200, "Devuelve codigo correcto."
    assert response.json()['status'] == 'OK', "Devuelve estado correcto."

def testObtenerDatosObjeto():
    response = requests.get(url+"getInfoDato/1")
    assert response.status_code == 200, "Devuelve codigo correcto."
    assert response.json() == 'No existe un objeto con ese id', "Devuelve estado correcto."


def testObtenerPosicion():
    response = requests.get(url+"searchP/1")
    assert response.status_code == 200, "Devuelve codigo correcto."
    assert response.json() == 'No existe una posición con ese valor.', "Devuelve estado correcto."

def testObtenerActividad():
    response = requests.get(url+"searchA/1")
    assert response.status_code == 200, "Devuelve codigo correcto."
    assert response.json() == 'No existe una actividad con ese valor.', "Devuelve estado correcto."

def testCreateObject():
    payload = {
	   "act": {"idA":"Act1","tipo":"Deporte","titulo":"Ir al gimnasio"},
	   "post": {"idP":"Pos3","latitud":"37.197222","longitud":"-3.623889"}
       }
    response = requests.request("POST",url+"create", json=payload)

    assert response.status_code == 200, "Devuelve codigo correcto."
    assert response.json() != "No se ha podido crear el objeto ", "Devuelve estado correcto."
