from practicaOpcional import practicaOpcional

def test_contarVocales():
    # Creamos un objeto cadena con el constructor de la clase practicaOpcional
    # y le pasamos una cadena. En este caso tiene 17 vocales.
    cadena = practicaOpcional("Hola MAurIcio, ErEs mas feO que Un Nabo.")
    assert cadena.contarVocales() == 17

def test_contarPalabras():
    # Creamos un objeto cadena con el constructor de la clase practicaOpcional
    # y le pasamos una cadena. En este caso tiene 20 palabras.
    cadena = practicaOpcional("Esta oracion tiene cinco palabras. Sumando las siete de esta, son un total, de quince. Mas estas. ¿Son veinte no?")
    assert cadena.contarPalabras() == 20
