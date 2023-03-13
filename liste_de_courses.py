
choix = [
    ": Ajouter un élément à la liste de courses",
    ": Retirer un élement de la liste de courses",
    ": Afficher les éléments de la liste de courses",
    ": Vider la liste de courses",
    ": Quitter le programme",
]
liste_courses = []
while True :
    print("Choississez parmis les 5 options suivante : ")
    for i, element in enumerate(choix, start= 1):
        print(i, element)
    a=""
    if a not in ["1","2","3","4","5"]:
        a = input("votre choix : ")
        if a not in ["1","2","3","4","5"]:
            print("Veuillez choisir une option valide...")
    #Ajouter
    if a == "1":
        b = input("Entrez le nom d'un élément à ajouter à la liste de courses : ")
        liste_courses.append(b)
        print(f"L'élément {b} à bien été ajouté à la liste")
    #Retirer
    elif a == "2":
        b = input("Entrez le nom d'un élément à retirer de la liste de courses : ")
        liste_courses.remove(b)
        print(f"L'élément {b} à bien été supprimé de la liste")
    #afficher
    elif a == "3":
        if bool(liste_courses) == False :
            print("Votre liste ne content aucun élément.")
        else:
            print("Voici le contenu de votre liste : ")
            for i, courses in enumerate(liste_courses, start=1):
                print(str(i)+".", courses)
    #Vider
    elif a == "4":
        liste_courses.clear()
        print("La liste à bien été vidée de son contenu")
    #Quitter
    elif a == "5":
        print("À bientôt")
        break