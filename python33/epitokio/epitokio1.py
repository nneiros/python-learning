kefalaio = int(input('Δώσε το αρχικό κεφάλαιο : '))
epitokio = float(input('Δώσε το επιτόκιο σε μορφή δεκαδικού : '))
years = 0
while years < 5 :
    years = years + 1
    tokos = kefalaio * epitokio
    kefalaio = kefalaio + tokos
    print (kefalaio)
