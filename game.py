import time
from modules import Game

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
        GameObject.new_game()
            
        #手札の配布

        for i in range(player_num) :
            
            GameObject.output_global_message()
            if (isCP and i == player_num-1) :
                print(f"player{i+1}(CP)のターン")
                print("手札交換中…")
                time.sleep(1)
                print("交換完了")
                
            else :
                print(f"player{i+1}のターン")
                print("あなたの手札は")
                GameObject.wait_until_enter()
                GameObject.show_deals(i)
                print("です")
                
                player_Change_List = GameObject.ask_card_Change(i)
                
                GameObject.change_deals(i, player_Change_List)
                print("あなたの最終的な手札は")
                GameObject.show_deals(i)
                print("です。")
                GameObject.wait_until_enter()
                
                    
            
        #勝敗
        GameObject.wait_until_enter()
        GameObject.output_global_message()
        print("カードオープン")
        GameObject.wait_until_enter()
        for i in range(player_num) :
            print(f"player{i+1}")
            GameObject.show_deals(i)
            GameObject._roles[i] = GameObject.get_role(GameObject._deals[i])
            print(GameObject._roles[i])
            print()
            
        GameObject._points = GameObject.get_point(GameObject._roles)
        GameObject.wait_until_enter()
        
        winners = GameObject.get_winner()
        if len(winners) == player_num :
            print("引き分け")
        else :
            winners_for_showing = [i+1 for i in winners]
            print(f"勝者は Player{winners_for_showing}")
        
        GameObject.update_score()

        GameObject.show_scores()
            
        while True :
            Choise = input("ゲームを続行しますか？(y/n) :")
            if Choise == 'n':
                Choise_last = input("本当によろしいですか？(y/n) :")
                if Choise_last == "y" :
                    isContinue = False
                    print("最終スコア")    
                    GameObject.show_scores()
                    top = GameObject.get_top_score()
                    top_for_showing = [i+1 for i in top]
                    print(f"最もスコアが高かったのは Player{top_for_showing}")    
                    
                    break
                else :
                    continue
            elif Choise == "y" or Choise == "" :
                break
            else:
                continue
        
if __name__ == "__main__" :
    game()