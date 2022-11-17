'''
Scrivi un programma che, passata come parametro una lista di interi, fornisce in output il maggiore tra i numeri contenuti nella lista.
'''
# In[] My Version
def Man_List(list):
    n_max = 0
    for i in list:
        if i > n_max:
            n_max = i
    return(n_max)

list = [1,2,100,4,5]

# In[] Solution
def max_in_list(list):
    my_max = 0
    for num in list:
        if num > my_max:
            my_max = num
    print(f"Il numero più grande della lista passata è {my_max}")