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
    # Hem d'obtenir un nom aleatori, afegir-lo a la llista i mostrar per pantalla que hem afegit aquest nom
    nom = obtenir_nom()
    print(f"Acabem de afegir aquest nom {nom}")
    llista.append(nom)


def llistar_noms(llista):
    for noms in llista:
        print(f'Ara mateix tenim aquests noms en la llista {noms}')
    # Hem de mostrar per pantalla tots els noms que hem afegit a la llista



def ordenar_noms(llista):
    llista.sort()
    print(f"llista ordenada {llista}")
    # Hem d'ordenar la llista de noms
    # Un cop ordenada la llista, llistem tots els noms



def mostrar_menu():
    print("[A] Afegir valor: ")
    print("[L] Afegir valor: ")
    print("[O] Afegir valor: ")
    print("[F] FInalitzar: ")
    # Hem de mostrar el menú que ens demanen a l'enunciat



def demanar_opcio():
    menu_correcte= ['a','l','o','f']
    valor_correcte= False
    mostrar_menu()
    while not valor_correcte:
        valor= input('Selecionar una opcio: ').lower()
        print(valor)
        if valor not in menu_correcte:
            mostrar_menu()
            print('El valor no es correcte')
        else:
            valor_correcte = True
    return valor

    # Retornarem l'opció correcta sel.leccionada        


def gestionar_opcio(opcio, llista):
    finalitzar= False
    match opcio:
        case 'a':
           obtenir_nom()
        case 'l':
            llistar_noms(llista)
        case 'o':
            ordenar_noms(llista)
        



    # En funció de l'opció escollida per l'usuari, haurem de cridar a les funcions adients per fer el que ens demanen
    # Heu de fer servir `match`
    # Si no ho sabeu fer amb `match` podeu utilitzar altres estructures condicionals però no obtindreu tota la puntuació    



# Programa principal

gestionar_opcio()

# Heu de treballar amb una llista a la que li farem diverses operacions mostrades al menú
# Si ens introdueixen l'opció "F" acabarem el programa
# Si no ens introdueixen l'opció "F" farem l'acció corresponent i tornarem a preguntar
