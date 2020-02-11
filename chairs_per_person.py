f = open("reservations")

for reservation in f:
    name, number = reservation.split(",")
    try:
        chairs_per_person = 50 / int(number)
    except ValueError:
        number = input("What is this number: {} --- in digits: ".format(number))
        chairs_per_person = 50 / int(number)
    except ZeroDivisionError or number == " ":
        print("This \n\n\n")
    print("{} will get {} chairs per person".format(name, chairs_per_person))
