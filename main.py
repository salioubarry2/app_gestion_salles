from datta.dao_salle import DataSalle
from models.salle import Salle

dao = DataSalle()

try:
    connexion = dao.get_connection()
    print("Connexion réussie")
    connexion.close()
except Exception as e:
    print("Erreur connexion :", e)


s1 = Salle("C22", "Salle Programmeur", "Laboratoire", 35)
dao.insert_salle(s1)
print("Salle ajoutée")


s1.description = "Salle reseautique"
s1.capacite = 50
dao.update_salle(s1)
print("Salle modifiée")


salle_trouvee = dao.get_salle("C22")
if salle_trouvee:
    print(salle_trouvee.afficher_infos())


liste = dao.get_salles()
for x in liste:
    print(x.afficher_infos())


dao.delete_salle("C22")
print("Salle supprimée")