import random
playerIn = True
dealerIn = True
# deck of cards / player dealer hand
deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10,
        'J', 'Q', 'K', 'A''J', 'Q', 'K', 'A', 'J', 'Q', 'K', 'A', 'J', 'Q', 'K', 'A']
player_hand = []
dealer_hand = []


# deal the cards

def dealCard(turn):
    card = random.choice(deck)
    turn.append(card)
    deck.remove(card)


# calculate the total of each hand
def total(turn):
    total = 0
    face = ['J', 'K', 'Q']
    for card in turn:
        if card in range(1, 11):
            total += card
        elif card in face:
            total += 10
        else:
            if total > 11:
                total += 1
            else:
                total+=11
    return total

# check for winner

def revealDealerHand():
    if len(dealer_hand)==2:
        return dealer_hand[0]
    elif len(dealer_hand)>2:
        return dealer_hand[0],dealer_hand[1]


# game loop
for _ in range(2):
    dealCard(dealer_hand)
    dealCard(player_hand)

while playerIn or dealerIn:
    print(f'Dealer had {revealDealerHand()} and X')
    print(f'Your have {player_hand} for a total of {total(player_hand)}')
    if playerIn:
        stayorhit = input('1: Stay\n2: Hit\n')
    if total(dealer_hand)>16:
        dealerIn= False
    else:
        dealCard(dealer_hand)
    if stayorhit == '1':
        playerIn=False
    else:
        dealCard(player_hand)
    if total(player_hand) >= 21:
        break
    elif total(dealer_hand)>=21:
        break

if total(player_hand) == 21:
    print(f'\nYou have {player_hand} for a total of {total(player_hand)} and the dealer has {dealer_hand} for a total of {total(dealer_hand)}')
    print("BlackJack! You win!")
elif total(dealer_hand)==21:
    print(f'\nYou have {player_hand} for a total of {total(player_hand)} and the dealer has {dealer_hand} for a total of {total(dealer_hand)}')
    print("BlackJack! Dealer wins!")
elif total(player_hand)>21:
    print(f'\nYou have {player_hand} for a total of {total(player_hand)} and the dealer has {dealer_hand} for a total of {total(dealer_hand)}')
    print("You bust! Dealer wins!")
elif total(dealer_hand)>21:
    print(f'\nYou have {player_hand} for a total of {total(player_hand)} and the dealer has {dealer_hand} for a total of {total(dealer_hand)}')
    print("Dealer busts! You win!")
elif 21-total(dealer_hand)<21-total(player_hand):
    print(f'\nYou have {player_hand} for a total of {total(player_hand)} and the dealer has {dealer_hand} for a total of {total(dealer_hand)}')
    print("Dealer wins!")
elif 21-total(dealer_hand)>21-total(player_hand):
    print(f'\nYou have {player_hand} for a total of {total(player_hand)} and the dealer has {dealer_hand} for a total of {total(dealer_hand)}')
    print('You win!')

# print(f'Dealer Hand:{dealer_hand}')
# print(f'Player Hand:{player_hand}')



