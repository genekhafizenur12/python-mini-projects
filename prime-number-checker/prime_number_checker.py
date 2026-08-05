"""
Girilen bir sayının asal olup olmadığını kontrol eden program.

Özellikler:
- Kullanıcıdan bir sayı alır.
- 1 ve daha küçük sayıların asal olmadığını kontrol eder.
- Asal olmayan sayılarda ilk böleni gösterir.
"""

sayi = int(input("Lütfen istediğiniz sayıyı giriniz: "))
asal = True

if sayi <= 1:
    print("1 ve daha küçük sayılar asal değildir.")
else:
    for i in range(2, sayi):
        if sayi % i == 0:
            asal = False
            break

    if asal:
        print(f"{sayi} asal bir sayıdır.")
    else:
        print(f"{sayi} asal bir sayı değildir.")
        print(f"{i} sayısına tam bölünmektedir.")