from pygame import*

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, x, y, size_x, size_y, speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed

    def reset(self):
        window.blit(self.image, (self.rect.x, selfq.rect.y))

class Player1(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_w] and self.rect.x < win_width - 60:
            self.rect.x += self.speed

class Player2(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_o] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_l] and self.rect.x < win_width - 60:
            self.rect.x += self.speed

player1 = Player1('platform.png', 325, 455, 60, 40, 5)
player2 = Player2('platform.png', 325, 455, 60, 40, 5)

background = (255,255,255)
win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
window.fill(background)
display.set_caption("Пинг-понг")

game = True
FPS = 60
clock = time.Clock()

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    
    player1.update()
    player2.update()

    clock.tick(FPS)
    display.update()