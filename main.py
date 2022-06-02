
import pyxel


class App:


    def __init__(self):
        pyxel.init(128, 128, title="Test mario game")

        pyxel.load("ressources.pyxres")
        self.player_X = 0
        self.player_Y = 0

        pyxel.run(self.update, self.draw)



    def update(self):
        # update du joueur (deplacement)
        self.update_player()



    def draw(self):

        #effacer la fenetre
        pyxel.cls(0)

        # dessiner le fond
        pyxel.blt(0, 0, 0, 0, 56, 56, 112) # (x sur l'app, y sur l'app, img, x sur le tile, y sur le tile, w sur le tile, h sur le tile)

        # dessiner joueur (mario)
        pyxel.blt(self.player_X,self.player_Y,0,0,0,16,16,1) # ola derniere couleur est la couleur qui sera transparente 
        
        
        


    def update_player(self):

        # DEPLACEMENT du joueur

        if pyxel.btn(pyxel.KEY_LEFT) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_LEFT):
            self.player_X = max(self.player_X - 2, 0)
        if pyxel.btn(pyxel.KEY_RIGHT) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_RIGHT):
            self.player_X = min(self.player_X + 2, pyxel.width - 16)

        if pyxel.btn(pyxel.KEY_UP) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_UP):
            self.player_Y = max(self.player_Y - 2, 0)
        if pyxel.btn(pyxel.KEY_DOWN) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_DOWN):
            self.player_Y = min(self.player_Y + 2, pyxel.width - 16)



App()
