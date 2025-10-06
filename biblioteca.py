def carica_da_file(file_path):
    """Carica i libri dal file"""
    biblioteca ={}
    try:
        with open(file_path,'r', encoding='utf-8') as file:
            maxsezione = int(file.readline().rstrip())

            for line in file:

                line=line.rstrip().split(',')
                titolo=line[0]
                autore=line[1]
                anno=int(line[2])
                pagine=int(line[3])
                sezione=int(line[4])
                biblioteca[titolo]={'autore': autore, 'anno': anno,'pagine': pagine, 'sezione': sezione}
        return biblioteca, maxsezione
    except FileNotFoundError:
        return None




def aggiungi_libro(biblioteca, titolo, autore, anno, pagine, sezione, file_path,maxsezione):
    """Aggiunge un libro nella biblioteca"""
    if titolo in biblioteca or sezione > maxsezione:
        return None
    else:
        biblioteca[titolo]={'autore': autore,'anno': anno,'pagine': pagine, 'sezione': sezione}
        with open(file_path,'a') as file:
            file.write(f'{titolo},{autore},{anno},{pagine},{sezione}\n')
    return biblioteca





def cerca_libro(biblioteca, titolo):
    """Cerca un libro nella biblioteca dato il titolo"""
    risultato=''
    for key,dati in biblioteca.items():
        if key==titolo:
            autore=dati['autore']
            pagine=dati['pagine']
            sezione=dati['sezione']
            anno=dati['anno']
            risultato=titolo+','+str(autore)+','+str(anno)+','+str(pagine)+','+str(sezione)
            return risultato


    return None




def elenco_libri_sezione_per_titolo(biblioteca, sezione):
    """Ordina i titoli di una data sezione della biblioteca in ordine alfabetico"""
    libri_sezione=[]

    for key,dati in biblioteca.items():
        numero=dati['sezione']
        if numero==sezione:
            libri_sezione.append(key)
    if not libri_sezione:
        return None
    libri_sezione.sort()


    return libri_sezione




def main():
    biblioteca = {}
    file_path = "biblioteca.csv"

    while True:
        print("\n--- MENU BIBLIOTECA ---")
        print("1. Carica biblioteca da file")
        print("2. Aggiungi un nuovo libro")
        print("3. Cerca un libro per titolo")
        print("4. Ordina titoli di una sezione")
        print("5. Esci")

        scelta = input("Scegli un'opzione >> ").strip()

        if scelta == "1":
            while True:
                file_path = input("Inserisci il path del file da caricare: ").strip()
                biblioteca,maxsezione = carica_da_file(file_path)
                if biblioteca is not None:
                    break

        elif scelta == "2":
            if not biblioteca:
                print("Prima carica la biblioteca da file.")
                continue

            titolo = input("Titolo del libro: ").strip()
            autore = input("Autore: ").strip()
            try:
                anno = int(input("Anno di pubblicazione: ").strip())
                pagine = int(input("Numero di pagine: ").strip())
                sezione = int(input("Sezione: ").strip())
            except ValueError:
                print("Errore: inserire valori numerici validi per anno, pagine e sezione.")
                continue

            biblioteca = aggiungi_libro(biblioteca, titolo, autore, anno, pagine, sezione, file_path,maxsezione)
            if biblioteca:
                print(f"Libro aggiunto con successo!")
            else:
                print("Non è stato possibile aggiungere il libro.")

        elif scelta == "3":
            if not biblioteca:
                print("La biblioteca è vuota.")
                continue

            titolo = input("Inserisci il titolo del libro da cercare: ").strip()
            risultato = cerca_libro(biblioteca, titolo)
            if risultato:
                print(f"Libro trovato: {risultato}")
            else:
                print("Libro non trovato.")

        elif scelta == "4":
            if not biblioteca:
                print("La biblioteca è vuota.")
                continue

            try:
                sezione = int(input("Inserisci numero della sezione da ordinare: ").strip())
            except ValueError:
                print("Errore: inserire un valore numerico valido.")
                continue

            titoli = elenco_libri_sezione_per_titolo(biblioteca, sezione)
            if titoli is not None:
                print(f'\nSezione {sezione} ordinata:')
                print("\n".join([f"- {titolo}" for titolo in titoli]))

        elif scelta == "5":
            print("Uscita dal programma...")
            break
        else:
            print("Opzione non valida. Riprova.")


if __name__ == "__main__":
    main()

