class Obstacle(pg.sprite.Sprite):
    def __init__(self, color, width):
            self.color = color
            pg.sprite.Sprite.__init__(self)
            self.image = pygame.surface([width, 50])
            self.image.fill(self.color)
            self.rect = self.image.get_rect()
BLACK = (0,0,0)
obst1 = Obstacle(BLACK, 100)