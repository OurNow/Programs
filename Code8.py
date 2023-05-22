import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven',
         'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10,
          'Queen': 10, 'King': 10, 'Ace': 11}
playing = True


class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return (f"{self.rank} of {self.suit}")


class Deck:

    def __init__(self):
        self.deck = []  # start with an empty list
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    def __str__(self):
        deck_comp = ''  # start with an empty string
        for card in self.deck:
            deck_comp += '\n '+card.__str__()  # add each Card object's print string
        return 'The deck has:' + deck_comp

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        return self.deck.pop()


class Hand:
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0   # start with zero value
        self.aces = 0    # add an attribute to keep track of aces

    def add_card(self, card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1

    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1


class Chips:

    def __init__(self, total):
        self.total = total  # This can be set to a default value or supplied by a user input
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet


def take_bet(chips):

    while True:
        try:
            chips.bet = int(input('How many chips would you like to bet?: '))
        except ValueError:
            print('Sorry, a bet must be an integer!')
        else:
            if chips.bet > chips.total:
                print("Sorry, your bet can't exceed ", chips.total)
            else:
                break


def hit(deck, hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()


def hit_or_stand(deck, hand):
    global playing  # to control an upcoming while loop
    while True:
        choice = input("Would you like to Hit or Stand? Enter Hit or Stand: ")
        if choice == "Hit":
            hit(deck, hand)
        elif choice == "Stand":
            print("Player stands. Dealer is playing.")
            playing = False
        else:
            print("Invalid choice! Please choose either Hit or Stand: ")
            continue
        break


def show_some(player, dealer):
    print(" <card hidden>")
    print('', dealer.cards[1])
    print("Player's visible cards:")
    for i in range(0, len(player.cards)):
        print(player.cards[i])


def show_all(player, dealer):
    print("Dealer's cards:")
    for i in range(0, len(dealer.cards)):
        print(dealer.cards[i])
    print(f"Dealer's hand is {dealer.value}")
    print("Player's cards:")
    for i in range(0, len(player.cards)):
        print(player.cards[i])
    print(f"Player's hand is {player.value}")


def player_busts(chips):
    print("Player busts!")
    chips.lose_bet()


def player_wins(chips):
    print("Player wins!")
    chips.win_bet()


def dealer_busts(chips):
    print("Dealer busts!")
    chips.win_bet()


def dealer_wins(chips):
    print("Dealer wins!")
    chips.lose_bet()


def push():
    print("Dealer and Player tie! It's a push.")


print("Welcome to Blackjack!")
x = int(input("What would you like the max total to be?: "))
player_chips = Chips(x)

while True:

    # Create & shuffle the deck, deal two cards to each player
    deck = Deck()
    player = Hand()
    dealer = Hand()
    deck.shuffle()
    for i in range(0, 2):
        player.add_card(deck.deal())
        dealer.add_card(deck.deal())

    # Set up the Player's chips

    # Prompt the Player for their bet
    take_bet(player_chips)

    # Show cards (but keep one dealer card hidden)
    show_some(player, dealer)

    while playing:  # recall this variable from our hit_or_stand function

        # Prompt for Player to Hit or Stand
        hit_or_stand(deck, player)

        # Show cards (but keep one dealer card hidden)
        show_some(player, dealer)

        # If player's hand exceeds 21, run player_busts() and break out of loop
        if player.value > 21:
            player_busts(player_chips)
            break

    # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
        while dealer.value < 17:
            hit(deck, dealer)

        # Show all cards
        show_all(player, dealer)
        # Run different winning scenarios
        if dealer.value > 21:
            dealer_busts(player_chips)
        elif dealer.value > player.value:
            dealer_wins(player_chips)
        elif dealer.value < player.value:
            player_wins(player_chips)
        else:
            push(player, dealer)

    # Inform Player of their chips total
        print("Player's total winnings is ", player_chips.total)
    # Ask to play again
        new_game = input(
            "Would you like to play another hand? Enter Yes or No: ")

        if new_game == "Yes":
            playing = True
            continue
        else:
            print("Thanks for playing!")
            break
    break
