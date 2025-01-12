from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, weight, height):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(weight,height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))

class Player(GameSprite):
    def move_left(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if key_pressed[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

    def move_right(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if key_pressed[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

back = (80, 229, 123)
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
window.fill(back)

racket1 = Player('168297179_10620029.png', 30, 200, 4, 40, 150)
racket2 = Player('168297179_10620029.png', 520, 200, 4, 40, 150)
ball = GameSprite('523686.png', 200, 200, 4, 50, 50)

game = True
finish = False
clock = time.Clock()
FPS = 60
speed_x = 3
speed_y = 3

font.init()
font_sample = font.Font(None, 35)
lose1 = font_sample.render('ИГРОК 1 ПРОИГРАЛ', True, 'brown1')
lose2 = font_sample.render('ИГРОК 2 ПРОИГРАЛ', True, 'brown1')

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if not finish:
        window.fill(back)

        if sprite.collide_rect(racket1, ball) or sprite.collide_rect(racket2, ball):
            speed_x *= -1

        if ball.rect.y > win_height-50 or ball.rect.y < 0:
            speed_y *= -1

        if ball.rect.x <0:
            finish = True
            window.blit(lose1, (200, 200))

        if ball.rect.x > win_width:
            finish = True
            window.blit(lose2, (200, 200))

        racket1.move_left()
        racket2.move_right()

        ball.rect.x += speed_x
        ball.rect.y += speed_y

        racket1.reset()
        racket2.reset()
        ball.reset()

    display.update()
    clock.tick(FPS)