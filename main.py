
import random


class Spacing:

    @staticmethod
    def one_space():
        print()

    @staticmethod
    def two_space():
        print()
        print()

    @staticmethod
    def screen_refresh():
        for _ in range(20):
            print()


class Player:

    def __init__(self, bank, luck, bet):
        self.bank = bank
        self.luck = luck
        self.bet = bet

    def sub_bank(self, amount):
        if self.bank < amount:
            raise ValueError
        self.bank -= amount
        
    def add_bank(self, amount):
        self.bank += amount

    def add_luck(self, amount):
        if self.luck + amount >= 10:
            self.luck = 10
        elif self.luck + amount <= 0:
            self.luck = 0
        else:
            self.luck += amount


def generator(luck):
    slots = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    return random.choices(slots, weights=[-luck, luck, 5, luck, -luck, 5, 5, luck, 5, -luck], k=3) 


def luck_filter(outcome):

    luck_output = 0

    # lucky sums (sievie)

    if sum(outcome) == 1:
        luck_output += 0.1
    
    if sum(outcome) == 3:
        luck_output += 0.3

    if sum(outcome) == 7:
        luck_output += 0.5
    
    if sum(outcome) == 15:
        luck_output += 0.5
    
    if sum(outcome) == 21:
        luck_output += 2
        
    if sum(outcome) == 25:
        luck_output += 2

    # unlucky sums

    #  tetraphobia
    if sum(outcome) == 4:
        luck_output -= 0.1

    # enneaphobia
    if sum(outcome) == 9:
        luck_output -= 0.1

    #  triskaidekaphobia
    if sum(outcome) == 13:
        luck_output -= 0.2

    #  heptadecaphobia
    if sum(outcome) == 17:
        luck_output -= 0.3

    #  hexakosioihexekontahexaphobia
    if outcome[0] == outcome[1] == outcome[2] == 6:
        luck_output = -10

    return luck_output


def teller(outcome, amount):
    
    s1 = outcome[0]
    s2 = outcome[1]
    s3 = outcome[2]


    if s1 == s2 == s3 == 0:
        return amount * 0
    if s1 == s2 == s3 == 1:
        return amount * 25
    if s1 == s2 == s3 == 2:
        return amount * 1
    if s1 == s2 == s3 == 3:
        return amount * 50
    if s1 == s2 == s3 == 4:
        return amount * 0
    if s1 == s2 == s3 == 5:
        return amount * 1
    if s1 == s2 == s3 == 6:
        return amount * 0
    if s1 == s2 == s3 == 7:
        return amount * 100
    if s1 == s2 == s3 == 8:
        return amount * 1 
    if s1 == s2 == s3 == 9:
        return amount * 0

    return 0


if __name__ == '__main__':


    print('Welcome to the Slot Machine Casino')
    print('Get three sevens and win!')

    while True:
        try:
            bet = int(input('Enter your bet value (dollar amount, no cents, greater than zero): '))
            if  bet > 0:
                player = Player(50, 5, bet)
                break
            raise ValueError
        except:
            print('its really important that you input the correct values!')

    game = True
    outcome = [7, 7, 7]

    while game:

        # slot screen
        Spacing.screen_refresh()
        print(f'Player Luck: {player.luck:.2f}                 Player Bank: ${player.bank:,}                Current Bet: ${player.bet:,}')
        Spacing.two_space()
        print('Your numbers:')
        Spacing.one_space()
        print(f' {outcome[0]} {outcome[1]} {outcome[2]}')
        Spacing.two_space()

        # collect bet
        while True:

            try:
                player_input = input('Press enter to spin or type new bet amount: ')
                if player_input != '':
                    player.bet = int(player_input.strip('-'))
                player.sub_bank(player.bet)
                break
            except:
                print('Have to press enter or enter a value greater than or equal to the value of your current bank!')


        # generate numbers
        outcome = generator(player.luck)

        # adjust luck
        player.add_luck(luck_filter(outcome=outcome))

        # teller interaction
        player.add_bank(teller(outcome=outcome, amount=player.bet))

        if player.bank == 0:
            print('You are out of money. Thanks for playing!')
            game = False



    