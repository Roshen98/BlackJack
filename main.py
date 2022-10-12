import random
# global list
cardType = ['Heart','Club','Diamond','Spade']
cardNumber = ['Ace','Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten',
'Jack','Queen','King']
spacing = '*'*20

yourCardType = []
dealerCardType = []
yourCardNumber = []
dealerCardNumber = []

# def rules():
        
def placeBet(money):
    # returns the valid amount the player wants to bet
    while True:
        try:
            bet = int(input("What's your bet: "))
            if bet > 0 and bet <= money:
                return bet
            else:
                print('The bet is invalid')
        except ValueError:
            print('The bet you entered is not a valid amount')
    
def randomCard():
    # returns a random card type and a random card number
    return random.choice(cardType), random.choice(cardNumber)
    
def gamePlay(money):
    # returns the money after a single game has been completed
    if money == 0:
        print('You are bankrupt, RIP!')
        return money
    else:
        betMoney = placeBet(money)
        money -= betMoney
        randomType1, randomNumber1 = randomCard()
        randomType2, randomNumber2 = randomCard()
        computerType1, computerNumber1 = randomCard()
        computerType2, computerNumber2 = randomCard()
        
        yourCardType.clear()
        yourCardNumber.clear()
        dealerCardType.clear()
        dealerCardNumber.clear()
        
        yourCardType.append(randomType1)
        yourCardType.append(randomType2)
        yourCardNumber.append(randomNumber1)
        yourCardNumber.append(randomNumber2)
        
        dealerCardType.append(computerType1)
        dealerCardType.append(computerType2)
        dealerCardNumber.append(computerNumber1)
        dealerCardNumber.append(computerNumber2)
        
        print(spacing)
        printYourList()
        print(spacing)
        print('Dealer Card:')
        print(computerType1, computerNumber1)
        print('the second card for the dealer is hidden')
        print(spacing)
        # the second card for the dealer is hidden
        yourCardTotal = calculateCard(randomNumber1, randomNumber2)
        dealerCardTotal = calculateCard(computerNumber1,computerNumber2)
    
        userChoice = ''
        dealerChoice = ''
        while userChoice != 'Stand':
            userChoice = choice(betMoney,money)
            if userChoice == 'Hit':
                randomType, randomNumber = randomCard()
                yourCardType.append(randomType)
                yourCardNumber.append(randomNumber)
                print('Your new card:', randomType, randomNumber)
                yourCardTotal = calculateCard(yourCardTotal, randomNumber)
                if yourCardTotal > 21:
                    printYourList()
                    printDealerList()
                    print('\nYou Bursted! Dealer wins!')
                    return money
                printYourList()
            else:
                printYourList()
            
            if yourCardTotal == 21:
                print('\nBLACK JACK!')
                break
            
        while dealerChoice != 'Stand':
            dealerChoice = computerChoice(dealerCardTotal)
            if dealerChoice == 'Hit':
                randomType, randomNumber = randomCard()
                dealerCardType.append(randomType)
                dealerCardNumber.append(randomNumber)
                dealerCardTotal = calculateCard(dealerCardTotal, randomNumber)
                print('Dealer new card:', randomType, randomNumber)
                if dealerCardTotal > 21:
                    printDealerList()
                    print('\nThe Dealer Bursted! You Win!')
                    return money
                printDealerList()
            else:
                printDealerList()
            
            if dealerCardTotal == 21:
                print('BLACK JACK!')
                break
               
        condition = winCondition(dealerCardTotal,yourCardTotal)
        if condition == '\nYou Win!':
            money += 2*betMoney
            print(condition)
        elif condition == '\nDealer Wins!':
            print(condition)
        else:
            money += betMoney
            print(condition)
        return money

def printYourList():
    # show the player's cards
    print(spacing)
    print('Your Cards:')
    for x, y in zip(yourCardType, yourCardNumber):
        print(x, y)
    
def printDealerList():
    # show the dealer's cards
    print(spacing)
    print('Dealer Cards:')
    for x, y in zip(dealerCardType, dealerCardNumber):
        print(x, y)
    
    
def winCondition(dealerCardTotal,yourCardTotal):
    # returns the result of the game
    if (dealerCardTotal > 21 and yourCardTotal > 21) or dealerCardTotal == yourCardTotal:
        return '\nIt is a draw! No one wins!'
        
    if dealerCardTotal > 21 or dealerCardTotal < yourCardTotal:
        return '\nYou Win!'

    if yourCardTotal > 21 or dealerCardTotal > yourCardTotal:
        return '\nDealer Wins!'
    
        
def computerChoice(dealerCardTotal):
    # returns stand if the total sum of the dealer's cards are more than 
    # or equal to 17, otherwise return hit
    if dealerCardTotal >= 17:
        return 'Stand'
    else:
        return 'Hit'
        
def doubleOrNot():
    # returns true if the player wants to double, otherwise returns false
    while True:
        choices = input('Do you want to Double?[Yes/No]')
        if choices == 'Yes' :
            return True
        if choices == 'No':
            return False
            
                
def choice(betMoney,money):
    # returns the player's choice on hit or stand
    while True:
        choices = input('Do you want to Hit, Stand?[Hit/Stand]')
        if choices == 'Hit' or choices == 'Stand':
            return choices
        

def calculateCard(number1, number2):
    # returns the sum of the cards
    firstNumber = 0
    secondNumber = 0
    for x in range(1,10):
        if number1 == cardNumber[x]:
            firstNumber = x + 1
        if number2 == cardNumber[x]:
            secondNumber = x + 1
    
    if number1 == cardNumber[10] or number1 == cardNumber[11] or \
        number1 == cardNumber[12]:
            firstNumber = 10
    if number2 == cardNumber[10] or number2 == cardNumber[11] or \
    number2 == cardNumber[12]:
            secondNumber = 10
            
    if isinstance(number1, int):
        firstNumber = number1
    
    if isinstance(number2, int):
        secondNumber = number2
        
    if number1 == 'Ace':
        firstNumber = 11
    
    if number2 == 'Ace':
        secondNumber = 11
    
    if firstNumber + secondNumber > 21:
        if number1 == 'Ace':
            firstNumber = 1
        elif number2 == 'Ace':
            secondNumber = 1
        
    return firstNumber + secondNumber
    
def menu():
    # displays the main menu of the game
    print('IT IS BLACK JACK TIME! COME TO BET YOUR MONEY FOR MORE!')
    money = 2000  # $2000 initially
    print('Initial Amount Owned = $' + str(money))
    
    while True:
        money = gamePlay(money)
        if money == 0:
            return 'You are bankrupt, RIP!\nGame Over!'
         
        print('Current Amount: $'+ str(money))
        
        play = playAgain()
        if play == 'y':
            continue
        elif play == 'n':
            return 'Game Over!'
    
def playAgain():
    # returns if the user want to play or not
    while True:
        play = input('Do you want to play agdealern?[y/n]')
        if play == 'y' or play == 'n':
            return play
        else:
            print('Enter only y or n!')

if __name__ == '__main__':
    print(menu())








