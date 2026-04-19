from models.salle import Salle
from services.service_salle import ServiceSalle

service = ServiceSalle()

salle1 = Salle("A21", "Salle informatique", "Laboratoire", 60)
ok, message = service.ajouter_salle(salle1)
print(message)

salle2 = Salle("A21", "Salle informatique principale", "Laboratoire", 95)
ok, message = service.modifier_salle(salle2)
print(message)


resultat = service.rechercher_salle("A101")
if resultat:
    print(resultat.afficher_infos())
liste = service.recuperer_salle()
for salle in liste:
    print(salle.afficher_infos())


ok, message = service.supprimer_salle("A21")
print(message)