import time
import xml.etree.ElementTree as ET
import datetime


def fechaNow():
    now = datetime.datetime.now()
    fecha = now.strftime("%x")
    print(fecha)
    return fecha


class Notas:
    def __init__(self):
        self.notas = ET.Element('notas')
        self.nota = ET.SubElement(self.notas, 'nota')
        self.titulos = ET.SubElement(self.nota, 'Titulo')
        self.datos = ET.SubElement(self.nota, 'Datos')
        self.fecha = ET.SubElement(self.nota, 'Fecha')
        try:
            self.file = open("database.xml", "r")
        except:
            self.file = open("database.xml", "w")

    def insert(self):
        with open("database.xml", "r") as file:
            if file.read() != "":
                self.parse = ET.parse("database.xml")
                titulo = input("Que titulo desea?")
                self.titulos.text = titulo
                print()
                texto = input("Contenido de la nota")
                self.datos.text = texto
                self.fecha.text = fechaNow()

                self.parse.getroot().insert(0, self.nota)
                self.parse.write("database.xml")
            else:
                titulo = input("Que titulo desea?")
                self.titulos.text = titulo
                print()
                texto = input("Contenido de la nota")
                self.datos.text = texto
                self.fecha.text = fechaNow()

                with open("database.xml", "wb") as file:
                    ET.ElementTree(self.notas).write(file)

    def modify(self):
        self.parse = ET.parse("database.xml")
        print("Que nota desea cambiar introduzca su titulo:")
        elecc = input()
        comp = True
        for i in self.parse.getroot():
            for sub in i:
                if sub.tag == "Titulo":
                    if i.find('Titulo').text == elecc:
                        comp = False
                        print("Que desea modificar:\n"
                              "1- Titulo\n"
                              "2- Datos\n"
                              "3- Descripcion")
                        elecc2 = int(input())
                        if elecc2 == 2:
                            print("Introduzca: ")
                            elecc2text = input()
                            for elem in i.iter('Datos'):
                                elem.text = elecc2text
                        elif elecc2 == 1:
                            print("Introduzca: ")
                            elecc2text = input()
                            for elem in i.iter('Titulo'):
                                elem.text = elecc2text
                        elif elecc2 == 3:
                            print("Introduzca: ")
                            elecc2text = input()
                            for elem in i.iter('Fecha'):
                                elem.text = elecc2text
                        print("Cambio realizado correctamente: ")
                        print(i.find('Titulo').text)
                        print("-----------------------")
                        print(i.find('Datos').text)
                        print("-----------------------")
                        if i.find('Fecha').text != '':
                            print("Fecha: " + i.find('Fecha').text)

        self.parse.write("database.xml")
        if comp:
            print("No se han encontrado notas con ese titulo. (La busqueda por titulo es sensible a las mayusculas)")


    def search(self):
        self.parse = ET.parse("database.xml")
        print("Cual es el titulo de la nota?")
        elec = input()
        comprobar = True
        for i in self.parse.getroot():
            for sub in i:
                if sub.tag == "Titulo":
                    if i.find('Titulo').text == elec:
                        print("***********************")
                        print(i.find('Titulo').text)
                        print("-----------------------")
                        print(i.find('Datos').text)
                        print("-----------------------")
                        print("***********************")

                        comprobar = False
                        if i.find('Fecha').text != '':
                            print("Fecha: " + i.find('Fecha').text)

        if comprobar:
            print("No se han encontrado notas con ese titulo. (La busqueda por titulo es sensible a las mayusculas)")


    def showAll(self):
        self.parse = ET.parse("database.xml")
        a = 1
        for i in self.parse.getroot():

            for sub in i:
                if sub.tag == "Titulo":
                    print("***********************")
                    print(i.find('Titulo').text)
                    print("-----------------------")
                    print(i.find('Datos').text)
                    print("-----------------------")
                    if i.find('Fecha').text != '':
                        print("Fecha: " + i.find('Fecha').text)
                    print("***********************")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    database = Notas()
    exit = True
    bye = True
    while exit:
        print("*******************************************")
        print("¡Bienvenido a Notas!, ¿Qué desea hacer?\n"
              "1 - Crear una Nota\n"
              "2 - Mostrar todas las notas\n"
              "3 - Buscar nota por su titulo\n"
              "4 - Modificar una nota\n"
              "5 - Salir")
        print("*******************************************")
        print("* Introduzca el numero:")
        try:
            eleccion = int(input())
            if eleccion == 1:
                database.insert()
            elif eleccion == 2:
                database.showAll()
            elif eleccion == 3:
                database.search()
            elif eleccion == 4:
                database.modify()
            else:
                print("Good Byee")
                bye = False
                exit = False
                time.sleep(0.5)
            if bye:
                print("Desea hacer algo mas? Y/N")
                comprobador = input().upper()
                if comprobador != "Y" and comprobador != "YES" and comprobador != "SI" and comprobador != "S":
                    exit = False
        except:
            print("Error en la entrada, Por favor use solo numeros del 1 al 5")
            time.sleep(2.0)


