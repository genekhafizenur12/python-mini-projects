def uzunluk():
    print("\n1. Santimetre")
    print("2. Metre")
    print("3. Kilometre")
    print("4. Mil")
    print("5. Çıkış")

    try:
        kaynak_birim = input("\nHangi birimi cevirmek istersiniz(1-4): ")
        hedef_birim = input("Hangi birime çevirmek istiyorsunuz(1-4): ")
        deger = float(input("\nSayınızı giriniz: "))
    except ValueError:
        print("Sayı Giriniz!")
        return None, None, None, None

    if kaynak_birim == "1":
        metre_degeri = deger * 0.01
    elif kaynak_birim == "2":
        metre_degeri = deger
    elif kaynak_birim == "3":
        metre_degeri = deger * 1000
    elif kaynak_birim == "4":
        metre_degeri = deger * 1609.34
    elif kaynak_birim == "5":
        print("Çıkış Yapıyorsunuz!")
        return None, None, None, None
    else:
        print("Hatalı Seçim!")
        return None, None, None, None

    

    if hedef_birim == "1":
        sonuc_degeri = metre_degeri * 100
    elif hedef_birim == "2":
        sonuc_degeri = metre_degeri
    elif hedef_birim == "3":
        sonuc_degeri = metre_degeri / 1000
    elif hedef_birim == "4":
        sonuc_degeri = metre_degeri / 1609.34
    elif hedef_birim == "5":
        print("Çıkış Yapıyorsunuz!")
        return None, None, None, None
    else:
        print("Hatalı Seçim!")
        return None, None, None, None

    return sonuc_degeri, deger, kaynak_birim, hedef_birim

    
while True:

    print("\nBirim Dönüştürücüye Hoşgeldiniz")
    print("\n1. Uzunluk")
    print("2. Ağrlık")
    print("3. Sıcaklık")
    print("4. Çıkış")
    secim = input("\nSeçiminizi Yapınız: ")

    if secim == "1":
        sonuc_degeri, deger, kaynak_birim, hedef_birim = uzunluk()
        if sonuc_degeri is None:
            continue

        if kaynak_birim =="1":
            kaynak_birim = "Santimetre"
        elif kaynak_birim == "2":
            kaynak_birim = "Metre"
        elif kaynak_birim == "3":
            kaynak_birim = "Kilometre"
        elif kaynak_birim == "4":
            kaynak_birim = "Mil"

        if hedef_birim =="1":
            hedef_birim = "Santimetre"
        elif hedef_birim == "2":
            hedef_birim = "Metre"
        elif hedef_birim == "3":
            hedef_birim = "Kilometre"
        elif hedef_birim == "4":
            hedef_birim = "Mil"

        print(f"\n{deger} degerini {kaynak_birim} biriminden {hedef_birim} birimine çevrildi. Sonucunuz: {sonuc_degeri}")
    elif secim == "2":
        pass
    elif secim == "3":
        pass
    elif secim == "4":
        print("Çıkış Yapıyorsunuz!")
        exit()
    else:
        print("Hatalı Seçim!")
        break

    
    







