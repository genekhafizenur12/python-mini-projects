"""
Python Hesap Makinesi - v1
Toplama, çıkarma, çarpma, bölme, üs alma ve karekök işlemlerini destekler.
OOP tabanlı, hata yönetimi (try/except) içerir.
 
v2'de eklenecek: işlem geçmişinin dosyaya (.txt/.json) kaydedilmesi.
"""
import math

class Calculator:

    def topla(self,a,b):
        return a + b

    def cikar(self,a,b):
        return a - b

    def carp(self,a,b):
        return a * b

    def bolme(self,a,b):
        if b == 0 :
            raise ZeroDivisionError("Bir sayı 0' a bölünemez")
        return a / b

    def us_al(self,a,b):
        return a ** b

    def karekok(self,a):
        if a < 0 :
            raise ValueError("Negatif sayıların karekökü alınamaz.")
        return math.sqrt(a)


def menu_goster():

    print("\n╔══════════════════════════════════╗")
    print("║        PYTHON HESAP MAKİNESİ      ║")
    print("╠══════════════════════════════════╣")
    print("║  1. Toplama        (+)            ║")
    print("║  2. Çıkarma        (-)            ║")
    print("║  3. Çarpma         (*)            ║")
    print("║  4. Bölme          (/)            ║")
    print("║  5. Üs Alma        (^)            ║")
    print("║  6. Karekök        (√)            ║")
    print("║  0. Çıkış                         ║")
    print("╚══════════════════════════════════╝")


def sayi_al(sayi):

    while True:
        try:
            return float(input(sayi))
        except ValueError:
            print("Lütfen geçerli bir sayı giriniz.")


def main():
    hesap = Calculator()

    while True:
        menu_goster()
        secim = input("Seçiminiz: ")
        print(repr(secim))

        if secim == "0":
            print("\nProgramdan çıkılıyor. İyi günler!")
            break

        elif secim in ("1","2","3","4","5"):
            a = sayi_al("Birinci sayıyı girin: ")
            b = sayi_al("İkinci sayıyı girin: ")

            try:
                if secim == "1":
                    sonuc = hesap.topla(a,b)
                    islem = "+"

                elif secim == "2":
                    sonuc = hesap.cikar(a,b)
                    islem = "-"

                elif secim == "3":
                    sonuc = hesap.carp(a,b)
                    islem = "*"

                elif secim == "4":
                    sonuc = hesap.bolme(a,b)
                    islem = "/"

                elif secim == "5":
                    sonuc = hesap.us_al(a,b)
                    islem = "^"

                print("\n------------------------------------")
                print(f"   {a} {islem} {b} = {sonuc}")
                print("------------------------------------")

            except ZeroDivisionError as error:
                 print(f"\nHata: {error}")

        
        elif secim == "6":

            a = sayi_al("Karekökü alınacak sayıyı girin: ")
            try:
                sonuc = hesap.karekok(a)
                print("\n------------------------------------")
                print(f"   √{a} = {sonuc}")
                print("------------------------------------")

            except ValueError as e:
                 print(f"\nHata: {e}")
        
        else:
            print("\nGeçersiz seçim! Lütfen menüden bir seçenek girin.")

        devam = input("Devam etmek için Enter'a, çıkmak için Q'ya basınız: ")
        print("DEBUG:", repr(devam))
        if devam == "q" or devam == "Q":
            print("DEBUG: break tetiklendi")
            break

if __name__ == "__main__":   #Bu Python dosyası doğrudan çalıştırıldığında, programın ana işlemlerini yapan main() fonksiyonunu başlat.
    main()


