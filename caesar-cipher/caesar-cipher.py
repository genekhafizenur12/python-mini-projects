"""
Caesar Cipher - Simple Encryption Program

This program encrypts or decrypts text entered by the user using a
given shift value. It supports the Turkish alphabet (ç, ğ, ı, ö, ş, ü),
preserving spaces and punctuation marks unchanged. Both uppercase and
lowercase letters are handled correctly.

Usage: python3 caesar-cipher.py
"""
kucuk_alfabe = "abcçdefgğhıijklmnoöprsştuüvyz"
buyuk_alfabe = "ABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZ"

def sifreleme(metin, kaydirma, kucuk_alfabe,buyuk_alfabe):
    """
        Encrypts the given text using the Caesar Cipher method,
        supporting the Turkish alphabet.

        Parameters:
            metin (str): The text to encrypt
            kaydirma (int): Number of positions to shift each letter
            kucuk_alfabe (str): Alphabet used for lowercase letters
            buyuk_alfabe (str): Alphabet used for uppercase letters

        Returns:
            str: The encrypted text
    """
    yeni_metin = ""
    for harf in metin:
        if harf.isalpha():
            if harf.islower():
                pozisyon = kucuk_alfabe.index(harf)
                yeni_pozisyon = (pozisyon + kaydirma) % 29 #Wrap-around: alfabenin sonuna gelen bir harfi kaydırırken, % 26 ile pozisyonu 0-25 aralığında tutup alfabenin başına geri sardırma işlemi.
                yeni_harf = kucuk_alfabe[yeni_pozisyon]
                yeni_metin += yeni_harf
            else:
                pozisyon = buyuk_alfabe.index(harf)
                yeni_pozisyon = (pozisyon + kaydirma) % 29 
                yeni_harf = buyuk_alfabe[yeni_pozisyon]
                yeni_metin += yeni_harf
        else:
            yeni_metin += harf
    print(f"\nSonuç: {yeni_metin}")

def sifre_coz(metin,kaydirma):
    """
    Decrypts text that was encrypted with the Caesar Cipher method,
    supporting the Turkish alphabet.

    Parameters:
        metin (str): The encrypted text to decrypt
        kaydirma (int): The shift value originally used for encryption

    Returns:
        str: The original (decrypted) text
    """
    cozulmus_metin = ""
    for harf in metin:
        if harf.isalpha():
            if harf.islower():
                pozisyon = kucuk_alfabe.index(harf)
                yeni_pozisyon = (pozisyon - kaydirma) % 29 
                yeni_harf = kucuk_alfabe[yeni_pozisyon]
                cozulmus_metin += yeni_harf
            else:
                pozisyon = buyuk_alfabe.index(harf)
                yeni_pozisyon = (pozisyon - kaydirma) % 29
                yeni_harf = buyuk_alfabe[yeni_pozisyon]
                cozulmus_metin += yeni_harf
        else:
            cozulmus_metin += harf
    print(f"\nSonuç: {cozulmus_metin}")

while True:
    print("\n" + "="*30)
    print("   CAESAR CIPHER")
    print("="*30)
    print("1. Şifre Oluşturmak")
    print("2. Şifre Çözmek")
    print("3. Çıkış yap")
    print("="*30)

    secim = input("\nSeciminizi girin: (1,2,3) ")

    if secim == "1":
        metin = input("\nMetin: ")
        kaydirma = int(input("Kaydırma değeri: "))
        if kaydirma <= 0:
            print("Kaydırma değeri en az 1 olmalı!")
            continue
        sifreleme(metin,kaydirma,kucuk_alfabe,buyuk_alfabe)
    elif secim == "2":
        metin = input("Metin: ")
        kaydirma = int(input("Kaydırma değeri: "))
        if kaydirma <= 0:
            print("Kaydırma değeri en az 1 olmalı!")
            continue
        sifre_coz(metin,kaydirma)
    elif secim == "3":
        print("Çıkış yapıyorsunuz.")
        break
    else:
        print("Geçersiz seçim, lütfen 1, 2 veya 3 girin.")
        continue
