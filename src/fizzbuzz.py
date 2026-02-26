"""
Uzdevums: FizzBuzz.  Šeit pēc nosacījumiem bija svarīga secība, tāpēc izmantoju if elif. 
Par Jazz nebija minēts vai tam jānāk ir atsevišķi, kad tikai dalās ar 7 vai jābūt kopā.
Ja kopā, tad noteikti es pievienotu Fizzbuzz output 
    elif i % 3 == 0 and i % 5 == 0 and i % 7 == 0:
        output = "FizzBuzzJazz"
    elif i % 3 == 0 and i % 7 == 0:
        output = "FizzJazz"
    elif i % 5 == 0 and i % 7 == 0:
        output = "BuzzJazz"

Ja nebūtu svarīga secība, es noteikti izmantotu viekāršāk pārskatāmu kodu:
    def fizz_buzz(n):
    for i in range(1, n + 1):
        output = ""

        if i % 3 == 0:
            output += "Fizz"
        if i % 5 == 0:
            output += "Buzz"
        if i % 7 == 0:
            output += "Jazz"
        
        if not output:
            print(i)
        else:
            print(output)
"""
import sys

def fizz_buzz(n):
    for i in range(1, n + 1):
        output = ""
        
        if i % 3 == 0 and i % 5 == 0:
            output = "FizzBuzz"
        elif i % 7 == 0:
            output = "Jazz"
        elif i % 3 == 0:
            output = "Fizz"
        elif i % 5 == 0:
            output = "Buzz"

        if output:
            print(output)
        else:
            print(i)

def main():
    if len(sys.argv) < 2:
        print("Lietošana: python3 src/fizzbuzz.py <skaitlis>")
        sys.exit(1)

    try:
        limit = int(sys.argv[1])
        fizz_buzz(limit)
    except ValueError:
        print("Kļūda: N jābūt veselam skaitlim!\nLietošana: python3 src/fizzbuzz.py <N>")
        sys.exit(1)

if __name__ == "__main__":
    main()