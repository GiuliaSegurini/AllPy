Esercizio 1
Un modo per riconoscere in quale lingua può essere scritto un testo in lingua ignota, è calcolare le frequenze delle varie lettere: lingue diverse hanno infatti profili diversi.

Per esempio, in Italiano le 6 lettere più frequenti sono, in ordine, "eaionl" (la lettera più usata in Italiano è quindi la "e"); in Francese sono "esaitn", in Turco "aeinrl" e in Finlandese "aintes", e così via.

Ovviamente, non è detto che un testo particolare rispetti esattamente la sequenza: ma su testi abbastanza lunghi, il risultato sarà almeno molto simile a quello atteso.

Si definisca un programma Python così strutturato:
Una classe Frequenza che deve gestire un file di testo. In pratica la classe avrà (almeno) una proprietà chiamata fileToProcess il cui scopo è quello di memorizzare il file di testo che la classe gestisce (potete usare chiaramente tutte le proprietà aggiuntive che vi possano sembrare utili per progettare la classe in questione)
si assuma che il file di testo da processare possa essere presumibilmente lungo
si consideri come standard per il nome del file il suffisso .txt
esempio pippo.txt oppure divinaC.txt
Un metodo guess6 che analizza fileToProcess come segue:
Legge il file gestito dalla classe (usate una strategia adeguata alla lunghezza del testo)
Restituisce la stringa composta dai 6 caratteri più frequenti in fileToProcess, in ordine di frequenza decrescente, considerando le seguenti regole:
non differenziando le minuscole dalle maiuscole
si comprendano le lettere accentate
si escludano punteggiatura e altri simboli
si considerino i numeri
In caso di parità di frequenza, i caratteri vanno ordinati secondo l'ordine lessicografico

Si usi come file di riferimento il file divinaCommedia.txt che contiene la Divina Commedia in formato testo. Chiaramente il programma deve funzionare con qualsiasi file di testo dato in input alla funzione.

Si fornisca il programma in un file .py e non un notebook
Si nomini il file cognomeNome.py, con cognome e Nome il vostro Nome e il vostro Cognome, rispettivamente
Si fornisca il risultato ottenuto eseguendo il programma sul file di esempio divinaC.txt
Si fornisca il risultato ottenuto su un altro file di testo a vostra scelta
Si commenti adeguatamente il codice
Si fornisca una breve relazione (max 1 pagina) che spieghi le soluzioni adottate 
Esercizio 2
Il file ted_main.csv contiene informazioni relative a varie presentazioni fatte per la piattaforma TED da diversi invitati. Ogni riga rappresenta una presentazione con tutte le informazioni relative. L’obiettivo di questo esercizio è esplorare i dati contenuti nel file e risolvere i seguenti compiti:

Aprire il file e mostrare le informazioni di base per ognuna delle variabili: numero di valori nulli e tipo della variabile Per ogni riga, le viariabili sono separate da virgola.
Ogni presentazione è identificata da un titolo. Associare ad ogni titolo un valore numerico crescente. Salvare la corrispondenza in un dizionario e aggiungere una variabile ai dati con tale identificativo numerico al dataframe originale.
Una sola variabile presenta valori mancanti. Ne si stampino i possibili valori. Si produca una dataframe che contenga le sole righe con valori mancanti di questa variabile e si rimuovano tali righe dal dataframe originale.
Produrre statistiche descrittive per le variabili numeriche presenti: media, mediana, moda, deviazione standard. Produrre inoltre la matrice di correlazione per le sole variabili numeriche. Quali variabili sono maggiormente correlate tra di loro? Plottare la matrice di correlazione e renderla il più leggibile possibile.
Aggiungere una variabile ai dati che contenga il rapporto tra commenti di un presentazione e la durata della presentazione. Plottare la distribuzione di commenti, durata, e il loro rapporto, in tre plot separati. Personalizzate i grafici come ritenete opportuno al fine di migliorarne la leggibilità.
Quale tipo di occupazione è più rappresentata tra gli speaker? Indicare cioè, il mestiere più frequente.
Per ogni anno, mostrare il numero totale di presentazioni ed il numero totale visualizzazioni. Quale anno ha avuto il maggior numero di visualizzazione per presentazione? Plottare questo rapporto al variare dell’anno.
La variabile ‘ratings’ è particolare: il suo contenuto è un dizionario, che mostra, per ogni presentazione, i sentimenti espressi dagli spettatori. Perciò, ogni chiave del dizionario rappresenta il tipo di reazione (‘Funny’, ‘Courageous’ etc.) e il valore corrispondente rappresenta quante persone hanno espresso quell’emozione. Aprirte tale variabile, con una opportuna funzione o comando, mostrando per ogni presentazione tutti i sentimenti e i rispettivi valori presenti nei rating. Attenzione: non tutte le presentazione avranno tutti i tipi possibili di sentimento nei propri ‘rating’. Se un sentimento non è presente per una certa presentazione, aggiungerlo al dizionario con valore 0. 
Creare un nuovo dataframe separato. In tale dataframe inserire l’identificativo numerico di ogni presentazione. In querto nuovo dataframe inserire, come variabili i sentimenti espressi nei rating corrispondenti. Tali variabili avranno come valori il numero espresso nella variabile ‘rating’ originale. Usate l’identificativo per associare correttamente. Una volta terminato, mostrare tutte le informazioni statistiche di base per questo nuovo dataframe.
Infine unire il nuovo dataframe di rating all’originale con una operazione di join o merge.

Risolvere gli esercizi da 1) a 10) in linguaggio python strutturando il codice in diversi file .py oppure in un unico python notebook. Il codice deve corrispondere in maniera chiara e concisa ad ognuna delle domande, mostrando i vari procedimenti e risultati per ognuna di esse. 


