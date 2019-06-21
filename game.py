import sys, pygame

size = screenWidth, screenHeight = 320, 240


class SpaceShip:

    velocity = 5

    def __init__(self):
        self.width = 30
        self.height = 40
        self.x = screenWidth / 2 - self.width / 2
        self.y = screenHeight - self.height

    def draw(self):
        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(self.x, self.y, self.width, self.height))

    def update(self):
        if pygame.key.get_pressed()[pygame.K_LEFT]:
            statek.moveLeft()
        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            statek.moveRight()

    def moveLeft(self):
        if self.x > 0:
            self.x -= self.velocity
            if self.x < 0:
                self.x = 0

    def moveRight(self):
        if self.x < screenWidth - self.width:
            self.x += self.velocity
            if self.x > screenWidth - self.width:
                self.x = screenWidth - self.width


pygame.init()
black = 0, 0, 0
screen = pygame.display.set_mode(size)

statek = SpaceShip()
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill(black)

    statek.update()
    statek.draw()

    pygame.display.flip()
