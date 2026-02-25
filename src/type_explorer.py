"""
iepazīt Python datu tipus, to uzvedību un savstarpējo konversiju/pārveidošanu.
Izveido type_explorer.py, kas demonstrē:
• Piešķirt vismaz 2 pamata tipu vērtības mainīgajiem (str, int, float, bool, None)
• Konsoles izvade ar katras vērtības tipu, izmantojot type()
• Vismaz 3 Python truthy/falsy uzvedības piemērus ar komentāriem
• Vismaz 3 tiešās datu tipu pārveides (explicit conversion) ar robežgadījumiem (kas
notiek, ja konversija neizdodas)


# Virkņu savienošana — Python neveic automātisku tipu konversiju
print("5" + "3") # "53" (virkņu savienošana)
# print("5" + 3) # TypeError! Atšķirībā no JS, Python to neatļauj
print(int("5") + 3) # 8 (tieša/uzdota (explicit) konversija)
# Robežgadījumi
# print(int("abc")) # ValueError — ko ar to darīt?
print(float("3.14")) # 3.14
# Truthy / falsy
print(bool("")) # False (tukša virkne)
print(bool(" ")) # True (atstarpe ir simbols!)
print(bool("0")) # True (!) — jebkura netukša virkne ir True
print(bool(0)) # False
print(bool([])) # False (tukšs saraksts)
print(bool(None)) # False
print(True + True) # 2 (bool ir int apakšklase Python)
# Jauktā aritmētika
print(True * 10) print(False + 5) print(10 / True) # 10.0
# 10 (True ir 1)
# 5 (False ir 0)
#Skaitļu pārveidošana
print(int(3.86)) # 3 ('norauj' beigas, nenotiek apaļošana)
print(int("3.14")) # ValueError! Kāpēc?
print(int(float("3.14"))) # 3
print(float("1e3")) # 1000.0
#Citi interesanti gadījumi, izskaidrot kāpēc tā notiek.
print(0.1 + 0.2 == 0.3) # False, kāpēc?
print(round(2.5)) # 2
print(round(3.5)) # 4
Uzdevums 2: Vienību konvertors
Mērķis: nostiprināt konstanšu lietošanu, aritmē
"""
#print("5" + "3") # "53" (virkņu savienošana)
#print("5" + 3)
#print(int("5") + 3)
try:
    print(int("abc"))
except ValueError:
    print("Kļūda: lūdzu ievadiet veselu skai") # Veids kā kļūdu izmantot savā labā