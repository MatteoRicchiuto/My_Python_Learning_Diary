'''
Scrivi una funzione che prende due numeri come parametro e manda in print il più grande tra i due.
Per quanto Python disponga di una funzione max(), sei invitato a utilizzare le istruzioni If, Elif ed Else per la scrittura dell'algoritmo.
'''
def MyMax2(x,y):
    
    if x > y:
        return(x)
    
    elif y > x:
        return(y)
    
    else:
        return("I numeri sono uguali")

print(MyMax2(1,2))