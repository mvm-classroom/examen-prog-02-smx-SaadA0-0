#Generador de noms incorrectes per Timothée Chalamet

# Posa aquí qualsevol import que necessitis com rand, math, time...
import random

def obtenir_nom():
    #Llista de noms incorrectes
    noms = ["Timotei", "Timonel", "Timbaler", "Tennebaum", "TaoPaiPai", "Teruel", "Tirolés", "Traginer", "Tourmalet"]
    # Llista de cognoms incorrectes
    cognoms = ["Chandalet", "Camembert", "Sabadell", "Chevrolet", "Caganer", "Bechamel", "Casteller", "Churumbel", "Cafeaulait", "Crivillé", "Charmander"]
    return(f"{random.choice(noms)} {random.choice(cognoms)}")


def afegir_nom(llista):
    print("PENDENT: afegir_nom")
    # Hem d'obtenir un nom aleatori, afegir-lo a la llista i mostrar per pantalla que hem afegit aquest nom

def llistar_noms(llista):
    print("PENDENT: llistar_noms")
    # Hem de mostrar per pantalla tots els noms que hem afegit a la llista

def ordenar_noms(llista):
    print("PENDENT: ordenar_noms")
    # Hem d'ordenar la llista de noms
    # Un cop ordenada la llista, llistem tots els noms

def mostrar_menu():
    print("PENDENT: mostrar_menu")
    # Hem de mostrar el menú que ens demanen a l'enunciat

def demanar_opcio():
    print("PENDENT: demanar_opcio")
    # Hem de demanar a l'usuari una de les opcions del menú
    # Si ens introdueix un valor incorrecte hem de tornar a mostrar el menú i tornar a demanar opció
    # Si ens introdueix la lletra correcta en minúscula, la donarem per bona
    # Retornarem l'opció correcta sel.leccionada        

def gestionar_opcio(opcio, llista):
    print("PENDENT: gestionar_opcio")
    # En funció de l'opció escollida per l'usuari, haurem de cridar a les funcions adients per fer el que ens demanen
    # Heu de fer servir `match`
    # Si no ho sabeu fer amb `match` podeu utilitzar altres estructures condicionals però no obtindreu tota la puntuació    



# Programa principal

obtenir_nom()
# Heu de treballar amb una llista a la que li farem diverses operacions mostrades al menú
# Si ens introdueixen l'opció "F" acabarem el programa
# Si no ens introdueixen l'opció "F" farem l'acció corresponent i tornarem a preguntar
