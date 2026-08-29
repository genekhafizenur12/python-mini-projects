def hesapla(islem,*args):
    """ #docstring#
    Verilen işlemi (topla/çıkar/çarp/böl) args içindeki sayılara uygular.
    islem: yapılacak işlem ("Topla", "Çıkar", "Çarp", "Böl")
    args: işleme girecek sayılar (istediğin kadar)
    return: işlem sonucu
    """
    if not args:
        print("Sayı giriniz!")
        return

    if islem == "Topla":
        sonuc = 0
        for sayi in args:
            sonuc += sayi

    elif islem == "Çıkar":
        sonuc = args[0]
        for sayi in args[1:]:  # args[1:] -> ilk sayı hariç geri kalan tüm sayıları alır (0. index'i atlar)
            sonuc -= sayi

    elif islem == "Çarp":
        sonuc = 1
        for sayi in args:
            sonuc *= sayi

    elif islem == "Böl":
        sonuc = args[0]
        for sayi in args[1:]:

            if sayi == 0:
                print("Bir sayıyı 0'a bölemezsiniz.")
                return
            
            sonuc /= sayi

    return sonuc

while True:
    print("\n1. Topla")
    print("2. Çıkar")
    print("3. Çarp")
    print("4. Böl")
    print("5. Çıkış Yap")

    secim = input("\nİstediğiz işlemi seçiniz: ")

    if secim == "1":
        islem = "Topla"
    elif secim == "2":
        islem = "Çıkar"
    elif secim == "3":
        islem = "Çarp"
    elif secim == "4":
        islem = "Böl"
    elif secim == "5":
        print("\nÇıkış yapıyorsunuz.")
        break
    else:
        print("Hatalı seçim!")
        continue

    sayilar_str = input("\nSayıları boşlukla ayırarak girin: ")
    parcalar = sayilar_str.split()

    try:
        sayilar = [float(sayi) for sayi in parcalar]
    except ValueError:
        print("Lütfen sadece sayı giriniz!")
        continue

    sonuc = hesapla(islem, *sayilar)
    print(sonuc)

