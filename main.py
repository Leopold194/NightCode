"""
Documentation:

Le but du jeu est simple, le joueur doit survivre aller au plus loin dans le jeu en traverssant les salles, pour cela,
le joueur doit tuer tous les énemies pour ouvrir la porte qui permet d'avancer à la salle d'après.

Ce jeu se joue avec les flèches directionnelles du clavier, le joueur peut aussi utiliser les touches espace pour taper les énemies.

1ere fin: Lorsque le joueur meurt la partie est finie, le nombre de salles parcourues est est le score du joueur (son chrono sera aussi indiqué).
2eme fin: Lorsque le joueur arrive à aller au dela de la 10eme salle la partie est gagnée.


"""

from random import randint, choice
import pyxel
import time

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
            if (self.player_X > 48 and self.player_X < 70 and self.player_Y > 0) or self.player_Y > 17:
                self.player_Y -= 1
        if (pyxel.btn(pyxel.KEY_DOWN) or pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_DOWN)) and self.player_Y < 112:
            self.player_Y += 1

class Monster:

    def __init__(self, x, y, b = None):
        self.monster_X = x
        self.monster_Y = y
        self.gender = choice([16, 32])
        self.boss = b

        if not self.boss:
            self.life = choice([30, 60])
        else:
            self.life = 500

    def draw(self):
        if not self.boss:
            coef = pyxel.frame_count // 4 % 2
            pyxel.blt(self.monster_X, self.monster_Y, 0, 16*coef, self.gender, 16, 16, 9)
        else:
            pyxel.blt(self.monster_X, self.monster_Y, 0, 0, 112, 32, 32, 9)

