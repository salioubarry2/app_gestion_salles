from datta.dao_salle import DataSalle


class ServiceSalle:
    def __init__(self):
        self.dao_salle = DataSalle()

    def ajouter_salle(self, salle):
        if not salle.code or not salle.description or not salle.categorie or salle.capacite is None:
            return False, "Tous les champs sont obligatoires."
        if int(salle.capacite) < 1:
            return False, "La capacité doit être supérieure ou égale à 1."
        salle_existante = self.dao_salle.get_salle(salle.code)
        if salle_existante:
            return False, "Une salle avec ce code existe déjà."
        self.dao_salle.insert_salle(salle)
        return True, "Salle ajoutée avec succès."