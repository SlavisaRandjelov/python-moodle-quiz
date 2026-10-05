# Moodle Python Quiz & Score Tracker
# Author: Slavisa Randjelov

import time

def pokreni_kviz():
    pitanja = [
        {
            "pitanje": "1.Šta vraća len(['a', 'b', 'c'])?",
            "opcije": ["A) 2", "B) 3", "C) 4"],
            "tacan_odgovor": "B"
        },
        {
            "pitanje": "2. Šta radi metoda append() na listi?",
            "opcije": ["A) Briše element", "B) Dodaje na kraj", "C) Sortira listu"],
            "tacan_odgovor": "B"
        },
        {
            "pitanje": "3. Koji je rezultat 17 // 5 u Pythonu?",
            "opcije": ["A) 3", "B) 3.4", "C) 2"],
            "tacan_odgovor": "A"
        },
        {
            "pitanje": "4. Šta će uraditi komanda break u petlji?",
            "opcije": ["A) Preskočiti iteraciju", "B) Prekinuti petlju", "C) Prijaviti grešku"],
            "tacan_odgovor": "B"
        }
    ]

    skor = 0
    ukupno = len(pitanja)

    print("========================================")
    print("   WELCOME TO PYTHON MOODLE QUIZ TEST   ")
    print("========================================\n")

    for p in pitanja:
        print(p["pitanje"])
        for opcija in p["opcije"]:
            print(f" {opcija}")

        # Provera unosa (samo A, B ili C)
        odgovor = ""
        while odgovor not in ["A", "B", "C"]:
            odgovor = input("Tvoj odgovor (A/B/C): ").strip().upper()
            if odgovor not in ["A", "B", "C"]:
                print("⚠️ Nevažeći unos! Molimo unesite A, B ili C.")

        if odgovor == p["tacan_odgovor"]:
            print(print("✅ Tačno!\n"))
            skor += 1
        else:
            print(f"❌ Netačno. Tačan odgovor je: {p['tacan_odgovor']}\n")

    procenat = (skor / ukupno) * 100
    print("========================================")
    print(f"KRAJ TESTA! Tvoj rezultat: {skor}/{ukupno} ({procenat:.1f}%)")

    status = "POLOŽENO" if procenat >= 75 else "FALLEN / PADA"
    print(f"Status: {status}")
    print("========================================")

    # Čuvanje rezultata u fajl
    with open("rezultati.txt", "a", encoding="utf-8") as f:
        vreme = time.strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"[{vreme}] Rezultat: {skor}/{ukupno} ({procenat:.1f}%) - {status}\n")

    print("Rezultat je uspešno sačuvan u rezultati.txt!")

if __name__ == "__main__":
    pokreni_kviz()



