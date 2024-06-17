import random

# Määratud kaardi väärtused
card_values = {
    "A": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 10, "Q": 10, "K": 10
}

# Kasutaja ja mängija kaarte
user_cards = []
dealer_cards = []

# Alustades mängu, annab kasutaja ja mängijale kaks kaarti
for i in range(2):
    user_cards.append(random.choice(list(card_values.keys())))
    dealer_cards.append(random.choice(list(card_values.keys())))

# Kasutaja mäng
while True:
    # Kasutaja punkte
    user_points = sum([card_values[card] for card in user_cards])

    # Kasutaja küsitlus
    user_input = input("Kas soovite lisaks kaardi? (jah/ei) ")

    # Lisaks kaarti, kuni kasutaja ei täida 21 või ületab
    if user_input == "jah":
        user_cards.append(random.choice(list(card_values.keys())))
    else:
        break

# Tulemused
print("Kasutaja punkte:", user_points)
print("Mängija punkte:", sum([card_values[card] for card in dealer_cards]))

# Kasutaja võidab, kui täidab 21 või mängija läheb 21 ületab
if user_points == 21:
    print("Kasutaja võitis!")
elif user_points > 21:
    print("Kasutaja kaotas.")
else:
    # Mängija mäng
    while sum([card_values[card] for card in dealer_cards]) < 16:
        dealer_cards.append(random.choice(list(card_values.keys())))

    # Tulemused