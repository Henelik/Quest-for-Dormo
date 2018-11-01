import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, screenScale):
        self.possessed = False
        self.xPos = 0
        self.yPos = 0
        self.facingDirection = 0
        self.screenScale = screenScale

        pygame.sprite.Sprite.__init__(self)

        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.image = pygame.Surface([self.screenScale, self.screenScale])
        self.image.fill((150, 150, 0))

        # Fetch the rectangle object that has the dimensions of the image
        # Update the position of this object by setting the values of rect.x and rect.y
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.x = self.xPos * self.screenScale
        self.rect.y = self.yPos * self.screenScale
        #self.rect = pygame.Rect(self.xPosScreen, self.yPosScreen, 66, 92)

    def walkEast(self):
        self.xPos += 1
        self.update()

    def walkNorth(self):
        self.yPos -= 1
        self.update()

    def walkWest(self):
        self.xPos -= 1
        self.update()

    def walkSouth(self):
        self.yPos += 1
        self.update()
