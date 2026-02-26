import sys

def check_eligibility():

    try:
        age = int(input("Ievadi vecumu: "))
        if age < 0:
            print("Kļūda: Vecums nevar būt negatīvs.")
            sys.exit()
    except ValueError:
        print("Kļūda: Ievadi veselu skaitli!")
        sys.exit()

    has_license = False
    is_student = False
    is_veteran = False


    if 16 <= age <= 26:
        is_student = input("Vai esat students? (j/n): ").lower() == 'j'
    if age >= 18:
        has_license = input("Vai Jums ir autovadītāja apliecība? (j/n): ").lower() == 'j'
    if age < 65:
        is_veteran = input("Vai esat veterāns? (j/n): ").lower() == 'j'


    can_vote = age >= 18
    can_rent = age >= 21 and has_license
    senior_discount = age >= 65 or is_veteran
    student_discount = 16 <= age <= 26 and is_student


    print("\n--- Atbilstības pārbaude ---")
    print(f"Balsošana: {'Jā ✓' if can_vote else 'Nē ✗ (nepietiekams vecums)'}")


    if can_rent:
        print("Auto īre: Jā ✓")
    elif age < 21:
        print("Auto īre: Nē ✗ (nepietiekams vecums)")
    else:
        print("Auto īre: Nē ✗ (nav apliecības)")

    print(f"Senioru / veterānu atlaide: {'Jā ✓' if senior_discount else 'Nē ✗'}")
    print(f"Studentu atlaide: {'Jā ✓' if student_discount else 'Nē ✗'}")
    pass

if __name__ == "__main__":
    check_eligibility()