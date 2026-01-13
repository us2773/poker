from app import main_app
from flask import render_template, request
from .modules import gameViewModel

@main_app.route("/", methods=["GET", "POST"])
def main() :
    vm = gameViewModel.GameViewModel()
    if request.method == "POST":
        action = request.form.get("action")

        if action == "show":
            vm.reveal_deals()

        elif action == "exchange":
            choice = request.form.getlist("choice")
            vm.exchange_deals(choice)
    
    return render_template(
        "main.html",
        message=vm.global_message(),
        hand_items=vm.post_deals()
)