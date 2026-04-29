from abc import ABC, abstractmethod
from datetime import datetime

class Elettrodomestico(ABC): # classe astratta

    def __init__(self, marca: str, modello: str, anno_acquisto: int, guasto: str): # costruttore con parametri, con controllo sull'anno di acquisto
        self.__marca = marca
        self.__modello = modello
        self.__anno_acquisto = anno_acquisto
        self.__guasto = guasto

    @property # getter e setter per marca, modello, anno_acquisto e guasto, con controllo sull'anno di acquisto
    def marca(self):
        return self.__marca

    @marca.setter
    def marca(self, valore):
        # Controllo: stringa non vuota
        if isinstance(valore, str) and valore.strip(): # strip() per rimuovere spazi bianchi all'inizio e alla fine
            self.__marca = valore.strip()
        else:
            raise ValueError("Errore: La marca deve essere una stringa valida.")

    @property
    def modello(self):
        return self.__modello

    @modello.setter
    def modello(self, valore):
        # Controllo: stringa non vuota
        if isinstance(valore, str) and valore.strip():
            self.__modello = valore.strip()
        else:
            raise ValueError("Errore: Il modello deve essere una stringa valida.")

    @property
    def anno_acquisto(self):
        return self.__anno_acquisto

    @anno_acquisto.setter # controllo sull'anno di acquisto, non può essere nel futuro
    def anno_acquisto(self, valore):
        if not isinstance(valore, int):
            raise ValueError("Errore: L'anno di acquisto deve essere un intero.")
        anno_attuale = datetime.now().year # otteniamo l'anno attuale usando datetime
        if valore <= anno_attuale:
            self.__anno_acquisto = valore # se l'anno è valido, lo assegniamo
        else:
            print(f"Errore: L'anno {valore} è nel futuro!")
            self.__anno_acquisto = anno_attuale

    @property
    def guasto(self):
        return self.__guasto

    @guasto.setter
    def guasto(self, valore): # controllo: stringa non vuota, altrimenti "Guasto non specificato"
        if isinstance(valore, str) and valore.strip():
            self.__guasto = valore.strip()
        else:
            self.__guasto = "Guasto non specificato"

    @abstractmethod
    def descrizione(self):
        pass

    @abstractmethod
    def stima_costo_base(self):
        pass
