from . import GameClass

class GameViewModel:
    def __init__(self):
        self.game = GameClass.Game(1)
        self.player = 0
        self.show_hand = False  # 表示 / 非表示
        
    def global_message(self) -> str :
        return self.game.get_global_message()
    
    def post_deals(self) -> list :
        items = []
        for i in range(5) :
            deals = self.game.get_deals(self.player)
            items.append({
                "key": chr(ord("A")+i),
                "text": deals[i] if self.show_hand else "???",
                "visible": self.show_hand 
            })
        return items
        
    def reveal_deals(self) :
        self.show_hand = True
        
    def exchange_deals(self, change_list) :
        change_list_bool = [False] * 5
        for i in range(5):
            if chr(ord("A")+i) in change_list :
                change_list_bool[i] = True
                
        