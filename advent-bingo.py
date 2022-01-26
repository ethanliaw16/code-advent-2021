#day 4
import sys
def win(card):
    i = 0
    while i <= 20:
        row = card[i:i + 5]
        if sum(row) == 0:
            return True
        i += 5
    i = 0
    while i < 5:
        col = [card[i], card[i + 5], card[i + 10], card[i + 15], card[i + 20]]
        if sum(col) == 0:
            return True
        i += 1
    return False

def play_bingo(draws, cards):
    num_cards = len(cards)
    for draw in draws:
        to_remove = -1
        won = False
        #i = 0
        cards_to_remove = []
        for i in range(num_cards):
            card = cards[i]
            if draw in card:
                card[card.index(draw)] = 0
                if(win(card)):
                    won = True
                    cards_to_remove.append(i)
                    #cards = cards[:i] + cards[i + 1:]
                    if len(cards) - len(cards_to_remove) == 1:
                        print(f"Win! draw {draw} card {i}, {card}\nsum of remaining is {sum(card)}, output will be {draw * sum(card)}")
                        return f"Win! draw {draw} card {i}, {card}"
        if len(cards_to_remove) > 0:
            print(f"cards to remove: {cards_to_remove}")
            remaining_cards = cards[:cards_to_remove[0]]
            if len(cards_to_remove) > 1:
                for i in range(len(cards_to_remove) - 1):
                    remaining_cards += cards[cards_to_remove[i] + 1:cards_to_remove[i + 1]]
                remaining_cards += cards[cards_to_remove[len(cards_to_remove)- 1]:]
            else:
                remaining_cards += cards[cards_to_remove[0] + 1:]
            cards = remaining_cards
            num_cards = len(cards)
        print(f"{num_cards} cards remaining")

previous_was_newline = False
first_line = True
draws = []
cards = []
card = []
for line in sys.stdin:
    if(first_line):
        draw_input = line.replace('\n','').split(',')
        for draw in draw_input:
            draws.append(int(draw))
        first_line = False
    else:
        if line[:-1] == '':
            #print("empty!")
            if previous_was_newline:
                break
            if len(card) > 0:
                cards.append(card)
            card = []
            previous_was_newline = True
        else:
            row =  line.replace('\n','').split(' ')
            while('' in row):
                row.remove('')
            for num in row:
                card.append(int(num))
            previous_was_newline = False

testcard = [3,0,3,3,3,2,5,2,2,2,3,0,3,3,3,3,0,3,3,3,3,0,3,3,0]

print(f"first 3 cards: {cards[:3]}\n\nthere were {len(cards)} cards total")
print(f"Testing win function on test card {testcard}: {win(testcard)}")

play_bingo(draws,cards)
