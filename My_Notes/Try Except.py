try:

    a, b = int(input("Inserisci Il 1° Numero: ")), int(input("Inserisci Il 2° Numero: "))

    print('minore' if a < b else 'uguale' if a == b else 'maggiore')

except ValueError :
    
    print('Non hai inserito un valore intero ')

except NameError : 
    
    print('Torna alle elementari che non sai scrivere')

except:
    
    print("Errore generico")