🔧 OffiTech Repair Manager

Gestione intelligente di un’Officina di Elettrodomestici

⸻
👥 Team Project Collaboration

Questo progetto è stato sviluppato come lavoro di gruppo, con l’obiettivo di applicare in modo pratico i principi della Programmazione Orientata agli Oggetti attraverso collaborazione, suddivisione logica dei compiti e sviluppo condiviso.

Team Members:

* Davide Bruseghin
* Gabriele De Carlo
* Vincenzo Cantarello

Collaborative Focus:

* Progettazione struttura classi
* Implementazione OOP (incapsulamento, ereditarietà, polimorfismo)
* Gestione ticket e logica officina
* Testing e validazione del flusso operativo
* Documentazione e organizzazione del progetto
  _____
🎯 Obiettivi del Progetto

Progettare un sistema OOP completo per la gestione di un’officina specializzata nella riparazione di elettrodomestici.

* Modellare elettrodomestici generici e specifici (Lavatrice, Frigorifero, Forno)
* Applicare i principi fondamentali della Programmazione Orientata agli Oggetti
* Gestire ticket di riparazione con stato operativo e preventivi
* Simulare il flusso reale di una riparazione: apertura, diagnosi, preventivo, chiusura
* Utilizzare type() / isinstance() per classificare automaticamente gli oggetti
* Generare statistiche operative sull’attività dell’officina

⸻

📝 Methodology

Development Pipeline:

Class Design

Creazione della classe base Elettrodomestico con attributi privati e metodi condivisi

Inheritance Structure

Sviluppo delle sottoclassi:

* Lavatrice
* Frigorifero
* Forno

Polymorphism

Override del metodo stima_costo_base() per adattare il preventivo in base al tipo di dispositivo

Ticket Management

Implementazione della classe TicketRiparazione per gestire:

* Stato ticket
* Diagnosi tecnica
* Preventivo finale

Workshop System

Creazione della classe Officina per:

* Inserimento ticket
* Chiusura ticket
* Report operativi
* Analisi statistica

⸻

🛠️ Tech Stack

• Python 3 • OOP (Encapsulation, Inheritance, Polymorphism) • Lists & Object Management • type() / isinstance()

⸻

## 📂 Project Structure

- `elettrodomestico.py` — Classe astratta base (Davide)
- `lavatrice.py` — Classe derivata Lavatrice (Gabriele)
- `frigorifero.py` — Classe derivata Frigorifero (Gabriele)
- `forno.py` — Classe derivata Forno (Gabriele)
- `ticket_riparazione.py` — Classe TicketRiparazione (Vincenzo)
- `officina.py` — Classe Officina (Vincenzo)
- `main.py` — Entry point

## ⚙️ Setup

- Nessuna dipendenza esterna necessaria
- Eseguire con `python3 main.py`

## 🧱 Core Classes

- `Elettrodomestico` — classe astratta con getter/setter e controlli
- `Lavatrice` — sottoclasse con capacità e giri centrifuga
- `Frigorifero` — sottoclasse con litri e freezer
- `Forno` — sottoclasse con tipo alimentazione e ventilato
- `TicketRiparazione` — gestione ticket con preventivo variadic
- `Officina` — gestione lista ticket e statistiche

⸻

📁 Core Components

Elettrodomestico

Classe base che rappresenta qualsiasi apparecchio da riparare.

Attributi principali:

* Marca
* Modello
* Anno acquisto
* Guasto

⸻

Lavatrice

Specializzazione con:

* Capacità kg
* Giri centrifuga

⸻

Frigorifero

Specializzazione con:

* Litri
* Freezer

⸻

Forno

Specializzazione con:

* Alimentazione
* Ventilazione

⸻

TicketRiparazione

Sistema di gestione pratica:

* ID ticket
* Stato (aperto, in lavorazione, chiuso)
* Note tecniche
* Preventivo

⸻

Officina

Cuore del sistema:

* Lista ticket
* Gestione processi
* Statistiche
* Totale preventivi

⸻

📊 Functional Workflow

1. Registrazione dispositivo

Inserimento dell’elettrodomestico nel sistema

2. Apertura ticket

Creazione ticket associato

3. Diagnosi

Aggiunta note tecniche

4. Preventivo

Calcolo costo tramite polimorfismo

5. Chiusura

Aggiornamento stato

6. Reporting

Statistiche per categoria

⸻

📈 Key Learning Outcomes

1. Incapsulamento

Gli attributi privati proteggono l’integrità dei dati.

2. Ereditarietà

Le sottoclassi riducono duplicazione e migliorano scalabilità.

3. Polimorfismo

Ogni elettrodomestico produce costi differenti tramite lo stesso metodo.

4. Gestione Oggetti Complessi

Liste di oggetti e relazioni tra classi simulano casi reali.

5. Type Checking

L’uso di type() o isinstance() permette report dettagliati per categoria.

⸻

🎯 Esempio di Output Statistico

Numero di lavatrici in riparazione: X

Numero di frigoriferi in riparazione: Y

Numero di forni in riparazione: Z

⸻

🎓 Finalità Didattica

Questo progetto consolida competenze fondamentali per sviluppatori junior/intermediate:

* Costruttori
* Classi
* Oggetti
* Access modifiers
* Ereditarietà
* Override
* Gestione stato
* Architettura modulare

⸻

📄 License

This project is intended for educational purposes and practical OOP training.
