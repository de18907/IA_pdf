import PyPDF2
from PIL import Image, ImageDraw, ImageFont
import os
import shutil
from os import remove
from os import path
lista1 = []
for i in range(100):
    primero = str(input("Escribe las palabras claves: "))
    primero.lower
    if primero == "salir sergio":
        break
    lista1.append(primero)
def pdf(lista = None):
    if lista !=None:
        print(f"Esta es tu lista: {lista}")
        pdf = []#array de todo los archivos
        def devolverArchivos(carpeta):
	        for archivo in os.listdir(carpeta):
		        pdf.append(os.path.join(carpeta,archivo))
        devolverArchivos("pdf/")#busca todo los archivos
        nuevo_pdf = []#array de claves
        def nuevoArchivos(carpeta):
	        for archivo in os.listdir(carpeta):
		        nuevo_pdf.append(os.path.join(carpeta,archivo))
        nuevoArchivos("palabras_claves/pdf/")#busca todo los archivos
        for od in pdf:
            pdfFileObj = open(od, 'rb')#imagen
            pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 
            paginas = pdfReader.numPages#cantidad de paginas
            nuevo = []#guardado en array
            palabras = []
            for x in range(paginas):
                pageObj = pdfReader.getPage(x)
                texto = pageObj.extractText()
                nuevo.append(texto)
            for i in range(paginas):
                ver = nuevo[i].split()
                palabras.append(ver)
            resultado = []
            tot = []
            total = []
            for po in lista:
                for numero in range(paginas):
                    for s in palabras[numero]:
                        if s.lower() == po.lower():
                            resultado.append(po)
            tot.append(set(resultado))
            for fg in tot:
                for f in fg:
                    total.append(od)
                    total.append(f)
            if total != []:
                print(f"Este es el arhivo {total[0]}")
                print(total)#Esto es lo que ves
                print("----------------------------------")
                for pd in nuevo_pdf:#eliminar archivos
                    print(pd)
                    if path.exists(pd):
                        remove(pd)
                shutil.copy(f"{total[0]}", f"palabras_claves/{total[0]}")#mover
pdf(lista1)
