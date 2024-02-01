
import sys
def verifica_ordine_decrescente():
    # Verifica se la sequenza è ordinata in modo decrescente
    is_decrescente = True
    if len(sys.argv) < 3:
        print("Error! You must insert at least 2 numbers")
        sys.exit(1)
    sequenza = sys.argv[1:]
    i = 0
    while i < len(sequenza) - 1 and is_decrescente:
        if sequenza[i] < sequenza[i + 1]:
            is_decrescente = False
        i += 1
    i = 0
    new_sequenza = []
    while i < len(sequenza)-1:
        new_sequenza += [int(sequenza[i])]
        i+=1

    if is_decrescente:
        print("The inserted sequence is sorted!")
    else:
        # Se la sequenza non è ordinata in modo decrescente, stampa la lista ordinata correttamente
        sequenza_ordinata = sorted(new_sequenza, reverse=True)
        print("The inserted sequence is not sorted!")
        print("The correct order is ", sequenza_ordinata)

verifica_ordine_decrescente()


