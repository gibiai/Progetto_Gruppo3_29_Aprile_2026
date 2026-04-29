# Entry point del programma
# il main non definisce classi — le importa e le usa
# importo tutto ciò che mi serve da ogni modulo (ciascun singolo file .py) del progetto
from elettrodomestico import Elettrodomestico       #  classe astratta base
from lavatrice import Lavatrice                     #  sottoclasse
from frigorifero import Frigorifero                 #  sottoclasse
from forno import Forno                             #  sottoclasse
from ticket_riparazione import TicketRiparazione    #  sottoclasse
from officina import Officina                       #  sottoclasse

# creo gli oggetti elettrodomestico
# nota: non posso scrivere Elettrodomestico(...) — è astratta (!!!) Python darebbe errore
# posso solo istanziare le sottoclassi concrete
l = Lavatrice("Samsung", "WW90T", 2020, "non centrifuga", 9, 1400)
f = Frigorifero("Bosch", "KGN36", 2018, "non raffredda", 320, True)
fo = Forno("Whirlpool", "AKZ96", 2021, "non scalda", "gas", True)

# creo i ticket associando ogni elettrodomestico al suo ticket
# TicketRiparazione riceve un oggetto generico — non sa se è Lavatrice, Frigorifero o Forno
# questo è fondamentale per il polimorfismo: la stessa classe gestisce tipi diversi
t1 = TicketRiparazione(1, l)
t2 = TicketRiparazione(2, f)
t3 = TicketRiparazione(3, fo)

# aggiungo note ai ticket 
t1.aggiungi_nota("Cuscinetto da sostituire")
t2.aggiungi_nota("Compressore rotto")

# calcolo i preventivi — polimorfismo in azione (!!!)
# calcola_preventivo() chiama stima_costo_base() internamente
# Python capisce da solo quale versione chiamare in base al tipo reale dell'oggetto:
# t1 → Lavatrice.stima_costo_base() → 90 (capacità > 8kg) + 30 + 15 = 135
# t2 → Frigorifero.stima_costo_base() → 70 + 20 (freezer) + 15 (>300L) + 100 = 205
# t3 → Forno.stima_costo_base() → 65 + 25 (gas) + 10 (ventilato) = 100
# *voci_extra è un parametro variadico: accetta zero o più argomenti aggiuntivi
print(t1.calcola_preventivo(30, 15))
print(t2.calcola_preventivo(100))
print(t3.calcola_preventivo())

# creo l'officina e aggiungo i ticket
officina = Officina("Riparazioni Napoli")
officina.aggiungi_ticket(t1)
officina.aggiungi_ticket(t2)
officina.aggiungi_ticket(t3)

# stampo i ticket aperti — tutti e tre in questo momento
officina.stampa_ticket_aperti()

# chiudo il ticket 1 (lavatrice) — lo stato passa da "aperto" a "chiuso"
officina.chiudi_ticket(1)

# stampo di nuovo — ora appare solo t2 e t3
officina.stampa_ticket_aperti()

# somma dei preventivi base di tutti i ticket
# internamente scorre la lista e chiama calcola_preventivo() su ciascuno — polimorfismo
print(f"Totale preventivi: €{officina.totale_preventivi()}")

# stampa il report finale con il conteggio per tipo
# usa isinstance() per identificare il tipo reale di ogni elettrodomestico
officina.statistiche_per_tipo()
officina.statistiche_per_tipo()
