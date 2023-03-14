from parImpar import parImpar

def test_add():
    listaNum = parImpar([1,2,3,4,5,6,7,8,9,10])
    listaNum.add(5)
    assert len(listaNum.numeros) == 11

def test_sumarPar():
    listaNum = parImpar([1,2,3,4,5,6,7,8,9,10])
    assert listaNum.sumarPar() == 30

def test_sumaImpares():
    listaNum = parImpar([1,2,3,4,5,6,7,8,9,10])
    assert listaNum.sumaImpares() == 25

def test_cuadradoLista():
    listaNum = parImpar([1,2,3,4,5,6,7,8,9,10])
    assert listaNum.cuadradoLista() == [1,4,9,16,25,36,49,64,81,100]