'''
Scrivi una funzione a cui viene passato un carattere come parametro, e che ci dice se il carattere è o meno una vocale.
'''

def is_vocal(v):
    if v in "AEIOUYaeiouy":
        print(f"{v} è una vocale.")
    else: 
        print(f"{v} non è una vocale.")

is_vocal(input("Inserisci una lettera: "))