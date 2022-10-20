
user_gender = input("Are you a famale?: ")
user_age = input("How old are you?: ")
baby = input("How many children do you have?: ")

if user_gender == "yes" :
    is_female = True
else:
    is_female = False

if int(user_age) >= 35 and int(user_age) <= 55:
    right_age = True
else:
    right_age = False

if int(baby) >= 1:
    is_mom = True
else:
    is_mom = False

if is_female and right_age and is_mom:
    print("you are a milf.")
else:
    print("you are not a milf.")

    if is_female == False:
        print("you have to be a female to be a milf.")

    if int(user_age) < 35:
        print("you are not old enough to be a milf.")
        print("In " + str(35 - int(user_age)) + " years you will be a milf")
    if int(user_age) > 55:
        print("you are too old to be a milf.")
    if is_mom == False and is_female == True:
        print("You need to be a mom to be a milf")
