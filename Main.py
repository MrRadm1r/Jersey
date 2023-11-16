import pygame as pg
class Jersey:
    def init(self):
        pg.init()
        self.x = 500
        self.y = 500
        self.win = pg.display.set_mode((self.x, self.y))
        #pg.display.set_caption('Green Paws alpha:1.3')
        #pg.display.set_icon(pg.image.load('images/ghost.png'))
        self.run = True
        self.width = 32
        self.height = 32

        # ПИСАТЬ ДО
        self.game_events()

    def game_events(self):
        while self.run:
            #self.clock.tick(60)
            #self.win.fill((198, 223, 144))
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.run = False
            self.drawon()
        pg.quit()

    def drawon(self):
        #pg.rect(self.win, (255,0,0), (0,0,100,100))
        pg.display.update()

Jersey()