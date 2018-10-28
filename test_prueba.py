from Prueba import Prueba

def testInicio():
    prueba = Prueba()
    assert type(prueba.datos["idobjeto1"]) is dict

def testGetInfoDato():
    prueba = Prueba()
    assert prueba.getInfoDato("noexiste") == "No existe un objeto con ese id", "correcto"
    assert prueba.getInfoDato("idobjeto1") != "No existe un objeto con ese id", "correcto"

def testBuscaDores():
    p = Prueba()
    assert (p.buscarPosicion("noexiste"))[0] == False, "no debe existir"
    assert (p.buscarPosicion("Pos1"))[0] == True, "no debe existir"
    assert (p.buscarActividad("noexiste"))[0] == False, "no debe existir"
    assert (p.buscarActividad("Act1"))[0] == True, "no debe existir"

def testAsociados():
    p = Prueba()
    assert (p.ActividadesAsociadasAposicion("noexiste"))[0] == False, "no existe la posicion"
    assert (p.ActividadesAsociadasAposicion("Pos1"))[0] == True, "Existe la posicion"
    assert len((p.ActividadesAsociadasAposicion("Pos1"))[1]) == 1, "La cantidad es correcta"
    assert (p.PosicionesAsociadasAactividades("noexiste"))[0]== False, "no existe la actividad"
    assert (p.PosicionesAsociadasAactividades("Act1"))[0] == True, "no existe la posicion"
    assert len((p.PosicionesAsociadasAactividades("Act1"))[1]) == 2, "La cantidad es correcta"

def testCrearObjeto():
    p=Prueba()
    id = p.crearObjeto({"idA": "Act1", "tipo": "Deporte", "titulo": "Ir al gimnasio" }, {"idP": "Pos3","latitud": "37.197222","longitud": "-3.623889"})
    assert (id==("idobjeto"+ str(len(p.datos)))), "se ha creado bien"
    id = p.crearObjeto({"idP": "Act1", "tipo": "Deporte", "titulo": "Ir al gimnasio" }, {"idP": "Pos3","latitud": "37.197222","longitud": "-3.623889"})
    assert (id == -1), "No se ha podido crear el objeto"
