from enum import Enum, auto
class gameState(Enum) :
    INIT = auto()
    DEAL = auto()
    HOLD = auto()
    DRAW = auto()
    END = auto()