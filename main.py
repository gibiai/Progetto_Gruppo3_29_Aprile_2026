from elettrodomestico import Elettrodomestico
from classi_derivate import Lavatrice, Frigorifero, Forno
from ticket_riparazione import TicketRiparazione
from officina import Officina

l = Lavatrice("Samsung", "WW90T", 2020, "non centrifuga", 9, 1400)
f = Frigorifero("Bosch", "KGN36", 2018, "non raffredda", 320, True)
fo = Forno("Whirlpool", "AKZ96", 2021, "non scalda", "gas", True)

t1 = TicketRiparazione(1, l)
t2 = TicketRiparazione(2, f)
t3 = TicketRiparazione(3, fo)

t1.aggiungi_nota("Cuscinetto da sostituire")
t2.aggiungi_nota("Compressore rotto")

print(t1.calcola_preventivo(30, 15))
print(t2.calcola_preventivo(100))
print(t3.calcola_preventivo())

officina = Officina("Riparazioni Napoli")
officina.aggiungi_ticket(t1)
officina.aggiungi_ticket(t2)
officina.aggiungi_ticket(t3)

officina.stampa_ticket_aperti()

officina.chiudi_ticket(1)
officina.stampa_ticket_aperti()

print(f"Totale preventivi: €{officina.totale_preventivi()}")

officina.statistiche_per_tipo()