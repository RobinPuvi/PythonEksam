import sys
# Loeb failist a.txt
with open('a.txt', encoding='utf8') as f:
    sisuA = f.read()
# Loeb failist b.txt
with open('b.txt', encoding='utf8') as f:
    sisuB = f.read()
# Liitab mõlemad faili sisud kokku saades muutuja
vastus = int(sisuA) + int(sisuB)
# Defineerib funktsiooni (string_print)
def string_print(vastus):
    # Kasutan for loopi
    for i in range(vastus):
        print("Tere!")
# Kui arv on suurem kui 21 ja väiksem kui 1 miljon siis :
# teeb faili nimega tulemus.txt ja salvestab selle
if vastus >=21 <= 1000000 :
    with open('tulemus.txt', "w") as f:
        f.write(str(vastus))
        print(vastus)
    # Kui arv on väiksem kui 20 siis:
    # teeb faili nimega tulemus.txt ja prindib välja "Tere!" nii mitu korda kui on tulemus
elif vastus <= 20 :
    with open('tulemus.txt', "w") as f:
        f.write(str(vastus))
        string_print(vastus)
# Kui arv on suurem kui 1 miljon siis :
# teeb faili nimega miljon2r.txt ja salvestab selle
else:
    with open('miljon2r.txt', "w") as f:
        f.write(str(vastus))
        print(vastus)
