#Autor: Sebastián Triana

#Estos son ejercicios con clases

#Perros y Gatos

class Perro:
    def __init__(self, raza, color):
        self.raza = raza
        self.color = color


    def ladrar(self):
        print("GUAAAAAAAUU GUAAAUUU!!!!")

class Gato:
    def __init__(self, raza, color):
        self.raza = raza
        self.color = color

    def maullar(self):
        print("MIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAUUUUUUUUUUUUUUUU!!!!")

def main():
    raza_perro = input("Ingrese la raza de su perro: ")
    color_perro = input("Ingrese el color de su perro: ")
    mi_perro = Perro(raza_perro, color_perro)
    mi_perro.ladrar()

    raza_gato = input("Ingrese la raza de su gato: ")
    color_gato = input("Ingrese el color de su gato: ")
    mi_gato = Gato(raza_gato, color_gato)
    mi_gato.maullar()

main()
