while True: 
  nombre_a_gauche = input("Entrez un nombre : ")
  nombre_a_droite = input("Entrez un nombre : ")
  operation = input ("Quelle opération chef ? (+,-,*, ou /) : ")
  resultat = 0

  if not (nombre_a_gauche.isnumeric() and nombre_a_droite.isnumeric()):
    print("Erreur: les deux nombres doivent être des nombres entiers")

  else:
    a = int(nombre_a_gauche)
    b = int(nombre_a_droite)
    
    match operation:
     case '+':
       resultat = (a + b)
       print(resultat)
     case '-':
       resultat = (a - b)
       print(resultat)
     case '*':
       resultat = (a * b)
       print(resultat)
     case '/':
       if b != 0:
         resultat = (a / b)
         print(resultat)
       else:
         print("Erreur: division par zéro")
