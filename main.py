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
        if (pyxel.btn(pyxel.KEY_LEFT) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_LEFT)) and self.player_X > 17:
            self.player_X -= 1
        if (pyxel.btn(pyxel.KEY_RIGHT) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_RIGHT)) and self.player_X < 95:
            self.player_X += 1

        if (pyxel.btn(pyxel.KEY_UP) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_UP)) and self.player_Y > 17:
            self.player_Y -= 1
        if (pyxel.btn(pyxel.KEY_DOWN) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_DOWN)) and self.player_Y < 112:
            self.player_Y += 1

class Monster:

    def __init__(self, x, y):
        self.monster_X = x
        self.monster_Y = y
        
        self.gender = choice([16, 24, 32, 40])

    def draw(self):
        coef = pyxel.frame_count // 4 % 2
        pyxel.blt(self.monster_X, self.monster_Y, 0, 8*coef, self.gender, 8, 8, 9) 

class Game:

    def __init__(self):
        pyxel.init(128, 128, title="Test mario game")
        pyxel.load("ressources.pyxres")

        self.start = True
        
        self.char = Main_Char(56, 110)
        self.monsters_list = []

        pyxel.run(self.update, self.draw)

    def create_monster(self):
        self.monsters_list.append(Monster(randint(20, 108), randint(20, 100)))

    def new_dungeon_monsters(self, nb):
        for _ in range(nb):
            self.create_monster()
    
    def new_dungeon(self, nb, coo_x, coo_y):
        self.new_dungeon_monsters(5)
        return randint(0, 1)
    
    def draw_dungeon(self, wall):
        for i in range(8):
            pyxel.blt(16*i, 0, 0, 16*wall, 80, 16, 16)

        for j in range(2):
            for i in range(8):
                pyxel.blt(112*j, 16*i, 0, 16*wall, 80, 16, 16)

    def update(self):
        self.char.move()

    def draw(self):
        pyxel.cls(0)

        if self.start:
            self.wall = self.new_dungeon(0, 0, 52)
            self.start = False

        if self.char.life > 0:

            pyxel.text(5, 5, f"{self.char.life} HP", 7)

            if len(self.monsters_list) == 0:
                pyxel.blt(48, 0, 0, 0, 64, 32, 16)
                if self.char.player_X >= 48 and self.char.player_X <= 80 and self.char.player_Y <= 16:
                    self.wall = self.new_dungeon(0, 0, 52)
                    self.char.player_X, self.char.player_Y = 56, 110

            self.draw_dungeon(self.wall)

            if len(self.monsters_list) != 0:
                pyxel.blt(48, 0, 0, 0, 48, 32, 16)
                for monster in self.monsters_list:
                    monster.draw()

            self.char.draw()


Game()
