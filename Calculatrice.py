def message():
  print('Bienvenue sur la mini-calculatrice !')

def nombre_utilisateur():
  num1 = float(input('Veuillez saisir un  premier nombre :'))
  num2 = float(input('Veuillez saisir un  deuxième nombre :'))
  return num1, num2

def Menue():
    print("=== Menu ===")
    print('1. Addition')
    print('2. Soustraction')
    print('3. Division')
    print('4. Multiplication')

    choix_utilisateur = input('Choisissez votre opération : ')

    while choix_utilisateur not in ["1", "2", "3", "4"]:
        choix_utilisateur = input('Veuillez saisir un nombre valide : ')
    return choix_utilisateur

def adition(a, b):
  return a + b

def soustraction(a, b):
  return a - b

def multiplication(a, b):
  return a * b

def division(a, b):
  if b !=0:
    return a / b
  else:
     print('Erreur: division impossible par zéro !')

def démarage_calculatrice(choix_utilisateur):
  num1, num2 = nombre_utilisateur()
  match choix_utilisateur:
    case '1':
      resultat = adition(num1,num2)
    case '2':
      resultat = soustraction(num1,num2)
    case '3':
      resultat = division(num1,num2)
    case '4':
      resultat = multiplication(num1,num2)
    case _:
      print("choix invalide:")
  return resultat

if __name__ == '__main__': 
  message()
  choix_utilisateur = Menue()
  resultat = démarage_calculatrice(choix_utilisateur)
  print(resultat)
