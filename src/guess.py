"""
Uzdevums 5: Minēšanas spēle
Mērķis: praktizēt while ciklu, break, input() apstrādi un programmas stāvokļa uzturēšanu.
Izveido guess.py, kas:
• Ģenerē nejaušu skaitli no 1 līdz 100 (import random; random.randint(1, 100))
• Ļauj lietotājam minēt, izmantojot input()
• Pēc katra minējuma dod padomu "Par lielu" vai "Par mazu"
• Skaita mēģinājumus
• Beidzas, kad uzminēts vai pēc 10 mēģinājumiem
Piezīme: Python nav do...while cikla. Izmanto while True: ar break idiomu:
while True:
minejums = input("Tavs minējums: ")
# ... apstrāde ...
if nosacijums:
break
Prasības:
• Apstrādā nekorektu ievadi (kas nav skaitlis) — nepārtrauc spēli, bet parāda
paziņojumu
• Kad spēle beidzas, parāda mēģinājumu skaitu un pareizo atbildi
• Piedāvā spēlēt vēlreiz (papildus ārējais while True cikls)
"""