from random import shuffle

class Deck( object ):
    def __init__( self ):
        self.deck = []
        suits = [ "Spades", "Clubs", "Hearts", "Diamonds" ]
        values = [ "Two", "Three", "Four", "Five", "Six", "Seven", "Eight",
                   "Nine", "Ten", "Jack", "Queen", "King", "Ace" ]

        suitCount = 0

        while( suitCount < 4 ):
            valueCount = 0
            suit = suits[ suitCount ]
            while( valueCount < 13 ):
                value = values[ valueCount ]
                self.deck.append( Card( suit, value ) )
                valueCount += 1
            suitCount += 1

    def printDeck( self ):
        for card in self.deck:
            card.printCard()

    def shuffle( self ):
        shuffle( self.deck )

class Card( object ):
    def __init__( self, suit, value ):
        self.suit = suit
        self.value = value

    def printCard( self ):
        print( "%s of %s" % ( self.value, self.suit ) )


#==========================================================================
deck = Deck()
#deck.shuffle()
deck.printDeck()
print( len( deck.deck ) )

