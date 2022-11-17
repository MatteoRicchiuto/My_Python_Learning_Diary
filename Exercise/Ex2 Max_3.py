'''
Scrivi una funzione che prende stavolta tre numeri come parametro e restituisce il più grande tra loro!
'''
# In[] My Version
def MyMax3(x,y,z):
    
    if x > y and x > z:
        return(x)
    
    elif y > x and y > z:
        return(y)
    
    elif z > x and z > y:
        return(z)
    
    elif x == y and x > z:
        return(x, y)
    
    elif x == z and x > y:
        return(x, z)
    
    elif y == z and y > x:
        return(y, z)
    
    elif x == y and x == z:
        return("I numeri sono uguali")

print(MyMax3(1,2,2))

# In[] Solution
def my_max_of_three(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    elif c >= a and c >= b:
        return c

print(my_max_of_three(1,2,2))
# %%
