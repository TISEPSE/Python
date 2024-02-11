while True:

  def salaire_mensuel(salaire_annuel):
      return salaire_annuel / 12
  
  def salaire_hebdomadaire(salaire_mensuel):
      return salaire_mensuel / 4
  
  def salaire_horaire(salaire_hebdomadaire, heures_travaillees):
      return salaire_hebdomadaire / heures_travaillees
    
  def main():
    salaire_annuel = int(input("Quelle est votre salaire annuel ? : ")) 
    heure_travaille = int(input("Quel est votre nombre d'heure par semaine ? : "))
    salaire_hebdo = salaire_hebdomadaire(salaire_mensuel(salaire_annuel))
    salaire_horaire_result = salaire_horaire(salaire_hebdo, heure_travaille)
    salaire_mensuel_val = salaire_mensuel(salaire_annuel)
    print("Votre salaire mensuel est de", salaire_mensuel_val, "euros et votre salaire horaire est de", salaire_horaire_result, "euros")
    
  main()