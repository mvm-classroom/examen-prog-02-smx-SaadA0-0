#Generador de noms incorrectes per Timothée Chalamet

# Posa aquí qualsevol import que necessitis com rand, math, time...
import random

def obtenir_nom():
    #Llista de noms incorrectes
    noms = ["Timotei", "Timonel", "Timbaler", "Tennebaum", "TaoPaiPai", "Teruel", "Tirolés", "Traginer", "Tourmalet"]
    # Llista de cognoms incorrectes
    cognoms = ["Chandalet", "Camembert", "Sabadell", "Chevrolet", "Caganer", "Bechamel", "Casteller", "Churumbel", "Cafeaulait", "Crivillé", "Charmander"]

    return(f"{random.choice(noms)} {random.choice(cognoms)}") # Estic fent servir el random per crea un nom aleatori separat amb un esapai

def afegir_nom(llista):
    # Hem d'obtenir un nom aleatori, afegir-lo a la llista i mostrar per pantalla que hem afegit aquest nom
    nom = obtenir_nom()
    print('     ')
    print(f"        Acabem de afegir aquest nom === {nom}")

    llista.append(nom) # Afegint el valor a l'llista


def llistar_noms(llista):
    print('     ')
    for noms in llista:
            print(f'            {noms}')
    # Hem de mostrar per pantalla tots els noms que hem afegit a la llista



def ordenar_noms(llista):
    llista.sort()
    print(f"")
    for noms in llista:
        print(f" llista Ordenada:   {noms}")
    # Hem d'ordenar la llista de noms
    # Un cop ordenada la llista, llistem tots els noms



def mostrar_menu():
    print('____________________')
    print('                     ')
    print("[A] Afegir valor: ")
    print("[L] Llista Noms: ")
    print("[O] Ordenar llista: ")
    print("[F] FInalitzar: ")
    print('____________________')
    # Hem de mostrar el menú que ens demanen a l'enunciat



def demanar_opcio():
    menu_correcte= ['a','l','o','f']
    valor_correcte= False
    mostrar_menu()
    while not valor_correcte:
        print('     ')
        valor= input(' Selecionar una opcio: ').lower()
        if valor not in menu_correcte:
            mostrar_menu()
            print('     ')
            print('El valor no es correcte')
        else:
            valor_correcte = True
    return valor

    # Retornarem l'opció correcta sel.leccionada        


def gestionar_opcio(opcio, llista):
    finalitzar= False
    match opcio:
        case 'a':
            afegir_nom(llista)
        case 'l':
            llistar_noms(llista)
        case 'o':
            ordenar_noms(llista)
        case 'f':
            print('Gracies per fer servir el nostre generador')
            finalitzar= True
    return finalitzar


    # En funció de l'opció escollida per l'usuari, haurem de cridar a les funcions adients per fer el que ens demanen
    # Heu de fer servir `match`
    # Si no ho sabeu fer amb `match` podeu utilitzar altres estructures condicionals però no obtindreu tota la puntuació    



# Programa principal
llista = []
finalitzar= False
while not finalitzar: 
    valor=demanar_opcio()
    finalitzar = gestionar_opcio(valor, llista)


# Heu de treballar amb una llista a la que li farem diverses operacions mostrades al menú
# Si ens introdueixen l'opció "F" acabarem el programa
# Si no ens introdueixen l'opció "F" farem l'acció corresponent i tornarem a preguntar
