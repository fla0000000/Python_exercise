def ft_abs():
    espressione = input("Insert an expression: ")
    try:
    # Valuta l'espressione
        risultato = int(eval(espressione))
        print("The result is: ", risultato)

    except:
        print("Si è verificato un errore")
    if(risultato < 0):
        risultato *=-1



ft_abs()