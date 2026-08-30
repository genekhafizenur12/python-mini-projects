print("\nŞifreniz en az bir bütük harf içermelidir.")
print("Şifreniz en az bir küçük harf içermelidir.")
print("Şifreniz en az bir rakam içermelidir.")
print("Şifreniz en az bir özel karakter içermelidir.")
print("Şifreniz en az 8 karakter içermelir.")

sifre = input("\nşifrenizi girin: ")

def sifre_olusturucu(sifre):
    buyuk_var = False
    kucuk_var = False
    rakam_var = False
    ozel_karakter_var = False

    for harf in sifre:
        if harf.isupper():
            buyuk_var = True
        elif harf.islower():
            kucuk_var = True
        elif harf.isdigit():
            rakam_var = True
        elif not harf.isalnum():
            ozel_karakter_var = True

    if len(sifre) < 8:
        print("\nŞifreniz en az 8 karakter içermelir.")
        uzunluk = False
    else:
        uzunluk = True

    if buyuk_var == False:
        print("Şifreniz en az bir bütük harf içermelidir.")
    if kucuk_var == False:
        print("Şifreniz en az bir küçük harf içermelidir.")
    if rakam_var == False:
        print("Şifreniz en az bir rakam içermelidir.")
    if ozel_karakter_var == False:
        print("Şifreniz en az bir özel karakter içermelidir.")
    if buyuk_var == True and kucuk_var == True and rakam_var == True and ozel_karakter_var == True and uzunluk == True:
        print("Şifreniz kurallara uygun!")

    return sifre

sonuc = sifre_olusturucu(sifre)





            


        

    
