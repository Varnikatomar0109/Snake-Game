import pygame
import random#for thr random position of the food

pygame.init()#initiliase pygame instance

#setting the game window
window_width= 800
window_height=600
window = pygame.display.set_mode((window_width,window_height))
pygame.display.set_caption("snake game")
white=(255,255,255)
black = (0,0,0)
blue = (0,0,255)
game_over = False
score = 0
x1 = window_width // 2
y1 = window_height // 2



x1_change=0
y1_change=0
snake_body =[]
length_of_snake = 1
foodx = round(random.randrange(0,window_width-10)/10)*10.0#to set random poistion on x axis 
foody = round(random.randrange(0,window_height-10)/10)*10.0# to random poistion on y axis 
clock = pygame.time.Clock()


# to identify that game is over or not
#pygame.init(): Initializes all pygame modules to get the environment ready for the game.
#Setting up the display:
#pygame.display.set_mode((400, 300)): Creates a game window with dimensions 400 pixels wide and 300 pixels high.
#Game loop control:
#game_over = False: A variable to control when the game should end.
#Game loop:while not game_over: This loop runs as long as game_over is False.
#pygame.event.get(): Fetches all events (e.g., keyboard or mouse inputs) that occurred since the last iteration of the loop.
#Event handling:
#if event.type == pygame.QUIT: Checks if the user has closed the game window (clicked the "X" button).
#game_over = True: Ends the loop when the user quits the game
while not game_over:#while the game is not over
    for event in pygame.event.get():#event here is the moving od keyword and the mouse
        if event.type == pygame.QUIT:
            game_over = True
        #check for arrow keys pressed
        if event.type == pygame.KEYDOWN:# to check weater user click the key
          if event.key == pygame.K_LEFT:
             x1_change = -10
             y1_change = 0
          elif event.key == pygame.K_RIGHT:
             x1_change = 10 
             y1_change = 0
          elif event.key == pygame.K_UP:
             x1_change = 0
             y1_change = -10 
          elif event.key ==pygame.K_DOWN:
             x1_change = 0
             y1_change = 10
             

    x1 = x1 + x1_change
    y1 = y1 + y1_change
    if x1 >= window_width or x1<0 or y1>=window_height or y1 <0:
     game_over =True
    window.fill(black)
    snake_head= []
    snake_head.append(x1)#snake head 
    snake_head.append(y1)#snake head

    snake_body.append(snake_head)
    if len(snake_body)>length_of_snake:
       del snake_body[0]
    
    for segment in snake_body[:-1]:#checking from the back because of the  snake body is dynamic and static 
       if segment == snake_head:
          game_over =True
    font_style = pygame.font.SysFont(None,50)
    score_text = font_style.render("score: "+str(score),True, white)# to show the score 
    window.blit(score_text,(10,10))
    

    if x1 == foodx and y1 == foody:
       foodx = round(random.randrange(0,window_width-10)/10)*10.0#to set random poistion on x axis 
       foody = round(random.randrange(0,window_height-10)/10)
       length_of_snake +=1 # increase the length of snake
       score +=1 # increase the score 
       

    
    pygame.draw.rect(window,blue,[foodx,foody,10,10])
    #food item details
    for segment in snake_body:
       pygame.draw.rect(window,white,[segment[0],segment[1],10,10])
       
    pygame.display.update()#to show the new updates
    clock.tick(10)#to cantrol the speed 

    #sanke eat the food when the coodinate of snake annd coodinate of the food are same
# sanke head is equal to sanke body thats mean snake hit himself


