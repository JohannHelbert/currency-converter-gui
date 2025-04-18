import tkinter as tk
import requests

# Funktion für die Umrechnung


def umrechnen():
    try:
        betrag = float(betrag_entry.get())
        von = von_var.get()
        zu = zu_var.get()

        # API-URL für die Währungsumrechnung
        url = f"https://api.exchangerate-api.com/v4/latest/{von}"

        # API-Anfrage senden
        response = requests.get(url)
        data = response.json()

        if response.status_code == 200:
            # Umrechnungsrate aus der API-Daten extrahieren
            if zu in data['rates']:
                umrechnungsrate = data['rates'][zu]
                umgerechneter_betrag = betrag * umrechnungsrate
                ergebnis_label.config(
                    text=f"Ergebnis: {umgerechneter_betrag:.2f} {zu}")
            else:
                ergebnis_label.config(text="Ungültige Zielwährung!")
        else:
            ergebnis_label.config(
                text="Fehler bei der Umrechnung! API-Anfrage fehlgeschlagen.")
    except ValueError:
        ergebnis_label.config(text="Bitte gültigen Betrag eingeben!")
    except requests.exceptions.RequestException as e:
        ergebnis_label.config(text=f"Fehler bei der API-Anfrage: {e}")


# Fenster erstellen
root = tk.Tk()
root.title("Währungsrechner")
root.geometry("300x250")

# Betrag eingeben
betrag_label = tk.Label(root, text="Betrag:")
betrag_label.pack()
betrag_entry = tk.Entry(root)
betrag_entry.pack()

# Währungen definieren
waehrungen = [
    "AED", "AFN", "ALL", "AMD", "ANG", "AOA", "ARS", "AUD", "AWG", "AZN",
    "BAM", "BBD", "BDT", "BGN", "BHD", "BIF", "BMD", "BND", "BOB", "BRL",
    "BSD", "BTN", "BWP", "BYN", "BZD", "CAD", "CDF", "CHF", "CLP", "CNY",
    "COP", "CRC", "CUC", "CUP", "CVL", "CZK", "DJF", "DKK", "DOP", "DZD",
    "EGP", "ERN", "ETB", "EUR", "FJD", "FKP", "FOK", "GBP", "GEL", "GHS",
    "GIP", "GMD", "GNF", "GTQ", "GYD", "HKD", "HNL", "HRK", "HTG", "HUF",
    "IDR", "ILS", "INR", "IQD", "IRR", "ISK", "JMD", "JOD", "JPY", "KES",
    "KGS", "KHR", "KMF", "KPW", "KRW", "KWD", "KYD", "KZT", "LAK", "LBP",
    "LKR", "LRD", "LSL", "LTL", "LVL", "LYD", "MAD", "MDL", "MGA", "MKD",
    "MMK", "MNT", "MOP", "MRU", "MUR", "MVR", "MWK", "MXN", "MYR", "MZN",
    "NAD", "NGN", "NIO", "NOK", "NPR", "NZD", "OMR", "PAB", "PEN", "PGK",
    "PHP", "PKR", "PLN", "PRB", "PYG", "QAR", "RON", "RSD", "RUB", "RWF",
    "SAR", "SBD", "SCR", "SDG", "SEK", "SGD", "SHP", "SLL", "SOS", "SPL",
    "SRD", "SSP", "STD", "SYP", "SZL", "THB", "TJS", "TMT", "TND", "TOP",
    "TRY", "TTD", "TVD", "TWD", "TZS", "UAH", "UGX", "USD", "UYU", "UZS",
    "VEF", "VND", "VUV", "WST", "XAF", "XCD", "XDR", "XOF", "XPF", "YER",
    "ZAR", "ZMW", "ZWD"
]


# Von-Währung auswählen
von_Label = tk.Label(root, text="Von:")
von_Label.pack()
von_var = tk.StringVar(value="EUR")
von_menu = tk.OptionMenu(root, von_var, *waehrungen)
von_menu.pack()

# Zu-Währung auswählen
zu_Label = tk.Label(root, text="Zu:")
zu_Label.pack()
zu_var = tk.StringVar(value="USD")
zu_menu = tk.OptionMenu(root, zu_var, *waehrungen)
zu_menu.pack()

# Button für Umrechnung
umrechnen_button = tk.Button(root, text="Umrechnen", command=umrechnen)
umrechnen_button.pack()

# Label für das Ergebnis
ergebnis_label = tk.Label(root, text="Ergebnis:")
ergebnis_label.pack()

# Hauptloop starten
root.mainloop()
