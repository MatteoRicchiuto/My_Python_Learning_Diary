try:

    a, b = int(input("Inserisci Il 1° Numero: ")), int(input("Inserisci Il 2° Numero: "))

    print('minore' if a < b else 'uguale' if a == b else 'maggiore')

except ValueError :     
    print('Non hai inserito un valore intero ')         # Viene stampato soltante se c'è un erorre di valore

except NameError : 
    print('Torna alle elementari che non sai scrivere') # Viene stampato soltante se c'è un erorre di nome

except:
    print("Errore generico")                # Viene stampato per qualsiasi errore non specificat in precedenza

finally:
    print('Hope you got the result you want!')  # Viene stampato sempre alla fine del programma