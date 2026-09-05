aktif_gorevler = []
tamamlanan_gorevler =[]

def gorev_ekle():
    print("\nEklemek istediğiniz görevi yaznız:") 
    eklenecek_gorev = input("=> ")

    aktif_gorevler.append(eklenecek_gorev)

def gorev_listele():
    for numara, gorev in enumerate(aktif_gorevler,start = 1):
        print(f"{numara}. {gorev}")

    print("\n")

def gorev_tamamla():
    gorev_listele()

    try:
        tamamlananlar = int(input("\nHangi görevi tamamladınız numarasını yazınız: "))
    except ValueError:
        print("Hata!")
        return

    if 1 <= tamamlananlar <= len(aktif_gorevler):
        secilen_gorev = aktif_gorevler[tamamlananlar - 1]
        aktif_gorevler.remove(secilen_gorev)
        tamamlanan_gorevler.append(secilen_gorev)
        print(f"\n'{secilen_gorev}' tamamlandı olarak işaretlendi")
    else:
        print("\nGeçersiz numara, böyle bir görev yok.")

    print("\n")

def gorev_sil():
    gorev_listele()

    try:
        silinecekler = int(input("\nHangi görevi silmek istersiniz: "))
    except ValueError:
        print("Hata!")
        return

    if 1 <= silinecekler <= len(aktif_gorevler):
        silinecek_gorev = aktif_gorevler[silinecekler-1]
        aktif_gorevler.remove(silinecek_gorev)
        print(f"\n'{silinecek_gorev}' görevlerden silindi.")
    else:
        print("\nGeçersiz numara, böyle bir görev yok.")

    print("\n")

def gorev_sirala():
    aktif_gorevler.sort()
    gorev_listele()

    print("\n")

def son_eklenenler(): 
    eklenen = aktif_gorevler[-3:]
    for gorev in eklenen:
        print(f"\n{gorev}")

    print("\n")

while True:
    print("="*30)
    print("TO-DO LIST")
    print("="*30)
    print("1. Görev Ekle")
    print("2. Görevleri Listele")
    print("3. Tamamlanmış Görev Ekle")
    print("4. Görev Sil")
    print("5. Görevleri Sırala")
    print("6. Son Eklenen Görevler")
    print("7. Çıkış Yap")
    print("="*30)

    try:
        secim = int(input("Seçiminiz: "))
    except ValueError:
        print("Geçersiz seçim!")
        return
    
    if secim == 1:
        gorev_ekle()
    elif secim == 2:
        gorev_listele()
    elif secim == 3:
        gorev_tamamla()
    elif secim == 4:
        gorev_sil()
    elif secim == 5:
        gorev_sirala()
    elif secim == 6:
        son_eklenenler()
    elif secim == 7:
        print("Çıkış yapıyorsunuz:")
        break









    



        


