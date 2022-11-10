i = 0
secret_word = "ciao"
gues = ""

while i < 3:
     gues = input("Enter: ")
     if gues == secret_word:
        print("You win")
        break
     elif gues != secret_word and i < 3:
        print("you lose")
     i += 1