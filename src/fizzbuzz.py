"""
Mērķis: praktizēt for ciklu ar range(), nosacījumus un dalāmības pārbaudi ar % operatoru.
Izveido fizzbuzz.py, kas:
• Pieņem skaitli N kā komandrindas argumentu (sys.argv)
• Izvada skaitļus no 1 līdz N
• "Fizz" ja dalās ar 3
• "Buzz" ja dalās ar 5
• "FizzBuzz" ja dalās ar abiem
• Bonuss: parametrizē dalītājus un vārdus (piem., papildus "Jazz" ja dalās ar 7)
python fizzbuzz.py 15
# 1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz, 11, Fizz, 13, 14, FizzBuzz
Prasības:
• Apstrādā gadījumu, kad N nav norādīts vai nav skaitlis
• Secība ir svarīga: vispirms pārbaudi dalāmību ar abiem, tad ar katru atsevišķi
"""
