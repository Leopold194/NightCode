

import pyxel

REGLES = "    Regles du jeu:\n\nLe joueur doit \nsurvivre aux \nmonstres qui \nmenacent le joueur!\n\n       Touche:\n\n-Frapper: espace\n-Se deplacer: fleches"

BUTTON_PLAY_X = 128/2 - 50/2
BUTTON_PLAY_Y = 30
BUTTON_PLAY_H = 20
BUTTON_PLAY_W = 50

BUTTON_QUIT_X = 128/2 - 50/2
BUTTON_QUIT_Y = 75
BUTTON_QUIT_H = 20
BUTTON_QUIT_W = 50

BUTTON_RULES_X = 90
BUTTON_RULES_Y = 110
BUTTON_RULES_H = 15
BUTTON_RULES_W = 35


BUTTON_BACK_X = 3
BUTTON_BACK_Y = 110
BUTTON_BACK_H = 15
BUTTON_BACK_W = 35

class Game:

    def __init__(self):
        pyxel.init(128, 128, title="Test mario game")
        pyxel.load("ressources.pyxres")
        pyxel.mouse(True)

        self.home_state = True
        self.rules_state = False
        self.keys_state = False
        self.play_state = False

        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            if pyxel.mouse_x >= BUTTON_PLAY_X and pyxel.mouse_x <= BUTTON_PLAY_X+BUTTON_PLAY_W and pyxel.mouse_y >= BUTTON_PLAY_Y and pyxel.mouse_y <= BUTTON_PLAY_Y+BUTTON_PLAY_H:
                print("jouer")
                self.home_state = False
                self.play_state = True
                
            if pyxel.mouse_x >= BUTTON_QUIT_X and pyxel.mouse_x <= BUTTON_QUIT_X+BUTTON_QUIT_W and pyxel.mouse_y >= BUTTON_QUIT_Y and pyxel.mouse_y <= BUTTON_QUIT_Y+BUTTON_QUIT_H:
                print("quitter")
                pyxel.quit()
            if pyxel.mouse_x >= BUTTON_RULES_X and pyxel.mouse_x <= BUTTON_RULES_X+BUTTON_RULES_W and pyxel.mouse_y >= BUTTON_RULES_Y and pyxel.mouse_y <= BUTTON_RULES_Y+BUTTON_RULES_H:
                print("regles")
                self.home_state = False
                self.rules_state = True
            if pyxel.mouse_x >= BUTTON_BACK_X and pyxel.mouse_x <= BUTTON_BACK_X+BUTTON_BACK_W and pyxel.mouse_y >= BUTTON_BACK_Y and pyxel.mouse_y <= BUTTON_BACK_Y+BUTTON_BACK_H:
                print("touches")
                self.rules_state = False
                self.home_state = True
                
            


    def draw(self):
        pyxel.cls(0)

        for i in range(8):
            for y in range(8):
                pyxel.blt(i*16, y*16, 0, 0, 80, 16, 16)

        pyxel.text(42, 5, "The Dungeon", 7)

        if self.home_state:
            self.home()
        elif self.rules_state:
            self.rules()
        elif self.play_state:
            self.play()

    
    def home(self):

        pyxel.rect(BUTTON_PLAY_X, BUTTON_PLAY_Y, BUTTON_PLAY_W, BUTTON_PLAY_H, 13) # (x,y,w,h,color)
        pyxel.text(BUTTON_PLAY_X + BUTTON_PLAY_W/2 - 9, BUTTON_PLAY_Y + BUTTON_PLAY_H/2 - 2, "JOUER", 0)

        pyxel.rect(BUTTON_QUIT_X, BUTTON_QUIT_Y, BUTTON_QUIT_W, BUTTON_QUIT_H, 13) # (x,y,w,h,color)
        pyxel.text(BUTTON_QUIT_X + BUTTON_QUIT_W/2 - 13, BUTTON_QUIT_Y + BUTTON_QUIT_H/2 - 2, "QUITTER", 0)

        pyxel.rect(BUTTON_RULES_X, BUTTON_RULES_Y, BUTTON_RULES_W, BUTTON_RULES_H, 13) # (x,y,w,h,color)
        pyxel.text(BUTTON_RULES_X + BUTTON_RULES_W/2 - 11, BUTTON_RULES_Y + BUTTON_RULES_H/2 - 2, "Regles", 0)

       # pyxel.rect(BUTTON_KEYS_X, BUTTON_KEYS_Y, BUTTON_KEYS_W, BUTTON_KEYS_H, 13) # (x,y,w,h,color)
      #  pyxel.text(BUTTON_KEYS_X + BUTTON_KEYS_W/2 - 14, BUTTON_KEYS_Y + BUTTON_KEYS_H/2 - 2, "Touches", 0)

        pyxel.blt(5, 30, 0, 0, 0, 16, 16,11)
        pyxel.blt(100, 30, 0, 112, 0, 16, 16,11)

        pyxel.blt(60, 60, 0, 32, 16, 8, 8,9)
        pyxel.blt(60, 100, 0, 32, 24, 8, 8,9)

        pyxel.blt(100, 80, 0, 32, 32, 8, 8,9)
        pyxel.blt(20, 80, 0, 32, 40, 8, 8,9)

    def rules(self):

        pyxel.rect(20, 20, 90, 80, 13) # (x,y,w,h,color)
        pyxel.text(20+2, 20+2 , REGLES, 0)

        pyxel.rect(BUTTON_BACK_X, BUTTON_BACK_Y, BUTTON_BACK_W, BUTTON_BACK_H, 13) # (x,y,w,h,color)
        pyxel.text(BUTTON_BACK_X + BUTTON_BACK_W/2 - 14, BUTTON_BACK_Y + BUTTON_BACK_H/2 - 2, "Retour", 0)



Game()