"""
1-100 arasında rastgele bir sayı üreten sayı tahmin oyunu.

Özellikler:
- Kullanıcı istediği kadar hak belirleyebilir.
- Her yanlış tahminde hak ve puan azalır.
- Büyük/Küçük ipucu verilir.
- 1-100 dışındaki girişler kabul edilmez.
"""

import random

# Rastgele sayı oluştur
sayi = random.randint(1, 100)

# Hak sayısını al
hak = int(input("Kaç tane hakkınızın olmasını isterdiniz?: "))

while hak <= 0:
    hak = int(input("Hak sayısı en az 1 olabilir. Tekrar giriniz: "))

# Puan hesaplama
puan = 100
puan_kaybi = 100 // hak

# Oyun döngüsü
while hak > 0:
    tahmin = int(input("Tahmininiz: "))

    if tahmin < 1 or tahmin > 100:
        print("Lütfen 1 ile 100 arasında bir sayı giriniz.")
        continue

    if tahmin == sayi:
        print("🎉 Doğru Bildiniz!")
        print(f"Tutulan Sayı: {sayi}")
        print(f"Puanınız: {puan}")
        break

    hak -= 1
    puan -= puan_kaybi

    if hak > 0:
        if tahmin < sayi:
            print("Daha büyük bir sayı giriniz.")
        else:
            print("Daha küçük bir sayı giriniz.")

        print(f"Kalan Hak: {hak}")
        print(f"Puanınız: {puan}")

if hak == 0:
    print("Haklarınız bitti.")
    print(f"Tutulan Sayı: {sayi}")
    print(f"Puanınız: {puan}")