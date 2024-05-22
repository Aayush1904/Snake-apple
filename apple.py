from settings import *
from random import choice
class Apple:
    def __init__(self ,snake):
        self.pos = pygame.Vector2()
        self.display_surface = pygame.display.get_surface()
        self.snake = snake
        #this self.snake is added as apple should know the snake position so that apple should not render on snake body.
        self.set_pos()
    #This method is done in order top get a random position for apple.
        
        #self.surf = pygame.image.load(join('..','apple','apple.png')).convert_alpha()
        #This will create a another surface on the main surface and load the image of apple.
        #This join method is used as '/'is different in every system so file path should not be incorrect therefor it is used.
        #convert_alpha method is used as this will give the img as file to python so that it can work faster..


    def set_pos(self):
        available_pos=[pygame.Vector2(x,y) for x in range(COLS) for y in range(ROWS) if pygame.Vector2(x,y) not in self.snake.body]
    #With this if statement we have deleted 3 reactangles os snake body so that apple would never lie on snakes body.
        self.pos = choice(available_pos)
        

    
    def draw(self):
        rect = pygame.Rect(self.pos.x * CELL_SIZE, self.pos.y * CELL_SIZE , CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(self.display_surface, 'red', rect) 
        #self.display_surface.blit(self.surf , rect)
        #blit is the method to one surface onto the other..