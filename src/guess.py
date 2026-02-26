import random

def play_game():
    target = random.randint(1, 100)
    attempts = 0
    max_attempts = 10

    print(f"\nEsmu iedomājies skaitli no 1 līdz 100. Tev ir {max_attempts} mēģinājumi.")

    while True:
        try:
            user_input = input(f"Mēģinājums {attempts + 1}/{max_attempts}. Tavs minējums: ")
            guess = int(user_input)
        except ValueError:
            print("Kļūda: Lūdzu, ievadi veselu skaitli!")
            continue

        attempts += 1

        if guess == target:
            print(f"Apsveicu! Tu uzminēji {target} ar {attempts}. mēģinājumu.")
            break
        elif guess < target:
            print("Par mazu!")
        else:
            print("Par lielu!")

        if attempts >= max_attempts:
            print(f"Spēle beigusies! Tu neizmantoja {max_attempts} mēģinājumus. Pareizais skaitlis bija {target}.")
            break

def main():
    while True:
        play_game()
        
        # Cikls, kas "spīdzina" lietotāju, līdz dabū j vai n
        while True:
            again = input("\nVai vēlies spēlēt vēlreiz? (j/n): ").lower().strip()
            if again in ['j', 'n']:
                break
            print("Kļūda: Lūdzu, ievadi tikai 'j' (jā) vai 'n' (nē)!")

        if again == 'n':
            print("Paldies par spēli! Uz redzēšanos!")
            break

if __name__ == "__main__":
    main()