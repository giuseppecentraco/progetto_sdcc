# Sistema Distribuito per Tweet Geolocalizzati

## Descrizione del Progetto

Questo progetto mira a realizzare un sistema distribuito per la visualizzazione di tweet geolocalizzati su una dashboard interattiva basata su **Amazon OpenSearch Dashboard**. Il sistema consente agli utenti di analizzare e visualizzare grandi volumi di dati derivanti da Twitter in maniera scalabile ed efficiente.

## Funzionalità Principali

- **Visualizzazione su Mappa:** Mostra i tweet geolocalizzati su una mappa interattiva.
- **Filtri Personalizzati:** Filtra i tweet in base a parametri come hashtag, utente, data, ecc.
- **Visualizzazione Tabellare:** Presenta i tweet in formato tabellare per un'analisi dettagliata.
- **Dashboard Interattiva:** Include widget personalizzabili, grafici e tabelle.
- **Esportazione Dati:** Supporta l'esportazione dei dati in formato CSV e report in formato PDF/PNG.
- **Ricerca Avanzata:** Consente l'uso di query predefinite e personalizzate.

## Architettura del Sistema

Il progetto sfrutta i seguenti servizi di **Amazon Web Services (AWS):**

- **Amazon OpenSearch Service:** Per l'indicizzazione e la ricerca dei dati.
- **Amazon OpenSearch Dashboard:** Per la visualizzazione e l'analisi interattiva dei dati.

**Altri strumenti:**
- Script Python per il preprocessing dei dati (inclusa la generazione di coordinate random per i tweet senza geolocalizzazione).

## Tecnologie Utilizzate

- **Python:** Pre-processing dei dati.
- **AWS:** Per il deployment del sistema distribuito.
- **OpenSearch Dashboard:** Per l'interfaccia utente.
- **JSON:** Formato di input per i tweet.

## Requisiti

### Funzionali
- Visualizzazione interattiva su mappa.
- Filtri avanzati e ricerca personalizzata.
- Esportazione e reportistica.

### Non Funzionali
- **Scalabilità:** Gestione di grandi volumi di dati.
- **Affidabilità:** Operazioni coerenti senza guasti.
- **Sicurezza:** Autenticazione e controllo degli accessi.

## Implementazione

### Pre-processing
- Script Python per generare coordinate mancanti nei tweet.
- Parsing e trasformazione dei dati in formato JSON.

### Indicizzazione
- Creazione di un indice personalizzato in OpenSearch per gestire attributi geospaziali e temporali.

### Dashboard
- Dashboard interattiva con:
  - Mappe geolocalizzate.
  - Grafici e tabelle per analisi dettagliate.
  - Widget di filtro e conteggio.

### Test
- Test approfonditi per verificare l'affidabilità e la scalabilità del sistema.

## Considerazioni Finali

Il progetto ha raggiunto gli obiettivi prefissati, dimostrando l'efficacia delle tecnologie AWS nel gestire un sistema distribuito per l'analisi di Big Data.
