import os
import random
import Trump
import time

class Game() :
    def __init__(self, num_of_players):
        self._stock: list = self.create_stock() #山札
        self._cards: list = self.create_cards() #Trump型を数字順に格納したリスト
        self._deals: list = self.create_deals(num_of_players)
        self.scores: list = [0] * num_of_players
        self.isCP_list: list = [False] * num_of_players
        self._roles: list = [""] * num_of_players
        self._points : list = [0] * num_of_players
        self._turn: int = 0
        
    def create_stock(self) :
        # 山札の作成
        # self._stockの初期化に使用
        Dist_lst = []
        while len(Dist_lst) <= 51:
            a = random.randint(0,51)
            if not a in Dist_lst:
                Dist_lst.append(a)
        return Dist_lst

        #print(Dist_lst)

    def create_cards(self) :
        # トランプカードオブジェクトのリストを作成
        # self._cardsの初期化に使用
        # リストの0はスペードの2,1はクラブの2,2はダイヤの2,3はハートの2,4はスペードの3・・・
        
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
        self._card = lst

    def remove_from_stock(self, num: int) :
        # 山札から1枚カードを取り除く処理
        # 先頭要素を取り除いたリストを再代入
        self._stock = self._stock[num:]
    
    def draw_cards(self, num: int) :
        # 任意の枚数だけカードを山札から引く処理
        new_cards = self._stock[0:num]
        
        # 山札の更新
        self.remove_from_stock(num)
        return new_cards

    def create_deals(self, num_of_players) -> list:
        # 全員分の手札の決定
        deals = []
        for i in range(num_of_players) :
            deal = self.draw_cards(5)
            deals.append(deal)
        return deals
    
    def change_deals(self, player_num: int, isChange_list: list) :
        # 手札の交換
        deals = self._deals[player_num]
        for j in range(5) :
            if isChange_list[j] :
                deals[j] = self.draw_cards(1)[0]
                self.remove_from_stock(1)
    
    def add_score(self, player_num: list, points: list) :
        # 任意のユーザのスコアの更新
        self.scores[player_num] += points
    
    def get_role(self, deals: list) -> str:
        # 手札から役を判定する処理
        # 役を示す文字列を返す
        
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
        # 全員の役から全員の点数を求める処理
        point = []
        all_roles = {'ロイヤルストレートフラッシュ':324870, 'ストレートフラッシュ':36097, 'フォーカード':2083, 'フルハウス':347, 'フラッシュ':255, 'ストレート':128, 'スリーカード':24, 'ツーペア':11, 'ワンペア':2, 'ノーハンド':0, }
        for role in roles:
            point.append(all_roles[role])
        return point

    def get_winner(self) -> list :
        # ポイントリストから全ての勝者を判定する処理
        winner_lst = [i for i, x in enumerate(self._points) if x == max(self._points)]
        return winner_lst
    
    def get_top_score(self) -> list :
        # 最も総合スコアの高いプレイヤーを求める処理
        top_score_lst = [i for i, x in enumerate(self.scores) if x == max(self.scores)]
        return top_score_lst
                
    def ask_card_Change(self, player_num: int) -> list:
        # 交換する手札の確認
        # 標準入出力用
        # 交換：True、保持：False
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
    
    def show_deals(self, player_num) :
        # 手札を出力する処理
        # 標準入出力処理用
        deals = self._deals[player_num]
        for i in range(5) :
            print(f"{i+1}:{self._card[deals[i]]} ")
            
    def show_scores(self) :
        # スコアを出力する処理
        # 標準入出力処理用
        print("Score")    
        for i in range(len(self.scores)) :
            print(f'Player{i+1}: {self.scores[i]}')
    
    def new_game(self, num_of_players) :
        # 各プロパティを初期化し、ターン数を+1
        self._stock = self.create_stock() #山札
        self._cards = self.create_cards() #Trump型を数字順に格納したリスト
        self._deals = self.create_deals(num_of_players)
        self._roles = [""] * num_of_players
        self._points  = [0] * num_of_players
        self._turn += 1
        
    def output_global_message(self) :
        # ログの削除と全体メッセージの表示
        # 標準入出力処理用
        os.system("cls" if os.name == "nt" else "clear")
        print(f"第{self._turn}ラウンド")
        for i in range(len(self._deals)) :
            print(f"{i+1}P: {self.scores[i]}point")

    def wait_until_enter(self, msg="↓") :
        #　ユーザがエンターかyを押すまで次の出力を行わせない処理
        # 標準入出力処理用
        isWait = True
        while isWait :
            enter = input(msg)
            if enter == "" or "y" :
                isWait = False
        
