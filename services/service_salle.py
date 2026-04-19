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
    def modifier_salle(self, salle):
        if not salle.code or not salle.description or not salle.categorie or salle.capacite is None:
            return False, "Tous les champs sont obligatoires."
        if int(salle.capacite) < 1:
            return False, "La capacité doit être supérieure ou égale à 1."
        salle_existante = self.dao_salle.get_salle(salle.code)
        if not salle_existante:
            return False, "La salle à modifier n'existe pas."
        self.dao_salle.update_salle(salle)
        return True, "Salle modifiée avec succès."

    def supprimer_salle(self, code):

        salle_existante = self.dao_salle.get_salle(code)
        if not salle_existante:
            return False, "Salle introuvable."
        self.dao_salle.delete_salle(code)
        return True, "Salle supprimée avec succès."

    def rechercher_salle(self, code):

        return self.dao_salle.get_salle(code)
    def recuperer_salles(self):
        return self.dao_salle.get_salles()
