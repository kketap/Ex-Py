pizza = input("Elije el tipo de pizza: Vegetariana o No Vegetariana: ")

ingredientePimiento = "Pimiento"
ingredienteTofu = "Tofu"
ingredientePiTo = "Pimiento y Tofu"

ingredientePeperoni = "Peperoni"
ingredienteJamon = "Jamon"
ingredienteSalmon = "Salmon"
ingredienteTodo = "Peperoni Jamon y Salmon"

if pizza == "Vegetariana":
    ingredientes = input("Elije tus ingredientes: Pimiento o Tofu: ")
    if ingredientes == ingredientePimiento:
        print("Pedido de Pizza: ",pizza, "con ",ingredientes)
    if ingredientes == ingredienteTofu:
        print("Pedido de Pizza: ",pizza, "con ",ingredientes)
    if ingredientes == ingredientePiTo:
        print("Pedido de Pizza: ",pizza, "con ",ingredientes)
elif pizza == "No Vegetariana":
    ingredientes = input("Elije tus ingredientes: Peperoni, Jamón o Salmón: ")
    if ingredientes == ingredientePeperoni:
        print("Pedido de Pizza: ",pizza, "con ",ingredientes)
    elif ingredientes == ingredienteJamon:
        print("Pedido de Pizza: ",pizza, "con ",ingredientes)
    elif ingredientes == ingredienteSalmon:
        print("Pedido de Pizza: ",pizza, "con ",ingredientes)
    elif ingredientes == ingredienteTodo:
        print("Pedido de Pizza: ",pizza, "con ",ingredientes)
    else :
        print("Error")
else :
    print("Error")
  