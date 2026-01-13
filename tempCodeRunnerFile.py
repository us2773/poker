#役の判定


import random 
import Trump

class Game() :
    def __init__(self, num_of_players):
        self._stock: list = self.create_stock() #山札
        self._cards: list = self.create_cards() #Trump型を数字順に格納したリスト
        self._deals: list = [self.get_deals()] * 5
        self.scores: list = [0] * num_of_players
        self.isCP_list: list = [False] * num_of_players
        self._roles: list = [""] * num_of_players
        self._points : list = [0] * num_of_players
        self._turn: int = 0
        
    def create_stock(self) :
        Dist_lst = []
        while len(Dist_lst) <= 51:
            a = random.randint(0,51)
            if not a in Dist_lst:
                Dist_lst.append(a)
        return Dist_lst

        #print(Dist_lst)

    def create_cards(self) :
        lst = [i for i in range(0,52)]
        # print(Dist_lst)
        num = 2
        for k in range(0,49,4):
            while num <= 14:
                lst[k] = Trump.Trump(num,'Spade')
                lst[k + 1] = Trump.Trump(num,'Clab')
                lst[k + 2] = Trump.Trump(num,'Diamond')
                lst[k + 3] = Trump.Trump(num,'Heart')
                num += 1
                break
            #lstの0はスペードの2,1はクラブの2,2はダイヤの2,3はハートの2,4はスペードの3・・・
        self._card = lst

    def remove_from_stock(self, num: int) :
        self._stock = self._stock[num:]
    
    def draw_cards(self, num: int) :
        new_cards = self._stock[0:num]
        self.remove_from_stock(num)
        return new_cards
        
    def change_deals(self, player_num: int, isChange_list: list) :
        deals = self._deals[player_num]
        for j in range(5) :
            if isChange_list[j] :
                deals[j] = self.draw_cards(1)[0]
                self.remove_from_stock(1)
                    
    def get_deals(self) -> list :
        new_cards = self.draw_cards(5)
        return new_cards
    
    def add_score(self, player_num: list, points: list) :
        self.scores[player_num] += points
        
    def ask_card_Change(self, player_num: int) -> list:
        Change_list = [] 
        card = 0
        while card < 5:
            card_index = self._deals[player_num][card]
            Choise = input(f'{card+ 1}: {self._card[card_index]}を残しますか？（y/n）：')
            
            if Choise == 'n':
                Change_list.append(True)
                card += 1
            elif Choise == 'y':
                Change_list.append(False)
                card += 1
            else:
                continue
        return Change_list

    def get_role(self, deals: list) -> str:
        deals_card = [self._card[i] for i in deals]
        #連番の判定
        Number_Check = []
        for i in range(5):
            Number_Check.append(deals_card[i].Num)
        Number_Check.sort()
        m = 0
        while m < 4:
            if Number_Check[m] + 1 == Number_Check[m + 1]:
                m += 1
            else:
                break
                
        #マークの判定
        Suit_Check = set()
        for i in range(5):
            Suit_Check.add(deals_card[i].Suit)

        #数字の重複の判定
        OverLap = 0
        for i in range(5):
            j = 0
            while j < 5:
                if i == j:
                    j += 1
                elif deals_card[i].Num == deals_card[j].Num:
                    OverLap += 1
                    break
                else:
                    j += 1

        #数字の種類数の判定
        OverLap_set = set()
        for i in range(5):
            OverLap_set.add(deals_card[i].Num)

        if m == 4:
            if len(Suit_Check) == 1:
                if deals_card[0] == 10:
                    return 'ロイヤルストレートフラッシュ'
                else:
                    return'ストレートフラッシュ'
            else:
                return'ストレート'
        
        else:
            if OverLap == 4:
                if len(OverLap_set) == 2:
                    return'フォーカード'
                elif len(OverLap_set) == 3:
                    return'ツーペア'
                else:
                    return'ノーハンド'
            elif OverLap == 0:
                if len(Suit_Check) == 1:
                    return 'フラッシュ'
                else:
                    return 'ノーハンド'
            elif OverLap == 5:
                return 'フルハウス'
            elif OverLap == 3:
                return 'スリーカード'
            elif OverLap == 2:
                return 'ワンペア'
            else:
                return 'ノーハンド'
            
    def get_point(self, roles: list) -> list :
        print(roles)
        point = []
        all_roles = {'ロイヤルストレートフラッシュ':324870, 'ストレートフラッシュ':36097, 'フォーカード':2083, 'フルハウス':347, 'フラッシュ':255, 'ストレート':128, 'スリーカード':24, 'ツーペア':11, 'ワンペア':2, 'ノーハンド':0, }
        for role in roles:
            print(all_roles[role])
            point.append(all_roles[role])
        return point

    def show_deals(self, player_num) :
        print("あなたの手札は")
        deals = self._deals[player_num]
        for i in range(5) :
            print(f"{i+1}:{self._card[deals[i]]} ")
        print("です。")

    def get_winner(self) -> list :
        winner_lst = [i for i, x in enumerate(self._points) if x == max(self._points)]
        return winner_lst
    
    def show_scores(self) :
        print("Score")    
        for i in range(len(self.scores)) :
            print(f'Player{i}: {self.scores[i]}')
    
    def new_game(self) :
        self._stock = self.create_stock #山札
        self._cards = self.create_cards #Trump型を数字順に格納したリスト
        self._deals = [self.get_deals] * 5
        self._roles = [""] * 5
        self._points  = [0] * 5
        self._turn += 1
        
def game() :
    player_num = 0
    isCP = False
    isContinue = True
    while player_num == 0 :
        input_num = int(input("Playerの人数を選択: "))
        if (input_num == 1) :
            player_num = 2
            isCP = True
            print("CP対戦モード")
        if (2 <= input_num <= 4) :
            player_num = input_num
            break
        else :
            continue
    GameObject  = Game(player_num)

    while isContinue :
        print(f"第{GameObject._turn}ラウンド")
        
        GameObject.create_cards()
        GameObject.create_stock()
        
            
        #手札の配布

        for i in range(player_num) :
            input()
            if (isCP and i == 1) :
                print("CPのターン")
                player_Change_List = [False] * 5
                
            else :
                GameObject.show_deals(i)
                player_Change_List = GameObject.ask_card_Change(i)
            
            GameObject.change_deals(i, player_Change_List)

            GameObject.show_deals(i)
            
        #勝敗
        for i in range(player_num) :
            GameObject.show_deals(i)
            print(GameObject._deals[i])
            GameObject._roles[i] = GameObject.get_role(GameObject._deals[i])
            print(GameObject._roles)
            GameObject._points[i] = GameObject.get_point(GameObject._roles[i])
        
        winners = GameObject.get_winner()
        if len(winners) == player_num :
            print("引き分け")
        else :
            print(f"勝者は Player{winners}")
        
        for winner in winners :
            GameObject.add_score(winner, GameObject._points[winner])

        GameObject.show_scores()
            
        while True :
            Choise = input("ゲームを続行しますか？(y/n) :")
            if Choise == 'n':
                Choise_last = input("本当によろしいですか？(y/n) :")
                if Choise_last == "y" :
                    isContinue = False
                    print("最終スコア")    
                    GameObject.show_scores()
                    break
                else :
                    continue
            elif Choise == "y" or Choise == "" :
                break
            else:
                continue
        
if __name__ == "__main__" :
    game()