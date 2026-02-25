"""
Uzdevums 2: Vienību konvertors
Mērķis: nostiprināt konstanšu lietošanu, aritmētiskos operatorus un f-string formatēšanu.
Izveido converter.py, kas konvertē:
• Kilometrus ↔ jūdzes (1 km = 0.621371 mi)
• Kilogramus ↔ mārciņas (1 kg = 2.20462 lb)
• Litrus ↔ galonus (1 L = 0.264172 gal)
• Dolāri ↔ Eiro (1 $ = 0.84235020 €)
Prasības:
• Konversijas koeficientus glabā kā konstantes (nosaukumi ar LIELAJIEM_BURTIEM,
piem., KM_TO_MI = 0.621371)
• Lietotājs ar input() izvēlas konversijas tipu un virzienu, ievada vērtību
• Rezultātu formatē ar f-string un 2 decimālzīmju precizitāti (:.2f)
• Apstrādā nepareizu ievadi (kas nav skaitlis) ar informatīvu paziņojumu
"""

KM_TO_MI = 0.621371
KG_TO_LB = 2.20462
L_TO_GAL = 0.264172
USD_TO_EUR = 0.84235020

def main():
    print("--- Vienību konvertors ---")
    print("1: KM <-> MI | 2: KG <-> LB | 3: L <-> GAL | 4: USD <-> EUR")
    
    category = input("Izvēlies variantu (1-4): ")

    try:
        if category == '1':
            direction = input("1: KM -> MI | 2: MI -> KM: ")
            
            if direction == '1':
                value = float(input("Ievadi vērtību konvertēšanai: "))
                print(f"{value:.2f} km = {value * KM_TO_MI:.2f} mi")
            elif direction == '2':
                value = float(input("Ievadi vērtību konvertēšanai: "))  
                print(f"{value:.2f} mi = {value / KM_TO_MI:.2f} km")
            else:
                print("Kļūda: izvēlies 1 vai 2!")
                
        elif category == '2':
            direction = input("1: KG -> LB | 2: LB -> KG: ")
            if direction == '1':
                value = float(input("Ievadi vērtību konvertēšanai: "))
                print(f"{value:.2f} kg = {value * KG_TO_LB:.2f} lb")
            elif direction == '2':
                value = float(input("Ievadi vērtību konvertēšanai: ")) 
                print(f"{value:.2f} lb = {value / KG_TO_LB:.2f} kg")
            else: 
                print("Kļūda: izvēlies 1 vai 2!")  
                
        elif category == '3':
            direction = input("1: L -> GAL | 2: GAL -> L: ")
            if direction == '1':
                value = float(input("Ievadi vērtību konvertēšanai: "))
                print(f"{value:.2f} L = {value * L_TO_GAL:.2f} gal")
            elif direction == '2':
                value = float(input("Ievadi vērtību konvertēšanai: "))
                print(f"{value:.2f} gal = {value / L_TO_GAL:.2f} L")
            else:
                print("Kļūda: izvēlies 1 vai 2!")
                
        elif category == '4':
            direction = input("1: $ -> € | 2: € -> $: ")
            if direction == '1':
                value = float(input("Ievadi vērtību konvertēšanai: "))
                print(f"{value:.2f} $ = {value * USD_TO_EUR:.2f} €")
            elif direction == '2':
                value = float(input("Ievadi vērtību konvertēšanai: "))
                print(f"{value:.2f} € = {value / USD_TO_EUR:.2f} $")
            else: 
                print("Kļūda: izvēlies 1 vai 2!")
        else:
            print("Kļūda: Nepareiza izvēle!")
            
    except ValueError:
        print("Kļūda: Lūdzu ievadi skaitli (vērtībai)!")

if __name__ == "__main__":
    main()