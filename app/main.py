from app import main_app
from flask import render_template, request
from .modules import gameViewModel, GameClass

vm = gameViewModel.GameViewModel(GameClass.Game(2))

@main_app.route("/", methods=["GET", "POST"])
def main() :
    print(f"main.py show_hand: {vm.show_hand}")
    if request.method == "POST":
        action = request.form.get("action")

        if action == "show":
            print("action==show")
            # 表示ボタンを押した際の処理
            vm.reveal_deals()

        elif action == "exchange":
            # 交換ボタンを押した際の処理
            choice = request.form.getlist("choice")
            vm.exchange_deals(choice)
            
        elif action == "change_player" :
            vm.change_player()
        
    
    print(f"main.py show_hand: {vm.show_hand}")
    return render_template(
        "main.html",
        message=vm.global_message(),
        hand_items=vm.post_deals(),
        button_message=vm.button_message()
    )
    