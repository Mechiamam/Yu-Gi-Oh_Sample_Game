from random import choice

qliphort_decklist = ["Apoqliphort Towers", "Qliphort Shell", "Qliphort Stealth", "Qliphort Stealth",
                     "Qliphort Stealth", "Vanity's Ruler", "Qliphort Disk", "Odd-Eyes Pendulum Dragon",
                     "Odd-Eyes Pendulum Dragon", "Odd-Eyes Pendulum Dragon", "Qliphort Carrier",
                     "Qliphort Carrier", "Qliphort Carrier", "Qliphort Helix", "Qliphort Helix",
                     "Qliphort Helix", "Qliphort Monolith", "Qliphort Scout", "Qliphort Scout",
                     "Qliphort Scout", "Saqlifice", "Saqlifice", "Saqlifice", "Change of Heart",
                     "Harpie's Feather Duster", "Pot of Duality", "Pot of Duality", "Summoner's Art",
                     "Summoner's Art", "Summoner's Art", "Forbidden Chalice", "Forbidden Chalice",
                     "Forbidden Chalice", "Mystical Space Typhoon", "Mystical Space Typhoon",
                     "Mystical Space Typhoon", "The Monarchs Stormforth", "Skill Drain", "Skill Drain",
                     "Skill Drain"]
list_of_choices = ["Rock", "Paper", "Scissors"]
player_1_choice = choice(list_of_choices)
player_2_choice = choice(list_of_choices)
while player_1_choice == player_2_choice:
    player_1_choice = choice(list_of_choices)
    player_2_choice = choice(list_of_choices)
if player_1_choice == "Rock" and player_2_choice == "Scissors" \
        or player_1_choice == "Scissors" and player_2_choice == "Paper" \
        or player_1_choice == "Paper" and player_2_choice == "Scissors":
    card_1 = choice(qliphort_decklist)
    card_2 = choice(qliphort_decklist)
    card_3 = choice(qliphort_decklist)
    card_4 = choice(qliphort_decklist)
    card_5 = choice(qliphort_decklist)
    starting_hand = [card_1, card_2, card_3, card_4, card_5]
    print("You are going first")
else:
    card_1 = choice(qliphort_decklist)
    card_2 = choice(qliphort_decklist)
    card_3 = choice(qliphort_decklist)
    card_4 = choice(qliphort_decklist)
    card_5 = choice(qliphort_decklist)
    card_6 = choice(qliphort_decklist)
    starting_hand = [card_1, card_2, card_3, card_4, card_5, card_6]
    print("You are going second")

print(starting_hand)
