import arcade
import random
#from attack_animation import Attack_animation

WINDOW_WIDTH = 1280
SCREEN_HEIGHT = 720
WINDOW_TITLE = "farm"



class GameView(arcade.View):

    def __init__(self):
        super().__init__()

        self.players_list = arcade.SpriteList()

        self.computer_sprite = arcade.Sprite("assets/compy.png", scale=1.8)
        self.computer_sprite.position = (300, 135.24)
        self.players_list.append(self.computer_sprite)

        self.player_sprite = arcade.Sprite("assets/faceBeard.png", scale=0.351)
        self.player_sprite.position = (1000, 135.24)
        self.players_list.append(self.player_sprite)

        self.scissors_sprite = arcade.Sprite("assets/scissors.png", scale=0.5)
        self.scissors_sprite.position = (1000, 240)
        self.players_list.append(self.scissors_sprite)

        self.rock_sprite = arcade.Sprite("assets/srock.png", scale=0.5)
        self.rock_sprite.position = (920, 240)
        self.players_list.append(self.rock_sprite)

        self.paper_sprite = arcade.Sprite("assets/spaper.png", scale=0.5)
        self.paper_sprite.position = (1100, 240)
        self.players_list.append(self.paper_sprite)

        self.player_choice = None
        self.computer_choice = None

        self.player_score = 0
        self.computer_score = 0

        self.result_text = ""

        self.background_color = arcade.color.BLACK

    def draw_rectangle(self):
        arcade.draw_lrbt_rectangle_outline(260, 340, 200, 275, arcade.color.PINK)
        arcade.draw_lrbt_rectangle_outline(965, 1040, 200, 275, arcade.color.PINK)
        arcade.draw_lrbt_rectangle_outline(1060, 1130, 200, 275, arcade.color.PINK)
        arcade.draw_lrbt_rectangle_outline(885, 950, 200, 275, arcade.color.PINK)

    def on_mouse_press(self, x, y, button, modifiers):

        if self.rock_sprite.collides_with_point((x, y)):
            self.player_choice = "rock"
        elif self.paper_sprite.collides_with_point((x, y)):
            self.player_choice = "paper"
        elif self.scissors_sprite.collides_with_point((x, y)):
            self.player_choice = "scissors"
        else:
            return

        self.computer_choice = random.choice(["rock", "paper", "scissors"])

        self.determine_winner()

    def determine_winner(self):
        player = self.player_choice
        computer = self.computer_choice

        if player == computer:
            self.result_text = "Égalité!"
            return

        if player == "rock" and computer == "scissors":
            self.result_text = "Le joueur gagne la ronde!"
            self.player_score += 1
        elif player == "paper" and computer == "rock":
            self.result_text = "Le joueur gagne la ronde!"
            self.player_score += 1
        elif player == "scissors" and computer == "paper":
            self.result_text = "Le joueur gagne la ronde!"
            self.player_score += 1
        else:
            self.result_text = "L'ordinateur gagne la ronde!"
            self.computer_score += 1

    def on_draw(self):
        self.clear()
        self.draw_rectangle()
        self.players_list.draw()

        arcade.draw_text("Rock, Paper, Scissors", 350, 640, arcade.color.WHITE, 50)
        arcade.draw_text("Appuyer sur une image pour faire une attaque", 280, 550, arcade.color.WHITE, 30)

        arcade.draw_text(f"Pointage ordinateur : {self.computer_score}", 150, 50, arcade.color.WHITE, 18)
        arcade.draw_text(f"Pointage joueur : {self.player_score}", 850, 50, arcade.color.WHITE, 18)

        if self.player_choice:
            arcade.draw_text(f"Joueur: {self.player_choice}", 850, 350, arcade.color.YELLOW, 22)
        if self.computer_choice:
            arcade.draw_text(f"Ordinateur: {self.computer_choice}", 150, 350, arcade.color.YELLOW, 22)

        arcade.draw_text(self.result_text, 450, 450, arcade.color.PINK, 30)


def main():
    window = arcade.Window(WINDOW_WIDTH, SCREEN_HEIGHT, WINDOW_TITLE)
    game = GameView()
    window.show_view(game)
    arcade.run()


if __name__ == "__main__":
    main()
