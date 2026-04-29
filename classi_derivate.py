from elettrodomestico import Elettrodomestico

class Lavatrice(Elettrodomestico):

    def __init__(self, marca, modello, anno_acquisto, guasto, capacita_kg, giri_centrifuga):
        super().__init__(marca, modello, anno_acquisto, guasto)
        self.__capacita_kg = capacita_kg
        self.__giri_centrifuga = giri_centrifuga

    def get_capacita_kg(self):
        return self.__capacita_kg

    def get_giri_centrifuga(self):
        return self.__giri_centrifuga

    def descrizione(self):
        return f"{self.marca} {self.modello} ({self.anno_acquisto}) — Guasto: {self.guasto}"

    def stima_costo_base(self):
        if self.__capacita_kg > 8:
            return 90
        return 60


class Frigorifero(Elettrodomestico):

    def __init__(self, marca, modello, anno_acquisto, guasto, litri, ha_freezer):
        super().__init__(marca, modello, anno_acquisto, guasto)
        self.__litri = litri
        self.__ha_freezer = ha_freezer

    def get_litri(self):
        return self.__litri

    def get_ha_freezer(self):
        return self.__ha_freezer

    def descrizione(self):
        return f"{self.marca} {self.modello} ({self.anno_acquisto}) — Guasto: {self.guasto}"

    def stima_costo_base(self):
        base = 70
        if self.__ha_freezer:
            base += 20
        if self.__litri > 300:
            base += 15
        return base


class Forno(Elettrodomestico):

    def __init__(self, marca, modello, anno_acquisto, guasto, tipo_alimentazione, ha_ventilato):
        super().__init__(marca, modello, anno_acquisto, guasto)
        self.__tipo_alimentazione = tipo_alimentazione
        self.__ha_ventilato = ha_ventilato

    def get_tipo_alimentazione(self):
        return self.__tipo_alimentazione

    def get_ha_ventilato(self):
        return self.__ha_ventilato

    def descrizione(self):
        return f"{self.marca} {self.modello} ({self.anno_acquisto}) — Guasto: {self.guasto}"

    def stima_costo_base(self):
        base = 65
        if self.__tipo_alimentazione == "gas":
            base += 25
        if self.__ha_ventilato:
            base += 10
        return base