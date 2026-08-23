kilo = float(input("Kilonuzu kilogram cinsinden giriniz: "))
boy_cm = float(input("Boyunuzu santim cinsinden giriniz: "))


def Bilgiler(kilo,boy_cm):
    try:
        if kilo <= 0 or boy_cm <= 0:
            raise ValueError("Lütfen bilgilerinizi doğru giriniz.")
    except ValueError:
        print("Hata!")
        exit()
    return kilo,boy_cm


def BMI_hesaplama(kilo,boy_cm):
    boy = boy_cm / 100
    BMI = kilo / boy ** 2
    BMI = round(BMI,1)
    return BMI

def BMI_kategori(BMI):
    if BMI <= 18.5:
        kategori = "Zayıf"
    elif 18.5 < BMI <= 24.9:
        kategori = "Normal"
    elif 24.9 < BMI <= 29.9:
        kategori = "Fazla kilolu"
    elif 29.9 < BMI:
        kategori = "Obez"
    return kategori

BMI = BMI_hesaplama(kilo,boy_cm)
kategori = BMI_kategori(BMI)

print(f"\nBMI sonucunuz: {BMI}, Kategoriniz: {kategori}")