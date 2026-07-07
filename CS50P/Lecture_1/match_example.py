name = input("What is your name: ")

match name:
    case "Farah" | "Andrea" | "Teja":
        print("St. Lukes")
    case "Sana":
        print("St. Johns")
    case "Sammy":
        print("St. Marks")
    case "Dave":
        print("St. Mathews")
    case _:
        print("Who?")