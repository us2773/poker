from . import GameClass, GameState

class GameViewModel:
    def __init__(self, GameObject: GameClass.Game):
        self.game = GameObject
        self.player = 0
        self.show_hand = False  # 表示 / 非表示
        
    def global_message(self) -> str :
        return self.game.get_global_message()
    
    def post_deals(self) -> list :
        # 画面更新のたびに呼び出される
        self.game.log()
        items = []
        deals = self.game.get_deals()
        for i in range(5) :
            items.append({
                "key": chr(ord("A")+i),
                "text": deals[i] if self.show_hand else "???",
                "visible": self.show_hand 
            })
            
        return items
        
    def reveal_deals(self) :
        print("call reveal_deals")
        if self.game._state == GameState.gameState.DEAL :
            self.show_hand = True
            self.game.show_deals()
        elif self.game._state == GameState.gameState.END :
            self.game.new_game()
        
    def exchange_deals(self, change_list) :
        print(change_list)
        if self.game._state == GameState.gameState.HOLD :
            change_list_bool = [False] * 5
            for i in range(5):
                if chr(ord("A")+i) in change_list :
                    change_list_bool[i] = True
            print(change_list_bool)
            self.game.change_deals(change_list_bool)
            self.game.change_cards()
            self.post_deals()
            
    def change_player(self) :
        self.show_hand = False
        self.game.change_player()
        
    def button_message(self) :
        if self.game._state == GameState.gameState.DEAL :
            dict = {"show": "表示", "exchange": "--", "player_change": "--"}
        elif self.game._state == GameState.gameState.HOLD :
            dict = {"show": "--", "exchange": "交換", "player_change": "--"}
        elif self.game._state == GameState.gameState.DRAW and self.game._now_playing == self.game._num_of_players-1 :
            dict = {"show": "表示", "exchange": "--", "player_change": "オープン"}
        elif self.game._state == GameState.gameState.DRAW :
            dict = {"show": "--", "exchange": "--", "player_change": "プレイヤー交代"}
        elif self.game._state == GameState.gameState.END :
            dict = {"show": "続行", "exchange": "--", "player_change": "--"}
        
        else :
            dict = {"show": "表示", "exchange": "交換", "player_change": "プレイヤー交代"}
        return dict
            
        