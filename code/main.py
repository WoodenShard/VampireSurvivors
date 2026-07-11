from settings import *
from player import Player

class Game:
    def __init__(self):
        pygame.init()
        self.display = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
        pygame.display.set_caption('Vampire Survivors')
        self.clock = pygame.time.Clock()
        self.running: bool = True

        self.all_sprites = pygame.sprite.Group()

        self.player = Player((100,200), self.all_sprites)

    def run(self):
        while self.running:
            # dt
            dt = self.clock.tick() / 1000

            # event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running: bool = False
            

            self.all_sprites.update(dt)

            self.display.fill('black')   
            self.all_sprites.draw(self.display)        
            pygame.display.update()

        pygame.quit()


        
if __name__ == '__main__':
    game = Game()
    game.run()
 






