from settings import *

from snake import Snake
from apple import Apple
class Main:
    def __init__(self):

        #General 
        pygame.init()#This line is important because it will initialize all the modules in the pygame library.
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH ,WINDOW_HEIGHT))
        pygame.display.set_caption("Snake")
        #Title for the game.
        #This Line of code will create a window in which snake will movw to eat an apple.

        #GAME_OBJECTS
        self.bg_rects = [pygame.Rect((col + int(row%2 == 0))* CELL_SIZE, row*CELL_SIZE ,CELL_SIZE ,CELL_SIZE) for col in range(0 , COLS ,2) for row in range(ROWS)]
        #(col + int(row%2 == 0))* CELL_SIZE : left of rectangle 
        #row*CELL_SIZE : right and other two are height and width.
        # 0 is the start value and 2 is the step value so that will create alt rectangles.
        #In this line of code we are creating a list of rectangles alternatly on even rows : darkgreen and on odd rows :      lightgreen. 
        #This are instance we have to make to define and show on the screen.
        self.snake = Snake();
        self.apple = Apple(self.snake);

        #Timer
        self.update_event = pygame.event.custom_type()
        pygame.time.set_timer(self.update_event, 200)
        self.game_active = False#this code is for ki ek baar snake is dead toh directly game start na ho jaye 


    
    def draw_bg(self):
        for rect in self.bg_rects:
            pygame.draw.rect(self.display_surface, DARK_GREEN, rect)

    def input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]: 
            self.snake.direction = pygame.Vector2(1,0) if self.snake.direction.x != -1 else self.snake.direction
            #This line of code is written as if snake is moving in right and we clicked left btn then 
            #its also moving to left which shouldnt be possible so to do that we have written this code.
        if keys[pygame.K_LEFT]: 
            self.snake.direction = pygame.Vector2(-1,0) if self.snake.direction.x != 1 else self.snake.direction
        if keys[pygame.K_UP]: 
            self.snake.direction = pygame.Vector2(0,-1) if self.snake.direction.y != 1 else self.snake.direction
        if keys[pygame.K_DOWN]: 
            self.snake.direction = pygame.Vector2(0,1) if self.snake.direction.y != -1 else self.snake.direction

    def collision(self):
        #apple
        if self.snake.body[0] == self.apple.pos:
            self.snake.has_eaten = True #This is an attribute. 
            self.apple.set_pos()
        #game over : if snake touches itself or goes out of the window.
        if self.snake.body[0] in self.snake.body[1:] or \
            not 0 <= self.snake.body[0].x < COLS or \
            not 0 <= self.snake.body[0].y < ROWS:
            self.snake.reset()
            self.game_active = False

        


    def run (self) :
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

                if event.type == self.update_event and self.game_active:
                    self.snake.update()

                if event.type == pygame.KEYDOWN and not self.game_active:
                    self.game_active = True


            self.display_surface.fill(LIGHT_GREEN)
            self.input()
            self.collision()
            self.draw_bg()
            self.snake.draw()
            self.apple.draw()
            pygame.display.update()

if __name__ == "__main__":
  main = Main()
  main.run()