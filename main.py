from random import randint
import pyxel

class Main_Char:

    def __init__(self, x, y):
        self.player_X = x
        self.player_Y = y
        self.life = 100

    def draw(self):
        coef = pyxel.frame_count // 3 % 3
        print(coef)
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

    def draw(self):
        coef = pyxel.frame_count // 3 % 3
        pyxel.blt(self.monster_X, self.monster_Y, 0, 0, 16*coef, 16, 16, 11) 

class Game:

    def __init__(self):
        pyxel.init(128, 128, title="Test mario game")
        pyxel.load("ressources.pyxres")
        
        self.char = Main_Char(56, 42)
        self.monsters_list = []

        pyxel.run(self.update, self.draw)

    def create_monster(self):
        self.monsters_list.append(Monster(randint(0, 112), randint(20, 75)))

    def new_dungeon_monsters(self, nb):
        for _ in range(nb):
            self.create_monster()
    
    def new_dungeon(self, nb, coo_x, coo_y):
        pyxel.blt(0, 0, nb, coo_x, coo_y, 128, 128)
        self.new_dungeon_monsters(5)
        for monster in self.monsters_list:
            monster.draw()

    def update(self):
        self.char.move()

    def draw(self):
        pyxel.cls(0)

        if self.char.life > 0:
            
            pyxel.text(5, 5, f"{self.char.life} HP", 7)
            self.char.draw()

            if len(self.monsters_list) == 0:
                self.new_dungeon(0, 0, 52)


Game()
