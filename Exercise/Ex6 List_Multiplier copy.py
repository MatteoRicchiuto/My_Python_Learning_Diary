'''
Scrivi una funzione "sommatrice" che somma tra loro tutti gli elementi di una lista di numeri.
'''

def List_Mult(list):
    n = 1
    
    for i in list:
        n *= i
    
    print(n)

List_Mult([1,2,3,4,5])