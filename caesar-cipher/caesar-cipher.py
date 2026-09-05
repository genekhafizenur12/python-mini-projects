def sifreleme(metin, kaydirma):
    yeni_metin = ""
    for harf in metin:
        if harf.isalpha():
            if harf.islower():
                taban = ord("a")
                pozisyon = ord(harf) - taban
                yeni_pozisyon = (pozisyon + kaydirma) % 26 #Wrap-around: alfabenin sonuna gelen bir harfi kaydırırken, % 26 ile pozisyonu 0-25 aralığında tutup alfabenin başına geri sardırma işlemi.
                yeni_harf = chr(yeni_pozisyon + taban)
                yeni_metin += yeni_harf
            else:
                taban = ord("A")
                pozisyon = ord(harf) - taban
                yeni_pozisyon = (pozisyon + kaydirma) % 26 #Wrap-around: alfabenin sonuna gelen bir harfi kaydırırken, % 26 ile pozisyonu 0-25 aralığında tutup alfabenin başına geri sardırma işlemi.
                yeni_harf = chr(yeni_pozisyon + taban)
                yeni_metin += yeni_harf
        else:
            yeni_metin += harf
    print(f"\nSonuç: {yeni_metin}")

def sifre_coz(metin,kaydirma):
    cozulmus_metin = ""
    for harf in metin:
        if harf.isalpha():
            if harf.islower():
                taban = ord("a")
                pozisyon = ord(harf) - taban
                yeni_pozisyon = (pozisyon - kaydirma) % 26 
                yeni_harf = chr(yeni_pozisyon + taban)
                cozulmus_metin += yeni_harf
            else:
                taban = ord("A")
                pozisyon = ord(harf) - taban
                yeni_pozisyon = (pozisyon - kaydirma) % 26 
                yeni_harf = chr(yeni_pozisyon + taban)
                cozulmus_metin += yeni_harf
        else:
            cozulmus_metin += harf
    print(f"\nSonuç: {cozulmus_metin}")

while True:
    print("\n" + "="*30)
    print("   CAESAR CIPHER")
    print("="*30)
    print("1. Şifre Oluşturmak")
    print("2. Şifre Çözmek")
    print("3. Çıkış yap")
    print("="*30)

    secim = input("\nSeciminizi girin: (1,2,3) ")

    if secim == "1":
        metin = input("\nMetin: ")
        kaydirma = int(input("Kaydırma değeri: "))
        if kaydirma <= 0:
            print("Kaydırma değeri en az 1 olmalı!")
            continue
        sifreleme(metin,kaydirma)
    elif secim == "2":
        metin = input("Metin: ")
        kaydirma = int(input("Kaydırma değeri: "))
        if kaydirma <= 0:
            print("Kaydırma değeri en az 1 olmalı!")
            continue
        sifre_coz(metin,kaydirma)
    elif secim == "3":
        print("Çıkış yapıyorsunuz.")
        break
    else:
        print("Geçersiz seçim, lütfen 1, 2 veya 3 girin.")
        continue
