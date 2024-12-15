from pygame import *
font.init()
mixer.init()
#Игровая сцена
win_len = 1080
win_width = 1080
back = (200,255,255) #Задний фон
window = display.set_mode((win_len,win_width))
window.fill(back)


#Классы
class GameSprite(sprite.Sprite):
    def __init__(self,player_image,player_x,player_y,player_speed,wight,height):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(wight,height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
class Player_move(GameSprite):
    def update_l(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y >= 5:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y <= 900:
            self.rect.y += self.speed
    def update_r(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 950:
            self.rect.y += self.speed
class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
#Ракетки
racket1 = Player_move("Снимок.PNG", 30, 200, 4, 50, 150)
racket2 = Player_move("Снимок.PNG", 980, 200, 4, 50, 150)
ball = GameSprite("Шар.PNG", 200, 200, 4, 50, 50)
game = True
finish = False
font = font.Font(None,35)
lose1 = font.render("PLAYER 1 LOSE",True,(180,0,0))
lose2 = font.render("PLAYER 2 LOSE", True,(180,0,0))
#игровой цикл
speed_x = 1
speed_y = 1
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:
        window.fill(back)
        racket1.update_l()
        racket2.update_r()
        ball.rect.x += speed_x
        ball.rect.y += speed_y

        if sprite.collide_rect(racket1,ball) or sprite.collide_rect(racket2,ball):
            speed_x *= -1
            speed_y *= 1
        if ball.rect.y > win_width-50 or ball.rect.y < 0:
                speed_y *= -1
        if ball.rect.x <= 0:
            finish = True
            window.blit(lose1, (200,200))
            game_over = True
        if ball.rect.y >= win_width:
            finish = True
            window.blit(lose2,(200,200))
            game_over = True
        racket1.reset()
        racket2.reset()
        ball.reset()
#Конец

    display.update()