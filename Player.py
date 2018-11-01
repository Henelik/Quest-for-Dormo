import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, screenScale, level):
        self.possessed = True # Can the player control the player character
        self.xPos, self.yPos = level.getSpawn()
        self.facingDirection = 0
        self.screenScale = screenScale
        self.levelRef = level

        pygame.sprite.Sprite.__init__(self)

        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.image = pygame.Surface([self.screenScale, self.screenScale])
        self.image.fill((150, 150, 0))

        # Fetch the rectangle object that has the dimensions of the image
        # Update the position of this object by setting the values of rect.x and rect.y
        self.rect = self.image.get_rect()
        self.update()

    def update(self):
        self.rect.x = self.xPos * self.screenScale
        self.rect.y = self.yPos * self.screenScale

    def walkEast(self):
        if self.xPos + 1 < self.levelRef.xSize:
            if self.levelRef.tileset[self.yPos][self.xPos+1] == 0:
                self.xPos += 1
                self.update()

    def walkNorth(self):
        if self.yPos - 1 >= 0:
            if self.levelRef.tileset[self.yPos-1][self.xPos] == 0:
                self.yPos -= 1
                self.update()

    def walkWest(self):
        if self.xPos - 1 >= 0:
            if self.levelRef.tileset[self.yPos][self.xPos-1] == 0:
                self.xPos -= 1
                self.update()

    def walkSouth(self):
        if self.yPos + 1 < self.levelRef.ySize:
            if self.levelRef.tileset[self.yPos+1][self.xPos] == 0:
                self.yPos += 1
                self.update()
