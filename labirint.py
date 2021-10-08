#создай игру "Лабиринт"!
import pygame 
pygame.init()

class GameSprite(pygame.sprite.Sprite):
    def __init__(self, sprite_image, sprite_x, sprite_y, sprite_speed):
        super().__init__()

        self.image = pygame.transform.scale(pygame.image.load(sprite_image), (65,65))
        self.speed = sprite_speed
        self.rect = self.image.get_rect()
        self.rect.x = sprite_x
        self.rect.y = sprite_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Hero(GameSprite):
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.x < 635:
            self.rect.x += self.speed
        if keys[pygame.K_UP] and self.rect.y < 635:
            self.rect.y += self.speed
        if keys[pygame.K_DOWN] and self.rect.y > 5:
            self.rect.y -= self.speed 

class Enemy(GameSprite):
    direction = 'left'
    x_start = 550
    x_finish = 600

    def update(self):
        if self.rect.x <= self.x_start:
            self.direction = 'right'
        if self.rect.x >= self.x_finish:
            self.direction = 'left'
        if self.direction == 'left':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed

class Wall(pygame.sprite.Sprite):
    def __init__(self, color_1, color_2, color_3, x, y, width, height):
        super().__init__()
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3

        self.width = width
        self.height = height

        self.image = pygame.Surface((self.width, self.height))
        self.image.fill((color_1, color_2, color_3))

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y ))

window = pygame.display.set_mode((700,500))
pygame.display.set_caption('Labirint')
background = pygame.transform.scale(pygame.image.load('cosmos.back.jpg.jpg'), (700,500))

game = True

player = Hero("hero.png", 5, 400, 4)
treasure = GameSprite("treasure.png", 550, 100, 0)
cyborg = Enemy("cyborg.png", 500, 350, 2)
cyborg2 = Enemy("cyborg.png", 500, 200, 2)
#trap = Enemy()

wall1v = Wall(0,0 , 56, 60, 40, 15, 350)
wall1h = Wall(0, 0, 56, 60, 470, 600, 15)
wall2h = Wall(0,0, 56, 60, 40, 600, 15)
wall2v = Wall(0, 0, 56, 170, 135, 15, 350)
wall3v = Wall(0, 0, 56, 280, 40, 15, 350)
wall4v = Wall(0, 0, 56, 390, 135, 15, 350)
wall5v = Wall(0, 0, 56, 500, 40, 15, 350)
wall6v = Wall(0, 0, 56, 650, 40, 15, 445)
walls = [wall1v, wall1h, wall2h, wall2v, wall3v, wall4v, wall5v, wall6v]

clock = pygame.time.Clock()
finish = False

pygame.font.init()
font = pygame.font.Font(None, 70)
win = font.render('You WIN!', True, (250, 200, 0))
lose = font.render('You LOSE!', True, (0, 70, 0))

while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    window.blit(background, (0,0))
    player.update()
    cyborg.update()
    cyborg2.update()
    wall1v.draw_wall()
    wall1h.draw_wall()
    wall2h.draw_wall()
    wall2v.draw_wall()
    wall3v.draw_wall()
    wall4v.draw_wall()
    wall5v.draw_wall()
    wall6v.draw_wall()
    player.reset()
    treasure.reset()
    cyborg.reset()
    cyborg2.reset()

    for wall in walls:
        if pygame.sprite.collide_rect(player, wall):
            player.rect.x = 5
            player.rect.y = 400
    
    if pygame.sprite.collide_rect(player, cyborg):
        finish = True
        window.blit(lose, (250,350))
        player.rect.x = 5
        player.rect.y = 400


    if pygame.sprite.collide_rect(player, cyborg2):
        finish = True
        window.blit(lose, (250,350))
        player.rect.x = 5
        player.rect.y = 400





    clock.tick(60)
    pygame.display.update()