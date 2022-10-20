friends = ["Simone", "Carolina", "Alessandro"]
school_friends = ["Matteo", "John", "Alessio", "Matteo"]
print(friends[0 :1 ])
friends[0] = "Benny"
print(friends + school_friends)
school_friends.append("Erika")  #aggiunge alla fine della lista
school_friends.insert(0, "Simone") # aggiunge al index specificato
friends.extend(school_friends) # aggiungi una lista ad un altra lista
print(friends)
friends.remove("Alessio")
print(friends)
print("Ci sono " + str(friends.count("Matteo")) + " Matteo nella tua lista di amici")
