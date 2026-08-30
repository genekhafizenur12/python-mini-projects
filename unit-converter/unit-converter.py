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

def agirlik():
    print("\n1. Miligram")
    print("2. Gram")
    print("3. Kilogram")
    print("4. Pound(Libre)")
    print("5. Çıkış")

    try:
        kaynak_birim = input("\nHangi birimi cevirmek istersiniz(1-4): ")
        hedef_birim = input("Hangi birime çevirmek istiyorsunuz(1-4): ")
        deger = float(input("\nSayınızı giriniz: "))
    except ValueError:
        print("Sayı Giriniz!")
        return None, None, None, None

    if kaynak_birim == "1":
        gram_degeri = deger * 0.01
    elif kaynak_birim == "2":
        gram_degeri = deger
    elif kaynak_birim == "3":
        gram_degeri = deger * 1000
    elif kaynak_birim == "4":
        gram_degeri = deger * 453.592
    elif kaynak_birim == "5":
        print("Çıkış Yapıyorsunuz!")
        return None, None, None, None
    else:
        print("Hatalı Seçim!")
        return None, None, None, None

    if hedef_birim == "1":
        sonuc_degeri = gram_degeri * 100
    elif hedef_birim == "2":
        sonuc_degeri = gram_degeri
    elif hedef_birim == "3":
        sonuc_degeri = gram_degeri / 1000
    elif hedef_birim == "4":
        sonuc_degeri = gram_degeri / 453.592
    elif hedef_birim == "5":
        print("Çıkış Yapıyorsunuz!")
        return None, None, None, None
    else:
        print("Hatalı Seçim!")
        return None, None, None, None
    
    return sonuc_degeri, deger, kaynak_birim, hedef_birim

def sicaklik():
    print("\n1. Celsius(°C)")
    print("2. Fahrenheit(°F)")
    print("3. Kelvin(K)")
    print("4. Çıkış")

    try:
        kaynak_birim = input("\nHangi birimi cevirmek istersiniz(1-4): ")
        hedef_birim = input("Hangi birime çevirmek istiyorsunuz(1-4): ")
        deger = float(input("\nSayınızı giriniz: "))
    except ValueError:
        print("Sayı Giriniz!")
        return None, None, None, None

    if kaynak_birim == "1":
        Celsius_degeri = deger 
    elif kaynak_birim == "2":
        Celsius_degeri = (deger - 32) * 5/9
    elif kaynak_birim == "3":
        Celsius_degeri = deger - 273.15
    elif kaynak_birim == "4":
        print("Çıkış Yapıyorsunuz!")
        return None, None, None, None
    else:
        print("Hatalı Seçim!")
        return None, None, None, None

    if hedef_birim == "1":
        sonuc_degeri = Celsius_degeri 
    elif hedef_birim == "2":
        sonuc_degeri = ( Celsius_degeri * 9/5) + 32
    elif hedef_birim == "3":
        sonuc_degeri = Celsius_degeri + 273.15
    elif hedef_birim == "4":
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

    elif secim == "2":
        sonuc_degeri, deger, kaynak_birim, hedef_birim = agirlik()
        if sonuc_degeri is None:
            continue

        if kaynak_birim =="1":
            kaynak_birim = "Miligram"
        elif kaynak_birim == "2":
            kaynak_birim = "Gram"
        elif kaynak_birim == "3":
            kaynak_birim = "Kilogram"
        elif kaynak_birim == "4":
            kaynak_birim = "Pound(Libre)"
        
        if hedef_birim =="1":
            hedef_birim = "Miligram"
        elif hedef_birim == "2":
            hedef_birim = "Gram"
        elif hedef_birim == "3":
            hedef_birim = "Kilogram"
        elif hedef_birim == "4":
            hedef_birim = "Pound(Libre)"

    elif secim == "3":
        sonuc_degeri, deger, kaynak_birim, hedef_birim = sicaklik()
        if sonuc_degeri is None:
            continue

        if kaynak_birim =="1":
            kaynak_birim = "Celsius(°C)"
        elif kaynak_birim == "2":
            kaynak_birim = "Fahrenheit(°F)"
        elif kaynak_birim == "3":
            kaynak_birim = "Kelvin(K)"
        
        if hedef_birim =="1":
            hedef_birim = "Celsius(°C)"
        elif hedef_birim == "2":
            hedef_birim = "Fahrenheit(°F)"
        elif hedef_birim == "3":
            hedef_birim = "Kelvin(K)"
        
    elif secim == "4":
        print("Çıkış Yapıyorsunuz!")
        exit()
    else:
        print("Hatalı Seçim!")
        break

    print(f"\n{deger} degerini {kaynak_birim} biriminden {hedef_birim} birimine çevrildi. Sonucunuz: {round(sonuc_degeri, 2)}")

    
    







