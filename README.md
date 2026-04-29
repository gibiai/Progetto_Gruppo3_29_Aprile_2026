
---
# 🔧 Gestione Intelligente di un'Officina di Elettrodomestici
### 👥 Team Project Collaboration
Progetto sviluppato in gruppo per applicare i principi della Programmazione Orientata agli Oggetti attraverso collaborazione e suddivisione logica dei compiti.

**Team Members:**
* Davide Bruseghin
* Gabriele De Carlo
* Vincenzo Cantarello

---

## 🎯 Obiettivi del Progetto

- Modellare elettrodomestici generici e specifici (Lavatrice, Frigorifero, Forno)
- Applicare i principi fondamentali della Programmazione Orientata agli Oggetti
- Gestire ticket di riparazione con stato operativo e preventivi
- Simulare il flusso reale di una riparazione: apertura, diagnosi, preventivo, chiusura
- Utilizzare `type()` e `isinstance()` per classificare automaticamente gli oggetti
- Generare statistiche operative sull'attività dell'officina

---

## 🛠️ Tech Stack

- Python 3
- OOP (Encapsulation, Inheritance, Polymorphism, Abstraction)
- Lists & Object Management
- `type()` / `isinstance()`

---

## 📂 Project Structure

- `elettrodomestico.py` — Classe astratta base (Davide)
- `classi_derivate.py` — Classi derivate Lavatrice, Frigorifero, Forno (Gabriele)
- `ticket_riparazione.py` — Classe TicketRiparazione (Vincenzo)
- `officina.py` — Classe Officina (Vincenzo)
- `main.py` — Entry point (Gabriele - Davide - Vincenzo)

## ⚙️ Setup

- Nessuna dipendenza esterna necessaria
- Eseguire con `python3 main.py`

---

## 🧱 Core Classes

- `Elettrodomestico` — classe astratta con `@property`, setter con controlli e `@abstractmethod`
- `Lavatrice` — sottoclasse con capacità kg e giri centrifuga
- `Frigorifero` — sottoclasse con litri e freezer
- `Forno` — sottoclasse con tipo alimentazione e ventilato
- `TicketRiparazione` — gestione ticket con stato, note e preventivo variadic (`*voci_extra`)
- `Officina` — gestione lista ticket, statistiche e totale preventivi

---

## 📊 Functional Workflow

1. Creazione elettrodomestico e apertura ticket
2. Aggiunta note tecniche tramite `aggiungi_nota()`
3. Calcolo preventivo tramite `calcola_preventivo(*voci_extra)` — polimorfismo su `stima_costo_base()`
4. Chiusura ticket tramite `chiudi_ticket(id)`
5. Report statistico tramite `statistiche_per_tipo()` con `isinstance()`

---

## 📈 Key Learning Outcomes

1. **Incapsulamento** — attributi privati `__` accessibili solo tramite getter/setter
2. **Ereditarietà** — le sottoclassi ereditano da `Elettrodomestico` tramite `super()`
3. **Polimorfismo** — `stima_costo_base()` overridato in ogni sottoclasse produce costi diversi
4. **Astrazione** — `Elettrodomestico` è classe astratta (`ABC`) con `@abstractmethod`
5. **Type Checking** — `isinstance()` in `Officina` per statistiche per categoria

---

## 📄 License

This project is intended for educational purposes and practical OOP training.
