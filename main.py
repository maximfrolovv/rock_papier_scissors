"""
Maxim Frolov
405
le code si dessous fais un jeu de roche papier ciseaux avec un ordinateur animer
"""

import arcade
import random

from attack_animation import AttackAnimation, AttackType

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

        self.scissors_sprite = AttackAnimation(AttackType.SCISSORS, scale=0.5)
        self.scissors_sprite.position = (1000, 240)
        self.players_list.append(self.scissors_sprite)

        self.rock_sprite = AttackAnimation(AttackType.ROCK, scale=0.5)
        self.rock_sprite.position = (920, 240)
        self.players_list.append(self.rock_sprite)

        self.paper_sprite = AttackAnimation(AttackType.PAPER, scale=0.5)
        self.paper_sprite.position = (1100, 240)
        self.players_list.append(self.paper_sprite)

        self.comp_rock = AttackAnimation(AttackType.ROCK, scale=0.5)
        self.comp_rock.position = (300, -200)
        self.players_list.append(self.comp_rock)

        self.comp_paper = AttackAnimation(AttackType.PAPER, scale=0.5)
        self.comp_paper.position = (300, -200)
        self.players_list.append(self.comp_paper)

        self.comp_scissors = AttackAnimation(AttackType.SCISSORS, scale=0.5)
        self.comp_scissors.position = (300, -200)
        self.players_list.append(self.comp_scissors)

        self.player_choice = None
        self.computer_choice = None

        self.player_score = 0
        self.computer_score = 0

        self.result_text = ""

        self.game_over = False

        self.background_color = arcade.color.BLACK

        self.hide_timer = 0

    def hide_player_options_temp(self):
        if self.player_choice == "rock":
            self.paper_sprite.position = (2000, -200)
            self.scissors_sprite.position = (2000, -200)
        elif self.player_choice == "paper":
            self.rock_sprite.position = (2000, -200)
            self.scissors_sprite.position = (2000, -200)
        elif self.player_choice == "scissors":
            self.rock_sprite.position = (2000, -200)
            self.paper_sprite.position = (2000, -200)

        self.hide_timer = 0.7

    def show_computer_choice(self):
        self.comp_rock.position = (300, -200)
        self.comp_paper.position = (300, -200)
        self.comp_scissors.position = (300, -200)

        if self.computer_choice == "rock":
            self.comp_rock.position = (300, 240)
        elif self.computer_choice == "paper":
            self.comp_paper.position = (300, 240)
        elif self.computer_choice == "scissors":
            self.comp_scissors.position = (300, 240)

    def reset_game(self):
        self.player_score = 0
        self.computer_score = 0
        self.player_choice = None
        self.computer_choice = None
        self.result_text = ""
        self.game_over = False

        self.comp_rock.position = (300, -200)
        self.comp_paper.position = (300, -200)
        self.comp_scissors.position = (300, -200)

        self.rock_sprite.position = (920, 240)
        self.paper_sprite.position = (1100, 240)
        self.scissors_sprite.position = (1000, 240)

    def draw_rectangle(self):
        arcade.draw_lrbt_rectangle_outline(260, 340, 200, 275, arcade.color.PINK)
        arcade.draw_lrbt_rectangle_outline(965, 1040, 200, 275, arcade.color.PINK)
        arcade.draw_lrbt_rectangle_outline(1060, 1130, 200, 275, arcade.color.PINK)
        arcade.draw_lrbt_rectangle_outline(885, 950, 200, 275, arcade.color.PINK)

    def on_mouse_press(self, x, y, button, modifiers):

        if self.game_over:
            return

        if self.rock_sprite.collides_with_point((x, y)):
            self.player_choice = "rock"
            self.hide_player_options_temp()
        elif self.paper_sprite.collides_with_point((x, y)):
            self.player_choice = "paper"
            self.hide_player_options_temp()
        elif self.scissors_sprite.collides_with_point((x, y)):
            self.player_choice = "scissors"
            self.hide_player_options_temp()
        else:
            return

        self.computer_choice = random.choice(["rock", "paper", "scissors"])
        self.show_computer_choice()

        self.determine_winner()

    def determine_winner(self):
        player = self.player_choice
        computer = self.computer_choice

        if player == computer:
            self.result_text = "Égalité"
            return

        if player == "rock" and computer == "scissors":
            self.result_text = "Le joueur gagne"
            self.player_score += 1
        elif player == "paper" and computer == "rock":
            self.result_text = "Le joueur gagne"
            self.player_score += 1
        elif player == "scissors" and computer == "paper":
            self.result_text = "Le joueur gagne"
            self.player_score += 1
        else:
            self.result_text = "L'ordinateur gagne"
            self.computer_score += 1

        if self.player_score == 3 or self.computer_score == 3:
            self.game_over = True

    def on_key_press(self, key, modifiers):
        if key == arcade.key.SPACE and self.game_over:
            self.reset_game()

    def on_draw(self):
        self.clear()
        self.draw_rectangle()
        self.players_list.draw()

        arcade.draw_text("Roche, Papier, Ciseaux", 350, 640, arcade.color.WHITE, 50)
        arcade.draw_text("Appuyez sur une image pour faire une attaque", 280, 550, arcade.color.WHITE, 30)

        arcade.draw_text(f"Pointage de l'ordinateur : {self.computer_score}", 150, 50, arcade.color.WHITE, 18)
        arcade.draw_text(f"Pointage du joueur : {self.player_score}", 850, 50, arcade.color.WHITE, 18)

        if self.player_choice == "rock":
            arcade.draw_text("Joueur: Roche", 850, 350, arcade.color.YELLOW, 22)
        elif self.player_choice == "paper":
            arcade.draw_text("Joueur: Papier", 850, 350, arcade.color.YELLOW, 22)
        elif self.player_choice == "scissors":
            arcade.draw_text("Joueur: Ciseaux", 850, 350, arcade.color.YELLOW, 22)

        if self.computer_choice == "rock":
            arcade.draw_text("Ordinateur: Roche", 150, 350, arcade.color.YELLOW, 22)
        elif self.computer_choice == "paper":
            arcade.draw_text("Ordinateur: Papier", 150, 350, arcade.color.YELLOW, 22)
        elif self.computer_choice == "scissors":
            arcade.draw_text("Ordinateur: Ciseaux", 150, 350, arcade.color.YELLOW, 22)

        arcade.draw_text(self.result_text, 450, 450, arcade.color.PINK, 30)

        if self.game_over:
            winner = "Le joueur" if self.player_score == 3 else "L'ordinateur"
            arcade.draw_text(f"{winner} a gagné la partie", 400, 300, arcade.color.RED, 30)
            arcade.draw_text("Appuyez sur espace pour recommencer", 350, 250, arcade.color.WHITE, 22)

    def on_update(self, delta_time):
        if self.hide_timer > 0:
            self.hide_timer -= delta_time
            if self.hide_timer <= 0:
                self.rock_sprite.position = (920, 240)
                self.paper_sprite.position = (1100, 240)
                self.scissors_sprite.position = (1000, 240)

        self.rock_sprite.on_update()
        self.paper_sprite.on_update()
        self.scissors_sprite.on_update()

        self.comp_rock.on_update()
        self.comp_paper.on_update()
        self.comp_scissors.on_update()


def main():
    window = arcade.Window(WINDOW_WIDTH, SCREEN_HEIGHT, WINDOW_TITLE)
    game = GameView()
    window.show_view(game)
    arcade.run()


if __name__ == "__main__":
    main()
