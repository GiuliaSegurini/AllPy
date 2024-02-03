# Definizione di una classe chiamata Frequency
class Frequency:
    # Metodo __init__ che viene chiamato quando un nuovo oggetto Frequency viene creato
    def __init__(self, Filetoprocess):
        try:
            # Apre il file specificato in modalità lettura con encoding utf-8 e lo assegna all'attributo Filetoprocess dell'istanza
            self.Filetoprocess = open(Filetoprocess, encoding='utf-8')
        except FileNotFoundError:
            print(f"Errore: Il file {Filetoprocess} non è stato trovato.")
        except Exception as e:
            print(f"Errore durante l'apertura del file: {e}")

    # Metodo Guess6 per calcolare le 6 lettere più frequenti nel file
    def Guess6(self):
        # Dizionario che conterrà il conteggio di ogni carattere
        character = {}

        try:
            # Leggo tutte le linee del file e le assegno alla variabile text
            text = self.Filetoprocess.readlines()

            # Loop per ogni linea nel testo
            for line in text:
                # Loop per linea (trasformate in minuscolo)
                for letter in line.lower():
                    # Controlla se la lettera è una lettera dell'alfabeto
                    if letter.isalpha():
                        # Incrementa il conteggio del carattere nel dizionario
                        character[letter] = character.get(letter, 0) + 1

            # Converto il dizionario in una lista di tuple (carattere, conteggio) e la ordina in ordine lessicografico decrescente
            list_character = list(character.items())
            list_character.sort(key=lambda x: (-x[1],x[0]))

            # Restituisco una stringa formattata con le 6 lettere più frequenti
            #return f"i caratteri più frequenti sono:{list_character[0:6]}" #, list_character #con list_character si può verificare che faccia elenco anche delle lettere accentate
            # Restituisco una stringa formattata con i primi 6 caratteri più frequenti
            return f"I primi 6 caratteri più frequenti sono: {''.join([char[0] for char in list_character[0:6]])}"

        except Exception as e:
            print(f"Errore durante la lettura del file: {e}")

        finally:
            # Chiude il file quando il blocco try-finally è completato
            self.Filetoprocess.close()
