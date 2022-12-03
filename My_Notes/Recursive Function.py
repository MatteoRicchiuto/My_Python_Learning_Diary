'''
The word recursion in Python describes the process of repeatedly calling a function within itself
'''

def factorial(num):
    if num == 1:
        return 1
    else:
        return num * factorial(num-1)
# -------------------------------------------------------------------------------------------------------------------
#!    A recursive function contains two parts:
#?       - Recursive Step:
#              The line of code under the else statement is the recursive step, 
#              because it calls the function factorial().  

#?       - Base Case:
#              In the above function, the recursion stops when num == 1.    
#              This case is called the base case, which should be defined in every recursive function.
#  
#              Having a base case helps to avoid infinite recursions. 

#              The base case can be defined with an if statement like the function above.
#              Without the base case in the factorial function above, 
#              the function would start calling factorial(0), factorial(-1) and so on.
# -----------------------------------------------------------------------------------------------------------------            

# In[] Esempio
def scala(n):
    if n != 0:
        print ("scalino")  
        scala(n-1)
    else: 
        print("scala finita")

scala(10)
# %%
