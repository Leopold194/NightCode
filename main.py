from random import randint, choice
import pyxel

class Main_Char:

    def __init__(self, x, y):
        self.player_X = x
        self.player_Y = y
        self.life = 100

    def draw(self):
        coef = pyxel.frame_count // 6 % 3
        pyxel.blt(self.player_X, self.player_Y, 0, 16*coef, 0, 16, 16, 11)
    
    def move(self):
        if pyxel.btn(pyxel.KEY_LEFT) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_LEFT):
            self.player_X = max(self.player_X - 2, 0)
        if pyxel.btn(pyxel.KEY_RIGHT) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_RIGHT):
            self.player_X = min(self.player_X + 2, pyxel.width - 16)

        if pyxel.btn(pyxel.KEY_UP) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_UP):
            self.player_Y = max(self.player_Y - 2, 0)
        if pyxel.btn(pyxel.KEY_DOWN) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_DOWN):
            self.player_Y = min(self.player_Y + 2, pyxel.width - 16)

class Monster:

    def __init__(self, x, y):
        self.monster_X = x
        self.monster_Y = y
        
        #self.gender = choice([16, 24, 32, 40])
        self.gender = choice([16, 24])

    def draw(self):
        coef = pyxel.frame_count // 4 % 2
        pyxel.blt(self.monster_X, self.monster_Y, 0, 8*coef, self.gender, 8, 8, 9) 

class Game:

    def __init__(self):
        pyxel.init(128, 128, title="Test mario game")
        pyxel.load("ressources.pyxres")
        
        self.char = Main_Char(56, 110)
        self.monsters_list = []

        pyxel.run(self.update, self.draw)

    def create_monster(self):
        self.monsters_list.append(Monster(randint(0, 112), randint(20, 75)))

    def new_dungeon_monsters(self, nb):
        for _ in range(nb):
            self.create_monster()
    
    def new_dungeon(self, nb, coo_x, coo_y):
        """pyxel.blt(0, 0, nb, coo_x, coo_y, 128, 128)
        pyxel.blt(108, 0, 0, 0, 48, 32, 8, "COULEUR TRANSPARENTE POUR LA PORTE")"""
        self.new_dungeon_monsters(5)
        

    def update(self):
        self.char.move()

    def draw(self):
        pyxel.cls(0)

        if self.char.life > 0:
            
            pyxel.text(5, 5, f"{self.char.life} HP", 7)
            self.char.draw()

            if len(self.monsters_list) == 0:
                self.new_dungeon(0, 0, 52)

            if len(self.monsters_list) != 0:
                for monster in self.monsters_list:
                    monster.draw()


Game()
