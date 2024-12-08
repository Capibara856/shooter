from pygame import*

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
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y >= 5:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y <= 1000:
            self.rect.y += self.speed
    def update_2(self):
        keys_pressed = keys.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 1050:
            self.rect.y += self.speed
class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed

#Ракетки
racket1 = Player_move("racket.png", 30, 200, 4, 50, 150)
racket2 = Player_move("racket.png", 520, 200, 4, 50, 150)
ball = GameSprite("tenis_ball.png", 200, 200, 4, 50, 50)
game = True
finish = False
#игровой цикл
while game:

    for e in event.get():
        if e.type == QUIT:
            game = False
#Конец
display.update()