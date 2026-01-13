class Trump():
    def __init__(self, Num, Suit):
        self._Num = Num
        self._Suit = Suit
    
    @property
    def Num(self):
        return self._Num
    
    @property
    def Suit(self):
        return self._Suit
    
    def __str__(self):
        
        if self._Suit == "Spade" :
            suit = "♠"
        elif self._Suit == "Clab" :
            suit = "♣"
        elif self._Suit == "Diamond" :
            suit = "♦"
        elif self._Suit == "Heart" :
            suit = "♥"
        else :
            suit = ""
        
        if self._Num == 14 :
            return f'{suit}-A'
        elif self._Num == 13 :
            return f'{suit}-King'
        elif self._Num == 12 :
            return f'{suit}-Queen'
        elif self._Num == 11 :
            return f'{suit}-Jack'
        else :
            return f'{suit}-{self._Num}'