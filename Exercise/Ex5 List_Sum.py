'''
Scrivi una funzione "sommatrice" che somma tra loro tutti gli elementi di una lista di numeri.
'''

def List_Sum(list):
    n = 0
    
    for i in list:
        n += i
    
    print(n)

List_Sum([1,2,3,4,5])