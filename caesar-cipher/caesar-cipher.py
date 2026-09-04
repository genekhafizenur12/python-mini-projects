metin = input("Metin: ")
kaydirma = int(input("Kaydırma değeri: "))

def sifreleme(metin, kaydirma):
    yeni_metin = ""
    for harf in metin:
        taban = ord("a")
        pozisyon = ord(harf) - taban
        yeni_pozisyon = (pozisyon + kaydirma) % 26 #Wrap-around: alfabenin sonuna gelen bir harfi kaydırırken, % 26 ile pozisyonu 0-25 aralığında tutup alfabenin başına geri sardırma işlemi.
        yeni_harf = chr(yeni_pozisyon + taban)
        yeni_metin += yeni_harf
    print(yeni_metin)
    return yeni_metin

def sifre_coz():
    pass


sifreleme(metin,kaydirma)
