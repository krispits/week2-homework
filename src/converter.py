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