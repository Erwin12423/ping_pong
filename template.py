from pygame import *

'''
Step 1: Define GameSprite class here'''
class GameSprite(sprite.Sprite):
#class constructor
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
      #call for the class (Sprite) constructor:
        sprite.Sprite.__init__(self)
      #every sprite must store the image property
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
      #every sprite must have the rect property that represents the rectangle it is fitted in
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
'''
Step 2: Define Player calss here w/ 2 update methods:
    2.1 update_r: for the right player, move with the up and dow arrow keys
    2.2 update_l: for the left player, move with the w and s keys
'''
class Player(GameSprite):
  #method to control the sprite with arrow keys
   def update_1(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
    
   def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed


'''
Step 3: Define the background
    3.1 Size: width = 600, height = 500
    3.2 Color: Any
        Syntax: 
        back = (200, 255, 255) #Color code in RGB
        window.fill(back)
'''
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))

back = (200, 255, 255) #Color code in RGB
window.fill(back)
font.init()

font = font.Font(None, 80)



'''
Step 4: Create the 2 players and the ball
    4.1 racket1:
        - Instance of Player
        - x = 30, y = 200, size_x = 50, size_y = 150, speed = 4
    4.2 racket2:
        - Instance of Player
        - x = 520, y = 200, size_x = 50, size_y = 150, speed = 4
    4.1 ball:
        - Instance of GameSprite
        - x = 200, y = 200, size_x = 50, size_y = 50, speed = 4
'''
racket1 = Player("racket.png", 30, 200, 50, 150, 4)
racket2 = Player("racket.png", 520, 200, 50, 150, 4)
ball = GameSprite("tenis_ball.png", 200, 200, 50, 50, 4)

'''
Step 5: Create 1 font (size >35) and 2 texts to display the losing of 2 players:
    5.1: lose1text: 
        - Coordinate: (180, 0, 0)
    5.2: lose2text: 
        - Coordinate: (180, 0, 0)
'''

lose1text = font.render("Player1 lose" , 1 , (180, 0, 0))
lose2text = font.render("Player2 lose" , 1 , (180, 0, 0))


window.blit(lose1text, (10, 50))
window.blit(lose2text, (10, 50))

speed_x = 3
speed_y = 3

'''
Step 6: Define necessary details for the game loop, no delay for this game
'''
finish = False
game = True
FPS = 60
clock = time.Clock()

while game:
    '''
    Step 7: Quit events 
    '''
    for e in event.get():
        if e.type == QUIT:
            game = False

    
    if finish != True:

        window.fill(back)
        '''
        Step 8: Update the rackets and the ball 

        '''
        racket1.update_1()
        racket2.update_r()
        
        #Make the ball moves
        ball.rect.x += speed_x 
        ball.rect.y += speed_y

        '''
        Step 9: Check collision between the rackets and the ball.
        If true, multiply speed_x by -1 and speed_y by 1.   
        '''
        sprite.collide_rect(racket1, ball)
        sprite.collide_rect(racket2, ball)

        if sprite.collide_rect(racket1, ball) == True or sprite.collide_rect(racket2, ball) == True:
            speed_x = speed_x * -1
            speed_y = speed_y * -1

        

        '''
        Step 10: Check collision between the ball and the top/bottom edges.
        If true, multiply speed_y by -1. 
        '''    
        if ball.rect.y < 25 or ball.rect.y > win_height - 25:
            speed_y = speed_y * -1


        '''
        Step 11: Check collision between the ball and the left edge.
        If true:
            - Finish the game
            - Appear the lose1text at the middle   

        '''
        

        if ball.rect.x < 0 :
            finish = True
            window.blit(lose1text, (150, 200))

        '''
        Step 12: Check collision between the ball and the right edge.
        If true:
            - Finish the game
            - Appear the lose2text at the middle   
        '''
        if ball.rect.x > win_width:
            finish = True
            window.blit(lose2text, (150, 200))

        '''
        Step 13: Reset the rackets and the ball    
        '''
        racket1.reset()
        racket2.reset()
        ball.reset()


    display.update()
    clock.tick(FPS)