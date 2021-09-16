minLista = [2, 4, 10, 23]
def Average(x):
    return sum(x) / len(x)

while True:
    val = int(input("Vad vill du göra?\n1. Titta på hela listan             2. Titta på en specifik listposition\n3. Lägga till ett värde i listan    4. Ta bort ett värde i listan\n5. Sortera listan                   6. Beräkna listans medelvärde\n7. Avsluta\n\nAnge ditt val -> "))
    if val == 1:
        for x in minLista:
            print(x)
    if val == 2:
        length = len(minLista)
        valtemp = int(input(f"Det finns {length} värden i listan.\nVilken vill du kolla på? -> "))
        print(minLista[valtemp - 1])
    if val == 3:
        valtemp = int(input("Vad vill du lägga till i listan? -> "))
        minLista.append(valtemp)
    if val == 4:
        valtemp = int(input(f"{minLista}\nVad vill du ta bort från listan? -> "))
    if val == 5:
        minLista.sort()
        print(f"{minLista}\nListan har blivit sorterad.\n")
    if val == 6:
        print(f"Medelvärdet är: {Average(minLista)}")
    if val == 7:
        break