def ogrenci_ekle():
    ad = input("\nAdınız: ").capitalize()
    soyad = input("\nSoyad: ").capitalize()

    try:
        okul_no = int(input("\nOkul Numaranız: "))

        if okul_no <= 0:
            raise ValueError("Okul numarası 0 dan büyük olmalıdır.")
        
    except ValueError:
        return None

    with open("ogrenciler.txt","a", encoding="utf-8") as dosya:
        dosya.write(f"\n{ad}, {soyad}, {okul_no}")

def ogrenci_listele():
    with open("ogrenciler.txt","r", encoding="utf-8") as dosya:
        okuma = dosya.read()
    return okuma

def ogrenci_ara():
    try:
        aranacak_numara = int(input("\nAramak istediğiniz numarayı girin: "))
    
        if aranacak_numara <= 0:
            raise ValueError("Okul numarası 0 dan büyük olmalıdır.")
        
    except ValueError:
            return None
    
    with open("ogrenciler.txt","r", encoding= "utf-8") as dosya:
        satirlar = dosya.readlines()

    bulundu = False
    
    for satir in satirlar:                               # .strip() Satır sonlarındaki \n leri temizler
        parcalar = satir.strip().split(",")              # .split() Satırı virgüllerden bölerek listeye çevirir.
        if parcalar[2].strip() == str(aranacak_numara):     # "Ali, Yılmaz, 101" → ["Ali", " Yılmaz", " 101"]
            print(f"\nBulundu: {satir.strip()}")         #Yani parcalar[0] = ad, parcalar[1] = soyad, parcalar[2] = okul no.
            bulundu = True
            break

    if not bulundu:
         print(f"\n{aranacak_numara} numaralı bir öğrenci bulunamadı.")

def ogrenci_guncelle():
    try:
        guncellenecek_numara = int(input("\nGüncellemek istediğiniz öğrencinin numarasını giriniz: "))
        
        if guncellenecek_numara <= 0:
            raise ValueError("Okul numarası 0 dan büyük olmalıdır.")
        
    except ValueError:
          return None

    with open("ogrenciler.txt","r", encoding="utf-8") as dosya:
        satirlar = dosya.readlines()

    yeni_satirlar = []
    for satir in satirlar:
        parcalar = satir.strip().split(",")
        if parcalar[2].strip() == str(guncellenecek_numara):

            ad_guncelleme = input("Öğrencinin Adını güncelleyiniz. Güncelleme yapmayacaksanız Enter'a basın: ")
            if ad_guncelleme == "":
                pass  # kullanıcı boş geçti, ad_guncelleme'yi kullanmayacağız
            else:
                parcalar[0] = ad_guncelleme

            soyad_guncelleme = input("Öğrencinin Soyadını güncelleyiniz. Güncelleme yapmayacaksanız Enter'a basın: ")
            if soyad_guncelleme == "":
                pass  
            else:
                parcalar[1] = soyad_guncelleme
            
            numara_guncelleme = input("Öğrencinin Numarasını güncelleyiniz. Güncelleme yapmayacaksanız Enter'a basın: ")
            if numara_guncelleme == "":
                pass  
            else:
                parcalar[2] = numara_guncelleme

            yeni_satirlar.append(f"{parcalar[0]}, {parcalar[1]}, {parcalar[2]}\n")
        else:
            yeni_satirlar.append(satir)
        
    with open("ogrenciler.txt", "w", encoding="utf-8") as dosya:
        dosya.writelines(yeni_satirlar)

def ogrenci_sil():
    try:
        silinecek_no = int(input("\nSilinecek öğrencinin numarası: "))
            
        if silinecek_no <= 0:
            raise ValueError("Okul numarası 0 dan büyük olmalıdır.")
    except ValueError:
        return None

    with open("ogrenciler.txt","r", encoding="utf-8") as dosya:
        satirlar = dosya.readlines()

    yeni_satirlar = []
    for satir in satirlar: #her satırı tek tek kontrol et, eğer silinecek numara o satırda geçmiyorsa, yeni listeye ekle
        parcalar = satir.strip().split(",")

        if len(parcalar) != 3:
            continue 

        if parcalar[2].strip() == str(silinecek_no):
            continue
        else:
            yeni_satirlar.append(satir)

    if len(satirlar) == len(yeni_satirlar): #silinen satır olmamış.
        return None
    else:
        with open("ogrenciler.txt","w", encoding="utf-8") as dosya:
            dosya.writelines(yeni_satirlar)
        return silinecek_no

while True:
    print("\n1. Öğrenci Ekle")
    print("2. Öğremcileri Listele")
    print("3. Ara")
    print("4. Güncelle")
    print("5. Öğrenci Sil")
    print("6. Çıkış")
    secim = input("\nSeçiminiz: ")

    if secim == "1":
        ogrenci_ekle()

    elif secim == "2":
        liste = ogrenci_listele()
        print(liste)
    elif secim == "3":
        ogrenci_ara()

    elif secim == "4":
        ogrenci_guncelle()

    elif secim == "5":
        silinen = ogrenci_sil()

    elif secim == "6":
        print("Çıkış yapıyorsunuz.")
        break

    else:
        print("Hata!")
        

