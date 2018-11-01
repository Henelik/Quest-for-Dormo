import sys, pygame
import Player
pygame.init()

class App:
    def __init__(self):
        self.renderGroup = pygame.sprite.Group()
        self.size = self.width, self.height = 1000, 750
        self.screenScale = 64 # size of a tile on the screen

    def onInit(self):
        pygame.init()
        self._displaySurf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._running = True

    def onEvent(self, event):
        if event.type == pygame.KEYDOWN:
            # Try to parse the input using the unicode character
            if event.unicode:
                self.parseInput(event.unicode)
            # If there is no unicode character, look in the self.keys dict
            elif event.key in self.keys.keys():
                self.parseInput(self.keys[event.key])
        if event.type == pygame.QUIT:
            self._running = False

    def parseInput(self, key):
        print(key)
        if key == "up":
            self.player.walkNorth()
        elif key == "down":
            self.player.walkSouth()
        elif key == "left":
            self.player.walkWest()
        elif key == "right":
            self.player.walkEast()
        elif key == "w":
            self.player.walkNorth()
        elif key == "s":
            self.player.walkSouth()
        elif key == "a":
            self.player.walkWest()
        elif key == "d":
            self.player.walkEast()
        elif key == "":
            self._running = False

    def onLoop(self):
        pass

    def onRender(self):
        self._displaySurf.fill((0, 0, 0))
        self.renderGroup.draw(self._displaySurf)
        pygame.display.flip()

    def onCleanup(self):
        pygame.quit()

    def onExecute(self):
        if self.onInit() == False:
            self._running = False

        self.keys = {273:"up", 276:"left", 275:"right", 274:"down"}

        self.player = Player.Player(self.screenScale)
        self.renderGroup.add(self.player)

        while(self._running):
            for event in pygame.event.get():
                self.onEvent(event)
            self.onLoop()
            self.onRender()
        self.onCleanup()

if __name__ == "__main__":
    theApp = App()
    theApp.onExecute()
