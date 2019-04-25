import random
from pygame.locals import *
import pygame, sys, math
import pygame.gfxdraw
import time
import csv

# Screen Setup #################################################################
pygame.init()
scr = pygame.display.set_mode((1500, 800))
pygame.display.set_caption('Fitts\' Law')

myfont1 = pygame.font.SysFont("monospace", 15)

clock = pygame.time.Clock()

# Open text file
outfile = open("dataCollected.csv", 'w',newline='')

outfile_field = ['num', 'W', 'D', 'ID', 'MT', 'TP', 'time']
writer = csv.DictWriter(outfile, fieldnames=outfile_field)
writer.writeheader()

count = 1
startingTime = 0

# Update circle ################################################################

def update_current_circle(current_circle):
    if pair_start == 1:
        if current_circle > math.ceil(num_of_circle / 2):
            return current_circle - math.ceil(num_of_circle / 2)
        else:
            return math.ceil(num_of_circle / 2) + current_circle

    # Randomly choose the start point of the next pair
    else:
        while True:
            rand = random.randint(1, num_of_circle + 1)
            if rand != current_circle:
                break
        return rand


# Game Loop ####################################################################
def game():
    global count
    global circle_radius
    global current_circle
    global distance
    global pair_start
    global initial
    global timing
    global startingTime
    
    while timing<=10:
        timing = time.time()-initial
        
        
        pygame.display.update()
        scr.fill((255, 255, 255))

    
        # Drawing circles
        for i in range(1, num_of_circle + 1):
            pygame.gfxdraw.aacircle(scr, 750 + int(math.cos(math.pi * 2 / num_of_circle * i) * distance / 2),
                                    400 + int(math.sin(math.pi * 2 / num_of_circle * i) * distance / 2),
                                    circle_radius, (100, 100, 100))
    
        # Select a circle and make it red
        pygame.gfxdraw.filled_circle(scr, 750 + int(math.cos(math.pi * 2 / num_of_circle * current_circle) * distance / 2),
                                     400 + int(math.sin(math.pi * 2 / num_of_circle * current_circle) * distance / 2),
                                     circle_radius, (255, 0, 0))
    
        # Display Text
        # render text
        label1 = myfont1.render("Distance: ", 1, (0, 0, 0))
        scr.blit(label1, (20, 20))
    
        label2 = myfont1.render("Width: ", 1, (0, 0, 0))
        scr.blit(label2, (20, 50))
    
    
        current = myfont1.render("#" + str(count), 1, (0, 0, 0))
        scr.blit(current, (1000, 20))
#    
        init_distance = myfont1.render(str(int(distance)), 1, (0, 0, 0))
        scr.blit(init_distance, (115, 22))
#    

        init_width = myfont1.render(str(circle_radius), 1, (0, 0, 0))
        scr.blit(init_width, (115, 50))
    
#        scr.blit(textinput_distance.get_surface(), (115, 22))
#        scr.blit(textinput_width.get_surface(), (115, 50))
    
        # Mouse Click Event
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                click = scr.get_at(pygame.mouse.get_pos()) == (255, 0, 0)
                if click == 1:
                    current_circle = update_current_circle(current_circle)
                    if pair_start == 1:
                        print("Log the time")
                        # Starting time
                        startingTime = time.time()
                        pair_start = 0
                    else:
#                        print("Random starting point!")
#                        ID = math.log2(distance / circle_radius + 1)
#                        MT = math.log2(2*distance/ circle_radius)
#                        # Log: Finishing time
#                        writer.writerow({'num': str(count),
#                                         'W': str(circle_radius),
#                                         'D': str(distance),
#                                         'ID': str(ID),
#                                         'MT': str(MT),
#                                         'TP': str(ID/MT),
#                                         'time': str((time.time() - startingTime))})
                        count += 1
                        pair_start = 1
                        
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
    


    print("Random starting point!")
    ID = math.log2(distance / circle_radius + 1)
    MT = math.log2(2*distance/ circle_radius)
    # Log: Finishing time
    writer.writerow({'num': str(count),
                     'W': str(circle_radius),
                     'D': str(distance),
                     'ID': str(ID),
                     'MT': str(MT),
                     'TP': str(ID/MT),
                     'time': str(timing)})

#    

################################################################################
    

#Calling Function game every 10sec with new Distance and Circle Radius
            
num_of_circle = 16
circle_radius = 22  # 22, 55
distance = 500  # 125, 250, 500
current_circle = 1
pair_start = 1
initial = time.time()
timing =0 
game()

initial = time.time()
timing =0 
num_of_circle = 10
circle_radius = 22  # 22, 55
distance = 200  # 125, 250, 500
count=1
game()

initial = time.time()
timing =0 
num_of_circle = 6
circle_radius = 50  # 22, 55
distance = 400  # 125, 250, 500
count=1
game()

initial = time.time()
timing =0 
num_of_circle = 9
circle_radius = 50  # 22, 55
distance = 600  # 125, 250, 500
count=1
game()
