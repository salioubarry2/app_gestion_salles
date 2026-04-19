import customtkinter as ctk
from tkinter import ttk, messagebox
from models.salle import Salle
from services.service_salle import ServiceSalle
class ViewSalle(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Gestion des salles")
        self.geometry("700x500")
        self.service_salle = ServiceSalle()

    #informationssalle
        self.cadreInfo = ctk.CTkFrame(self, corner_radius=10)
        self.cadreInfo.pack(pady=10, padx=10, fill="x")
        self.labelCode = ctk.CTkLabel(self.cadreInfo, text="Code :")
        self.labelCode.grid(row=0, column=0, padx=10, pady=10)
        self.entryCode = ctk.CTkEntry(self.cadreInfo)
        self.entryCode.grid(row=0, column=1, padx=10, pady=10)
        self.labelDescription = ctk.CTkLabel(self.cadreInfo, text="Description :")
        self.labelDescription.grid(row=1, column=0, padx=10, pady=10)
        self.entryDescription = ctk.CTkEntry(self.cadreInfo)
        self.entryDescription.grid(row=1, column=1, padx=10, pady=10)
        self.labelCategorie = ctk.CTkLabel(self.cadreInfo, text="Catégorie :")
        self.labelCategorie.grid(row=2, column=0, padx=10, pady=10)
        self.entryCategorie = ctk.CTkEntry(self.cadreInfo)
        self.entryCategorie.grid(row=2, column=1, padx=10, pady=10)
        self.labelCapacite = ctk.CTkLabel(self.cadreInfo, text="Capacité :")
        self.labelCapacite.grid(row=3, column=0, padx=10, pady=10)
        self.entryCapacite = ctk.CTkEntry(self.cadreInfo)
        self.entryCapacite.grid(row=3, column=1, padx=10, pady=10)

        #Cadre actions

        self.cadreActions = ctk.CTkFrame(self, corner_radius=10)
        self.cadreActions.pack(pady=10, padx=10, fill="x")
        self.btnAjouter = ctk.CTkButton(self.cadreActions, text="Ajouter", command=self.ajouter_salle)
        self.btnAjouter.grid(row=0, column=0, padx=10, pady=10)
        self.btnSupprimer = ctk.CTkButton(self.cadreActions, text="Supprimer", command=self.supprimer_salle)
        self.btnSupprimer.grid(row=0, column=1, padx=10, pady=10)
        self.btnModifier = ctk.CTkButton(self.cadreActions, text="Modifier", command=self.modifier_salle)
        self.btnModifier.grid(row=0, column=2, padx=10, pady=10)
        self.btnRechercher = ctk.CTkButton(self.cadreActions, text="Rechercher", command=self.rechercher_salle)
        self.btnRechercher.grid(row=0, column=3, padx=10, pady=10)

        # Cadre liste des salles

        self.cadreList = ctk.CTkFrame(self, corner_radius=10, width=400)

        self.cadreList.pack(pady=10, padx=10, fill="both", expand=True)

        self.treeList = ttk.Treeview(

            self.cadreList,

            columns=("code", "description", "categorie", "capacite"),

            show="headings"

        )

        self.treeList.heading("code", text="CODE")

        self.treeList.heading("description", text="Description")

        self.treeList.heading("categorie", text="Catégorie")

        self.treeList.heading("capacite", text="Capacité")
        self.treeList.column("code", width=80)
        self.treeList.column("description", width=180)
        self.treeList.column("categorie", width=120)
        self.treeList.column("capacite", width=100)
        self.treeList.pack(expand=True, fill="both", padx=10, pady=10)
        self.lister_salles()