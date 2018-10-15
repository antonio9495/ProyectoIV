from Prueba import Prueba


def testTrue():
    prueba = Prueba()
    assert  prueba.devuelveTrue() == True, "Devolución de True"

def testgetMapId():
    prueba = Prueba()
    assert  prueba.getTipoActividad() == "Deporte", "correcto"
