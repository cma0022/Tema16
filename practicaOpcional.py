class practicaOpcional:

    cadena = ""

    def __init__(self, cadena):
        self.cadena = cadena

    def contarVocales(self) -> int:
        cont = 0
        for letra in self.cadena:
            # Recorremos todo el string letra por letra
            # Con el .lower() volvemos todas las letras minusculas y si son "aeiou" el contador suma 1
            if letra.lower() in "aeiou":
                cont += 1
        return cont
    
    def contarPalabras(self) -> int:
        # Con el meotodo .split() separamos las palabras de nuestro string y devuleve un array
        # Con el uso de len() devuelvo el numero de valores que tiene el array devuelto por el .split()
        return len(self.cadena.split())

