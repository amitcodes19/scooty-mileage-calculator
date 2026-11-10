while True:
    name = input("Enter your name: ")
    price = float(input("Petrol price per litre: "))
    amount = float(input("Petrol amount: "))
    distance = float(input("Distance travelled: "))

    if price > 0 and amount > 0 and distance > 0:
        litres = amount / price
        mileage = distance / litres
        cost = amount / distance

        print("\n--- SCOOTY REPORT ---")
        print("Hello", name)
        print("Petrol used:", litres, "litres")
        print("Mileage:", mileage, "km/l")
        print("Cost per km: Rs.", cost)

    else:
        print("Invalid input!")

    again = input("Again? yes/no: ")

    if again == "no":
        print("Bye", name)
        break
