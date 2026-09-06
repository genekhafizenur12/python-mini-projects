ogrenciler = {}

def ogr_ekle():
    ad = str(input("Öğrencinin Adı: "))
    soyad = str(input("Öğrencinin Soyadı: "))

    try:
        numara = int(input("Öğrencinin Numarası: "))
    except ValueError:
        print("Geçersiz karakter!")
        return

    if numara in ogrenciler:
        print("Öğrenci zaten kayıtlı!")
        return
    else:
        ogrenciler[numara] = {
            "Ad": ad,
            "Soyad": soyad,
            "Numara": numara,
            "Notlar": [],
        }

def not_ekle():
    try:
        eklenecek_numara = int(input("Öğrencinin Numarası: "))
        eklenecek_not = int(input("Notu yazınız:"))
    except ValueError:
        print("Geçersiz Numara!")
        return

    if eklenecek_numara in ogrenciler:
        ogrenciler[eklenecek_numara]["Notlar"].append(eklenecek_not)
        print("Not eklendi!")
    else:
        print("Öğrenci bulunamadı!")
        return

def kyt_listele():
    if len(ogrenciler) == 0:
        print("öğrenci kaydı bulunamadı!")
        return
    else:
        for numara, bilgi in ogrenciler.items():
            print(bilgi["Ad"],bilgi["Soyad"],bilgi["Numara"],bilgi["Notlar"])

def kyt_ara():
    try:
        aranacak_ogr = int(input("\nAranacak öğrencinin numarası: "))
    except ValueError:
        print("Geçersiz Numara!")
        return

    if aranacak_ogr in ogrenciler:
        print(ogrenciler[aranacak_ogr]["Ad"],ogrenciler[aranacak_ogr]["Soyad"],ogrenciler[aranacak_ogr]["Numara"],ogrenciler[aranacak_ogr]["Notlar"])
    else:
        print("Öğrenci bulunamadı!")
        return

def kyt_sil():
    try:
        silinecek_numara = int(input("\nSilinecek öğrencinin numarası: "))
    except ValueError:
        print("Geçersiz Numara!")
        return

    if silinecek_numara in ogrenciler:
        ogrenciler.pop(silinecek_numara)
        print(f"'{silinecek_numara}' numaralı öğrenci silindi")
    else:
        print("Öğrenci bulunamadı!")
        return

def kyt_guncelle():
    try:
        guncellenecek_numara = int(input("Güncellenecek öğrencinin numrası: "))
    except ValueError:
        print("Geçersiz Numara!")
        return

    if guncellenecek_numara in ogrenciler:
        guncel_ad = str(input("\nÖğrencinin Güncellenmiş Adı: "))
        guncel_soyad = str(input("Öğrencinin Güncellenmiş Soyadı: "))

        ogrenciler[guncellenecek_numara]["Ad"] = guncel_ad
        ogrenciler[guncellenecek_numara]["Soyad"] = guncel_soyad

        print(f"'{guncellenecek_numara}' numaralı öğrencinin Adı ve Soyadı '{guncel_ad} {guncel_soyad}' olarak güncellendi.")

    else:
        print("Öğrenci bulunamadı!")
        return

def ort_goster():
    try:
        numara = int(input("Not ortalaması hesaplacak öğrencinin numarası: "))
    except ValueError:
        print("Geçersiz Numara!")
        return

    if numara in ogrenciler:
        if ogrenciler[numara]["Notlar"] == []:
            print(f"'{numara}' numaralı öğrencinin girilmiş bir notu yok!")
            return
        else:
            not_sayisi = len(ogrenciler[numara]["Notlar"])
            not_toplamlari = sum(ogrenciler[numara]["Notlar"])
            ort = not_toplamlari / not_sayisi
            print(f"'{numara}' numaralı öğrencinin not ortalaması: '{ort}' ")
    else:
        print("Öğrenci bulunamadı!")
        return


def harf_notu():
    pass

while True:
    print("="*30)
    print("---Öğrenci Bilgi Sistemi---")
    print("="*30)
    print("1. Öğrenci Ekle")
    print("2. Not Ekle")
    print("3. Ortalama Göster")
    print("4. Kayıt Listele")
    print("5. Kayıt Ara")
    print("6. Kayıt Sil")
    print("7. Kayıt Güncelle")
    print("8. Harf Notu Hesapla")
    print("9. Çıkış yap")
    print("="*30)

    try:
        secim = int(input("\nSeçiminiz: "))
    except ValueError:
        print("Hatalı seçim!")
        continue

    if secim == 1:
        ogr_ekle()
    elif secim == 2:
        not_ekle()
    elif secim == 3:
        ort_goster()
    elif secim == 4:
        kyt_listele()
    elif secim == 5:
        kyt_ara()
    elif secim == 6:
        kyt_sil()
    elif secim == 7:
        kyt_guncelle()
    elif secim == 8:
        harf_notu()
    elif secim == 9:
        print("Çıkış Yapıyorsunuz!")
        break


