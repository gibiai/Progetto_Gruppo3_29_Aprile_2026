from elettrodomestico import Elettrodomestico # importo la classe astratta base nel modulo elettrodomestico.py

class Lavatrice(Elettrodomestico): # Ereditarietà - eredita da Elettrodomestico

    def __init__(self, marca, modello, anno_acquisto, guasto, capacita_kg, giri_centrifuga): # costruttore ricevei i parametri base + quelli specifici della lavatrice
        super().__init__(marca, modello, anno_acquisto, guasto) # chiamo il costruttore della classe madre con tutti i suoi attributi e controlli
        self.__capacita_kg = capacita_kg # attributi specifici lavatrice
        self.__giri_centrifuga = giri_centrifuga

    def get_capacita_kg(self): # serie di getter per accedere e leggere attributi privati
        return self.__capacita_kg

    def get_giri_centrifuga(self):
        return self.__giri_centrifuga

    def descrizione(self): # override del metodo astratto descrizione() della classe madre — polimorfismo / obbligato implementarlo perchè abstractmethod
        return f"{self.marca} {self.modello} ({self.anno_acquisto}) — Guasto: {self.guasto}" # self.marca, self.modello ecc. senza underscore: sto chiamando i @property

    def stima_costo_base(self): # override del metodo astratto stima_costo_base() — polimorfismo - restituisce un costo diverso in base alle proprie caratteristiche
        if self.__capacita_kg > 8:
            return 90
        return 60


class Frigorifero(Elettrodomestico): # Frigorifero eredita da Elettrodomestico — ereditarietà

    def __init__(self, marca, modello, anno_acquisto, guasto, litri, ha_freezer): # costruttore: parametri base + specifici del frigorifero
        super().__init__(marca, modello, anno_acquisto, guasto) # delego i parametri base alla classe madre tramite super()
        # attributi privati specifici del frigorifero — incapsulamento (litri & ha_frezeer)
        self.__litri = litri
        self.__ha_freezer = ha_freezer # booleano: True se ha il freezer

    def get_litri(self): # serie di getter per accedere e leggere attributi privati
        return self.__litri

    def get_ha_freezer(self):
        return self.__ha_freezer

    def descrizione(self): # override del metodo astratto descrizione() — polimorfismo
        return f"{self.marca} {self.modello} ({self.anno_acquisto}) — Guasto: {self.guasto}"

    def stima_costo_base(self): # override del metodo astratto stima_costo_base() — polimorfismo - stessa logica - comportamento diverso
        base = 70
        if self.__ha_freezer:
            base += 20
        if self.__litri > 300:
            base += 15
        return base


class Forno(Elettrodomestico): # Forno eredita da Elettrodomestico — ereditarietà

    def __init__(self, marca, modello, anno_acquisto, guasto, tipo_alimentazione, ha_ventilato): # costruttore: parametri base + specifici del forno
        super().__init__(marca, modello, anno_acquisto, guasto) # delego i parametri base alla classe madre tramite super()
        # attributi privati specifici del forno — incapsulamento ( alimentazione & ha_ventilato )
        self.__tipo_alimentazione = tipo_alimentazione # stringa: "elettrico" o "gas"
        self.__ha_ventilato = ha_ventilato # booleano: True se ventilato

    def get_tipo_alimentazione(self): # serie di getter
        return self.__tipo_alimentazione

    def get_ha_ventilato(self):
        return self.__ha_ventilato

    def descrizione(self): # override del metodo astratto descrizione() — polimorfismo
        return f"{self.marca} {self.modello} ({self.anno_acquisto}) — Guasto: {self.guasto}"

    def stima_costo_base(self): # override del metodo astratto stima_costo_base() — polimorfismo
        base = 65
        if self.__tipo_alimentazione == "gas":
            base += 25
        if self.__ha_ventilato:
            base += 10
        return base
