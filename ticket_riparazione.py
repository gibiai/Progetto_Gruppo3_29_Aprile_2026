class TicketRiparazione:

    def __init__(self, id_ticket, elettrodomestico):
        self.__id_ticket = id_ticket
        self.__elettrodomestico = elettrodomestico
        self.__stato = "aperto"
        self.__note = []

    def get_id_ticket(self):
        return self.__id_ticket

    def get_elettrodomestico(self):
        return self.__elettrodomestico

    def get_stato(self):
        return self.__stato

    def set_stato(self, stato):
        self.__stato = stato

    def aggiungi_nota(self, testo):
        self.__note.append(testo)

    def calcola_preventivo(self, *voci_extra):
        totale = self.__elettrodomestico.stima_costo_base()
        totale += sum(voci_extra)
        return totale