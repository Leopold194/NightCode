from random import randint, choice
import pyxel
import time

class Main_Char:

    def __init__(self, x, y):
        self.player_X = x
        self.player_Y = y
        self.life = 100

    def draw(self, pos):
        coef = pyxel.frame_count // 6 % 3
        pyxel.blt(self.player_X, self.player_Y, 0, pos+16*coef, 0, 16, 16, 11)
    
    def move(self):
        if (pyxel.btn(pyxel.KEY_LEFT) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_LEFT)) and self.player_X > 17:
            self.player_X -= 1
        if (pyxel.btn(pyxel.KEY_RIGHT) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_RIGHT)) and self.player_X < 95:
            self.player_X += 1
        if (pyxel.btn(pyxel.KEY_UP) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_UP)):
            if (self.player_X > 48 or self.player_X < 70) or self.player_Y > 17:
                self.player_Y -= 1
        if (pyxel.btn(pyxel.KEY_DOWN) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_DOWN)) and self.player_Y < 112:
            self.player_Y += 1

class Monster:

    def __init__(self, x, y):
        self.monster_X = x
        self.monster_Y = y
        self.life = choice([30, 60])
        
        #self.gender = choice([16, 24, 32, 40])
        self.gender = choice([16, 32])

    def draw(self):
        coef = pyxel.frame_count // 4 % 2
        pyxel.blt(self.monster_X, self.monster_Y, 0, 16*coef, self.gender, 16, 16, 9)
        #pyxel.blt(self.monster_X, self.monster_Y, 0, 8*coef, self.gender, 8, 8, 9) 

class Game:

    def __init__(self):
        pyxel.init(128, 128, title="Nuit du cOde 2022")
        pyxel.load("ressources.pyxres")

        self.start = True
        self.turn = 1
        self.start_time = time.time()

        self.char = Main_Char(56, 110)
        self.monsters_list = []

        pyxel.run(self.update, self.draw)

    def create_monster(self):
        lvl =  2 if self.turn == 5 else 3 if self.turn == 10 else 1
        if lvl == 1:
            self.monsters_list.append(Monster(randint(20, 88), randint(20, 90)))
        elif lvl == 2:
            self.monsters_list.append(Monster(randint(20, 88), randint(20, 90)))
        elif lvl == 3:
            self.monsters_list.append(Monster(randint(20, 88), randint(20, 90)))

    def new_dungeon_monsters(self, nb):
        for _ in range(nb):
            self.create_monster()

        [(20, 20), (40, 20), (60, 20), (80, 20), (90, 20), (20, 40), (20, 60), (20, 80), (20, 90)]
    
    def new_dungeon(self):
        self.new_dungeon_monsters(self.turn)
        return randint(0, 1)
    
    def draw_dungeon(self, wall):
        for i in range(8):
            pyxel.blt(16*i, 0, 0, 16*wall, 80, 16, 16)

        for j in range(2):
            for i in range(8):
                pyxel.blt(112*j, 16*i, 0, 16*wall, 80, 16, 16)

        for j in range(6):
            for i in range(7):
                pyxel.blt(16+16*j, 16+16*i, 0, 16-16*wall, 96, 16, 16)

    def fight(self):
        for monster in self.monsters_list:
            if monster.monster_X <= self.char.player_X+14 and monster.monster_Y <= self.char.player_Y+14 and monster.monster_X+14 >= self.char.player_X and monster.monster_Y+14 >= self.char.player_Y:
                self.char.life -= 5
                self.char.player_Y += randint(5, 15)
            if monster.monster_X <= self.char.player_X+19 and monster.monster_Y <= self.char.player_Y+19 and monster.monster_X+19 >= self.char.player_X and monster.monster_Y+19 >= self.char.player_Y:
                if pyxel.btn(pyxel.KEY_SPACE):
                    monster.life -= 3
                    if monster.life <= 0:
                        self.monsters_list.remove(monster)
                    return True

    def give_end_time(self):
        return int(time.time() - self.start_time)

    def update(self):
        self.char.move()
        self.fight()

    def draw(self):
        pyxel.cls(0)
        self.all_time = int(time.time() - self.start_time)
        if self.start:
            self.wall = self.new_dungeon()
            self.start = False

        if self.char.life > 0 and self.turn <= 1:
            self.draw_dungeon(self.wall)

            if len(self.monsters_list) == 0:
                pyxel.blt(48, 0, 0, 0, 64, 32, 16)
                if (self.char.player_X >= 48 and self.char.player_X <= 80) and self.char.player_Y <= 10:
                    self.turn += 1
                    self.wall = self.new_dungeon()
                    self.char.player_X, self.char.player_Y = 56, 110

            
            if len(self.monsters_list) != 0:
                pyxel.blt(48, 0, 0, 0, 48, 32, 16)
                for monster in self.monsters_list:
                    monster.draw()

            pos = 48 if self.fight() == True else 0
            self.char.draw(pos)

            color = 11 if self.wall == 1 else 7
            pyxel.text(100, 5, f"{self.char.life} HP", color)
            pyxel.text(5, 5, f"{int(time.time() - self.start_time)}s", color)
            pyxel.text(5, 118, f"{self.turn}", color)

        elif self.char.life <= 0:
            self.draw_dungeon(self.wall)
            pyxel.blt(70, 56, 0, 96, 0, 16, 16, 11)
            pyxel.text(2, 2, f"Vous avez perdu !\nVous etiez manche n°{self.turn}", 7)

        elif self.turn > 1:
  
            all_time = self.give_end_time()
            h, r = all_time // 3600, all_time % 3600
            m, s = r // 60, r % 60
            pyxel.text(50, 35, "Bravo !", 7)
            pyxel.text(8, 50, f"Vous avez gagne en {h}h {m}m {s}s.", 7)
            pyxel.blt(56, 70, 0, 112, 0, 16, 16, 11)

Game()
