import string
import random

  #ham string (r"""): \] gibi karakterlerde SyntaxWarning çıkmasın diye       
r"""                                                          
string.ascii_uppercase   # "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
string.ascii_lowercase   # "abcdefghijklmnopqrstuvwxyz"
string.digits            # "0123456789"
string.punctuation       # "!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
"""

def secimleri_oku(secimler):
    buyuk_harf = False
    kucuk_harf = False
    rakam = False
    ozel_karakter = False
    gecerli_secimler = ["1", "2", "3", "4"]

    for parca in secimler:
        if parca == "1":
            buyuk_harf = True

        if parca == "2":
            kucuk_harf = True

        if parca == "3":
            rakam = True

        if parca == "4":
            ozel_karakter = True

        if parca not in gecerli_secimler:   #isalnum(), bir karakterin harf ya da rakam olup olmadığına bakıyor
            print("Hatalı seçim!")

    return buyuk_harf, kucuk_harf, rakam, ozel_karakter

def sifre_uret(buyuk_harf, kucuk_harf, rakam, ozel_karakter, uzunluk):

    havuz = ""   # tüm izin verilen karakterlerin toplanacağı yer
    garanti = []

    if buyuk_harf == True:
        havuz += string.ascii_uppercase  # büyük harfleri havuza ekler
        garanti.append(random.choice(string.ascii_uppercase))  # garanti 1 tane büyük harf ekler

    if kucuk_harf == True:
        havuz += string.ascii_lowercase  # küçük harfleri havuza ekler
        garanti.append(random.choice(string.ascii_lowercase))   # garanti 1 tane küçük harf ekler

    if rakam == True:
        havuz += string.digits   #  rakamları havuza ekler
        garanti.append(random.choice(string.digits))   # garanti 1 tane rakam ekler

    if ozel_karakter == True:
        havuz += string.punctuation  # özel karakterleri havuza ekler
        garanti.append(random.choice(string.punctuation))   # garanti 1 tane özel karakter ekler
        
    sifre = ""
    for i in range(uzunluk - len(garanti)):
        sifre += random.choice(havuz)

    sifre += "".join(garanti)

    sifre_listesi = list(sifre)
    random.shuffle(sifre_listesi)
    sifre = "".join(sifre_listesi)

    return sifre

while True:
    try:
        uzunluk = int(input("\nŞifrenin uzunluğu kaç karakter olsun: "))
        if uzunluk < 4:
            raise ValueError("Karakter sanıyısı en az 4 olmalıdır")
    except:
        None

    print("\nHangi karakter tiplerini istiyorsunuz?")
    print("1-Büyük harf")
    print("2-Küçük harf")
    print("3-Rakam")
    print("4-Özel Karakter")
    secim = input("\nSeçimlerini virgülle ayırarak gir (örn: 1,2,3): ").split(",")

    buyuk_harf, kucuk_harf, rakam, ozel_karakter = secimleri_oku(secim)

    if not (buyuk_harf or kucuk_harf or rakam or ozel_karakter):
        print("\nHiçbir karakter tipi seçmediniz!")
        break

    if uzunluk < len(secim):
        print("\nSeçtiğiniz uzunluk, seçtiğiniz tipten az olamaz!")
        break
    else:
        sifre = sifre_uret(buyuk_harf, kucuk_harf, rakam, ozel_karakter, uzunluk)
        print("\n",sifre)
        devam = input("Başka bir şifre üretmek ister misiniz? (e/h): ").capitalize().strip()

        if devam == "H":
            print("Çıkış yapıyosunuz!")
            break
        elif devam == "E":
            pass
        else:
            print("Geçersiz seçim!")



