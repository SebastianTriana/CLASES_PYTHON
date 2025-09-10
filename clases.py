#Autor: Sebastián Triana


#Estos son ejercicios con clases


#Caso de uso: Hacer al perro feliz(Darle comida juguetes y acariciarlo)


class Perro:
    def __init__(self, raza, color):
        self.raza = raza
        self.color = color


    def dar_juguete(self, juguete):
        if juguete == "S":
            return True
        if juguete == "N":
            return False
        return False


    def dar_comida(self, comida):
        if comida == "S":
            return True
        if comida == "N":
            return False
        return False


    def dar_acariciar(self, caricia):
        if caricia == "S":
            return True
        if caricia == "N":
            return False
        return False




def main():
    raza_perro = input("Ingrese la raza de su perro: ")
    color_perro = input("Ingrese el color de su perro: ")
    juguete = input("Dar juguete? S/N  ").upper()
    comida = input("Dar comida? S/N  ").upper()
    caricia = input("Acariciar? S/N  ").upper()


    mi_perro = Perro(raza_perro, color_perro)


    if mi_perro.dar_juguete(juguete) and mi_perro.dar_comida(comida) and mi_perro.dar_acariciar(caricia):
        print(f"Tu {raza_perro} de color {color_perro} está feliz!! GUAAAUU GUAUU")
    else:
        print(f"Tu {raza_perro} de color {color_perro} está más triste que 10 tristes.")


main()

