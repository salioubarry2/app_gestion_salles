import json

import mysql.connector

from models.salle import Salle

class DataSalle:

    def __init__(self):

        pass

    def get_connection(self):

        with open("data/config.json", "r", encoding="utf-8") as fichier:

            config = json.load(fichier)

        connexion = mysql.connector.connect(

            host=config["host"],
            user=config["user"],
            password=config["Python2026"],
            database=config["db_salles"]

        )

        return connexion