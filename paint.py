import pygame

brush = pygame.image.load('brush.png')   
bigBrush = pygame.transform.scale(brush, (40, 40))
smallBrush = pygame.transform.scale(brush, (30, 30))

class button:
    def __init__(self, colour, height, width, x, y):
        self.colour = colour
        self.height = height
        self.width = width
        self.x = x
        self.y = y

    def draw(self, win, outline=False):
        if outline:
            pygame.draw.rect(win, (0,0,0), (self.x-2,self.y-2,self.height+3,self.width+3),2)
        pygame.draw.rect(win, self.colour, (self.x,self.y,self.height,self.width),0)
        

    def isOn(self, pos):
        if pos[0] >= self.x and pos[0] <= self.x + self.width:
            if pos[1] >= self.y and pos[0] <= self.y + self.height:
                return True
        return False

pygame.init()
pygame.display.set_icon(brush)
pygame.display.set_caption("Paint")
font = pygame.font.SysFont("comic sans", 30, True, False)
win = pygame.display.set_mode((500, 500))
canvas = win.copy()
colour = (0,0,0)
mouse = pygame.mouse
red = button((255,0,0), 30, 30, 3, 465)
orange = button((204,102,0), 30, 30, 36, 465)
yellow = button((255,255,0), 30, 30, 69, 465)
green = button((0,255,0), 30, 30, 102, 465)
blue = button((0,0,255), 30, 30, 135, 465)
purple = button((127,0,255), 30, 30, 3, 430)
pink = button((255,51,153), 30, 30, 36, 430)
black = button((0,0,0), 30, 30, 69, 430)
white = button((255,255,255), 30, 30, 102, 430)
grey = button((128,128,128), 30, 30, 135, 430)
r_select = False
o_select = False
y_select = False
green_select = False
blue_select = False
pu_select = False
pi_select = False
black_select = False
w_select = False
grey_select = False
SIZE = 10

def redraw_window():
    win.fill((255,255,255))
    win.blit(canvas, (0,0))
    win.blit(smallBrush, (168, 430))
    win.blit(bigBrush, (168, 460))
    brush_size = font.render("Brush Size: " + str(SIZE), 0, (0,0,0))
    win.blit(brush_size, (10,10))
    red.draw(win, r_select)
    orange.draw(win, o_select)
    yellow.draw(win, y_select)
    green.draw(win, green_select)
    blue.draw(win, blue_select)
    purple.draw(win, pu_select)
    pink.draw(win, pi_select)
    black.draw(win, black_select)
    white.draw(win, w_select)
    grey.draw(win, grey_select)
    pygame.draw.line(win, (0,0,0), (0,420), (500,420), 2)
    pygame.draw.circle(win, colour, (pygame.mouse.get_pos()),5)
    pygame.display.update()

canvas.fill((255,255,255))
run = True
while run:
    left_pressed, middle_pressed, right_pressed = mouse.get_pressed()
    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
            run = False
        elif left_pressed:
            if pos[0] >= 168 and pos[0] < 208:
                if pos[1] >= 460 and pos[1] < 500:
                    if SIZE < 30:
                        SIZE += 1
                        
            if pos[0] >=168 and pos[0] < 198:
                if pos[1] >= 430 and pos[1] < 460:
                    if SIZE > 1:
                        SIZE = SIZE -1 
            if red.isOn(pos):
                colour = red.colour
            elif orange.isOn(pos):
                colour = orange.colour 
            elif yellow.isOn(pos):
                colour = yellow.colour
            elif green.isOn(pos):
                colour = green.colour 
            elif blue.isOn(pos):
                colour = blue.colour 
            elif purple.isOn(pos):
                colour = purple.colour 
            elif pink.isOn(pos):
                colour = pink.colour 
            elif black.isOn(pos):
                colour = black.colour 
            elif white.isOn(pos):
                colour = white.colour 
            elif grey.isOn(pos):
                colour = grey.colour 
       
            if pos[1] < 410:
                pygame.draw.circle(canvas, colour, (pygame.mouse.get_pos()), SIZE)   
        elif right_pressed:
            colour = (0,0,0)   
    if colour == red.colour:
        r_select = True 
    else:
        r_select = False
    if colour == orange.colour:
        o_select = True 
    else:
        o_select = False
    if colour == yellow.colour:
        y_select = True
    else:
        y_select = False
    if colour == green.colour:
        green_select = True
    else:
        green_select = False
    if colour == blue.colour:
        blue_select = True
    else:
        blue_select = False
    if colour == purple.colour:
        pu_select = True
    else:
        pu_select = False
    if colour == pink.colour:
        pi_select = True
    else:
        pi_select = False
    if colour == black.colour:
        black_select = True
    else:
        black_select = False
    if colour == white.colour:
        w_select = True
    else:
        w_select = False
    if colour == grey.colour:
        grey_select = True
    else:
        grey_select = False
    redraw_window()
    pygame.display.update()