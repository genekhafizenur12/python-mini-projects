import random
import sys  # exit yerine sys.exit kullanmak için

player_score = 0
computer_score = 0
print("\nZar Oyununa Hoşgeldiniz!\n")

try:
    winning_score = int(input("Skor kaçta bitsin: "))

    if winning_score <= 0:
        raise ValueError("Skor 0'dan büyük olmalıdır.")

except ValueError:
    print("Geçersiz skor!")
    sys.exit()

while True:
    print("\nDevam etmek için Enter tuşuna basınız.")
    print("Oyundan çıkmak için q yazınız.")
    secim = input("Seçiminiz: ").strip().lower()

    if secim == "q":
        print("Oyun sonlandırıldı.")
        break

    if secim != "":
        print("Geçersiz seçim! Lütfen sadece Enter'a basın veya q yazın.")
        continue

    player_dice = random.randint(1, 6)
    computer_dice = random.randint(1, 6)

    print(f"\nZar sonucun: {player_dice}")
    print(f"Bilgisayarın zar sonucu: {computer_dice}")

    if player_dice > computer_dice:
        print("Kazandınız!")
        player_score += 1
    elif player_dice < computer_dice:
        print("Kaybettiniz!")
        computer_score += 1
    else:
        print("Berabere!")

    print(f"Skor => Sen: {player_score} | Bilgisayar: {computer_score}")

    if player_score >= winning_score:
        print(f"\nTebrikler! {winning_score} skoruna ulaşarak kazandınız!")
        break
    elif computer_score >= winning_score:
        print(f"\nBilgisayar {winning_score} skoruna ulaşarak kazandı!")
        break

print("\nOyun sona erdi!")
print(f"Toplam Skor => Sen: {player_score} | Bilgisayar: {computer_score}\n")