class Game:

    def __init__(self):
        pyxel.init(128, 128, title="Nuit du cOde 2022")
        pyxel.load("ressources.pyxres")

        self.start = True
        self.turn = 1
        self.start_time = time.time()

        self.char = Main_Char(56, 110)
        self.monsters_list = []

        pyxel.playm(0, loop = True)
        pyxel.mouse(True)

        self.home_state = True
        self.rules_state = False
        self.play_state = False

        pyxel.run(self.update, self.draw)

    def create_monster(self):
        lvl =  2 if self.turn == 5 or self.turn == 10 else 1
        if lvl == 1:
            self.monsters_list.append(Monster(randint(20, 88), randint(20, 90)))
        elif lvl == 2:
            self.monsters_list.append(Monster(randint(20, 72), randint(20, 74), True))

    def new_dungeon_monsters(self, nb):
        if self.turn != 5 and self.turn != 10:
            for _ in range(nb):
                self.create_monster()
        else:
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
            if not monster.boss:
                if monster.monster_X <= self.char.player_X+14 and monster.monster_Y <= self.char.player_Y+14 and monster.monster_X+14 >= self.char.player_X and monster.monster_Y+14 >= self.char.player_Y:
                    self.char.life -= 5
                    self.char.player_Y += randint(5, 15)
                if monster.monster_X <= self.char.player_X+19 and monster.monster_Y <= self.char.player_Y+19 and monster.monster_X+19 >= self.char.player_X and monster.monster_Y+19 >= self.char.player_Y:
                    if pyxel.btn(pyxel.KEY_SPACE):
                        monster.life -= 3
                        if monster.life <= 0:
                            self.monsters_list.remove(monster)
                        return True
            else:
                if monster.monster_X <= self.char.player_X+30 and monster.monster_Y <= self.char.player_Y+30 and monster.monster_X+30 >= self.char.player_X and monster.monster_Y+30 >= self.char.player_Y:
                    self.char.life -= 15
                    self.char.player_Y += randint(5, 15)
                if monster.monster_X <= self.char.player_X+35 and monster.monster_Y <= self.char.player_Y+35 and monster.monster_X+35 >= self.char.player_X and monster.monster_Y+35 >= self.char.player_Y:
                    if pyxel.btn(pyxel.KEY_SPACE):
                        monster.life -= 3
                        if monster.life <= 0:
                            self.monsters_list.remove(monster)
                        return True

    def give_end_time(self):
        return int(time.time() - self.start_time)

    def home(self):

        pyxel.rect(BUTTON_PLAY_X, BUTTON_PLAY_Y, BUTTON_PLAY_W, BUTTON_PLAY_H, 13) # (x,y,w,h,color)
        pyxel.text(BUTTON_PLAY_X + BUTTON_PLAY_W/2 - 9, BUTTON_PLAY_Y + BUTTON_PLAY_H/2 - 2, "JOUER", 0)

        pyxel.rect(BUTTON_QUIT_X, BUTTON_QUIT_Y, BUTTON_QUIT_W, BUTTON_QUIT_H, 13) # (x,y,w,h,color)
        pyxel.text(BUTTON_QUIT_X + BUTTON_QUIT_W/2 - 13, BUTTON_QUIT_Y + BUTTON_QUIT_H/2 - 2, "QUITTER", 0)

        pyxel.rect(BUTTON_RULES_X, BUTTON_RULES_Y, BUTTON_RULES_W, BUTTON_RULES_H, 13) # (x,y,w,h,color)
        pyxel.text(BUTTON_RULES_X + BUTTON_RULES_W/2 - 11, BUTTON_RULES_Y + BUTTON_RULES_H/2 - 2, "Regles", 0)

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

    def update(self):
        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            if pyxel.mouse_x >= BUTTON_PLAY_X and pyxel.mouse_x <= BUTTON_PLAY_X+BUTTON_PLAY_W and pyxel.mouse_y >= BUTTON_PLAY_Y and pyxel.mouse_y <= BUTTON_PLAY_Y+BUTTON_PLAY_H:
                self.home_state = False
                self.play_state = True
            elif pyxel.mouse_x >= BUTTON_QUIT_X and pyxel.mouse_x <= BUTTON_QUIT_X+BUTTON_QUIT_W and pyxel.mouse_y >= BUTTON_QUIT_Y and pyxel.mouse_y <= BUTTON_QUIT_Y+BUTTON_QUIT_H:
                pyxel.quit()
            elif pyxel.mouse_x >= BUTTON_RULES_X and pyxel.mouse_x <= BUTTON_RULES_X+BUTTON_RULES_W and pyxel.mouse_y >= BUTTON_RULES_Y and pyxel.mouse_y <= BUTTON_RULES_Y+BUTTON_RULES_H:
                self.home_state = False
                self.rules_state = True
            elif pyxel.mouse_x >= BUTTON_BACK_X and pyxel.mouse_x <= BUTTON_BACK_X+BUTTON_BACK_W and pyxel.mouse_y >= BUTTON_BACK_Y and pyxel.mouse_y <= BUTTON_BACK_Y+BUTTON_BACK_H:
                self.rules_state = False
                self.home_state = True
        
        self.char.move()
        self.fight()

    def draw(self):
        pyxel.cls(0)
        
        if self.home_state or self.rules_state:
            for i in range(8):
                for y in range(8):
                    pyxel.blt(i*16, y*16, 0, 0, 80, 16, 16)

            pyxel.text(42, 5, "The Dungeon", 7)

            if self.home_state:
                self.home()
            if self.rules_state:
                self.rules()

        elif self.play_state == True:
            pyxel.mouse(False)
            self.all_time = int(time.time() - self.start_time)
            if self.start:
                self.wall = self.new_dungeon()
                self.start = False

            if self.char.life > 0 and self.turn <= 10:
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

            elif self.turn > 10:
    
                all_time = self.give_end_time()
                h, r = all_time // 3600, all_time % 3600
                m, s = r // 60, r % 60
                pyxel.text(50, 35, "Bravo !", 7)
                pyxel.text(8, 50, f"Vous avez gagne en {h}h {m}m {s}s.", 7)
                pyxel.blt(56, 70, 0, 112, 0, 16, 16, 11)

Game()
