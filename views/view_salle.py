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
