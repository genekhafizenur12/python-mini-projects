import random
player_score = 0
computer_score = 0

secenekler = ["Taş","Kağıt","Makas"]

def get_winning_score():
    try:
        winning_score = int(input("Skor kaçta bitsin: "))

        if winning_score <= 0:
            raise ValueError("Skor 0'san büyük olmalıdır.")
    
    except ValueError:
        print("Geçersiz skor!")
        exit()

    return winning_score

def get_player_choice(secenekler):
    while True:
        player_choice = input("\nSeçiminizi yazınız: ").capitalize()

        if player_choice not in secenekler:
            print("\nSeçiminiz hatalı. Lütfen 'Taş', 'Kağıt', 'Makas' seçimlerinden birini yapınız.")
            continue

        return player_choice

def winner(player_choice,computer_choice,player_score,computer_score):
    if player_choice == computer_choice:
        print("\nBerabere!")
    elif player_choice == "Taş" and computer_choice == "Kağıt":
        print("\nKaybettiniz!")
        computer_score += 1
    elif player_choice == "Taş" and computer_choice == "Makas":
        print("\nKazandınız!")
        player_score += 1
    elif player_choice == "Kağıt" and computer_choice == "Taş":
        print("\nKazandınız!")
        player_score += 1
    elif player_choice == "Kağıt" and computer_choice == "Makas":
        print("\nKaybettiniz!")
        computer_score += 1
    elif player_choice == "Makas" and computer_choice == "Taş":
        print("\nKaybettiniz!")
        computer_score += 1
    elif player_choice == "Makas" and computer_choice == "Kağıt":
        print("\nKazandınız!")
        player_score += 1
    else:
        print("\nHata!")

    return player_score, computer_score

def score_yazdir(player_choice, computer_choice, player_score, computer_score):
    print(f"\nSizin seçimiz: {player_choice}, Bilgisayarın seçimi: {computer_choice} ")
    print(f"\nSkorlar=> Siz: {player_score}, Bilgisayar: {computer_score}")

winning_score = get_winning_score()

while True:
    print("\nDevam etmek için Enter tuşuna basınız.")
    print("\nÇıkmak için q yazınız.")                   #lower() bütün harfleri küçültür.
    secim = input("\nDevam/çık: ").strip().lower()      #strip() baştaki ve sondaki boşlukları siler.
                                                     
    if secim == "q":
        print("\nOyun sonlandırıldı.")
        break

    if secim !="":
        print("\nGeçersiz seçim.")
        continue

    player_choice= get_player_choice(secenekler)
    computer_choice = random.choice(secenekler)

    player_score, computer_score = winner(player_choice,computer_choice,player_score,computer_score)

    if player_score >= winning_score:
        print(f"\nTebrikler! {winning_score} skoruna ulaşarak kazandınız!")
        break
    elif computer_score >= winning_score:
        print(f"\nBilgisayar {winning_score} skoruna ulaşarak kazandı!")
        break

    score_yazdir(player_choice, computer_choice, player_score, computer_score)



