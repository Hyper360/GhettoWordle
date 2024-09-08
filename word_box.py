import pygame
pygame.init()
font = pygame.font.SysFont('Comic Sans', 30, bold=True)

class Box():
    def __init__(self, screen : pygame.Surface, width, height, RowNum, ColNum):
        self.screen = screen
        self.width = width
        self.height = height
        self.screenWidth = self.screen.get_width()
        self.screenHeight = self.screen.get_height()
        self.ROW = RowNum
        self.COL = ColNum
        self.color = (200, 200, 200)

        self.letter = ''
        self.clicked = False
        self.surface = font.render(self.letter, True, (200, 0, 0))
        self.changed = False

        self.rect = pygame.Rect(self.width * self.COL, self.height * self.ROW, self.width, self.height)

    def checkClicked(self):
        mousePos = pygame.mouse.get_pos()
        mouseClicked = pygame.mouse.get_pressed()[0]

        if mouseClicked:
            if self.rect.collidepoint(mousePos[0], mousePos[1]):
                self.clicked = True
            else:
                self.clicked = False

    def changeValue(self, event):
        if self.clicked == True and self.changed == False:
            self.letter = event.unicode
            self.surface = font.render(self.letter.upper(), True, (200, 0, 0))
            self.changed = True


    def draw(self):
        self.checkClicked()
        pygame.draw.rect(self.screen, self.color, self.rect)
        pygame.draw.rect(self.screen, (0, 0, 0), self.rect, 2, 5)

        self.screen.blit(self.surface, self.rect.center)
