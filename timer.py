# Pygame Timer made by Huatao

###########
# Imports #
###########

import time
import pygame
import sys
from pygame.locals import *
from pygame import mixer


##############
# Game Setup #
##############

pygame.init()
mixer.init()
pygame.display.set_caption("Timer")
# Define Surface
gameDisplay = pygame.display.set_mode((400, 400))
# Set Clock
clock = pygame.time.Clock()
green = (0, 255, 0)
rectpos = (0, 0)
# List to store user's set time
seconds = []
# A variable to determine whether or not to play the alarm
alarm_state = ""
font = pygame.font.SysFont(None, 40)
font2 = pygame.font.SysFont(None, 30)
text = font2.render("".join(seconds), False, (0, 0, 200))
# Set up alarm sound
sound = mixer.Sound("bell.wav")


##################
# Function Setup #
##################


def start_timer():
    try:
        times = "".join(seconds)
        final_time = int(times)
        gameDisplay.blit(font.render(times, True, (0, 0, 200)), (150, 125))
        start_time = time.monotonic()
        time.sleep(final_time)
        end_time = time.monotonic()
        elapsed_time = end_time - start_time
        if alarm_state == "on":
            sound.play()
        print(elapsed_time)
    except:
        print("Error")
        quit()


def clear_timer():
    seconds.clear()


def quit_timer():
    pygame.quit()
    sys.exit()
    quit()


##########################
# Event and Screen Setup #
##########################

while True:
    try:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEMOTION:
                # Move the timer's "mouse" accordingly to the real mouse
                rectpos = event.pos
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Detect if the mouse presses down on the buttons
                if mouse.colliderect(button1):
                    seconds.append("1")
                if mouse.colliderect(button2):
                    seconds.append("2")
                if mouse.colliderect(button3):
                    seconds.append("3")
                if mouse.colliderect(button4):
                    seconds.append("4")
                if mouse.colliderect(button5):
                    seconds.append("5")
                if mouse.colliderect(button6):
                    seconds.append("6")
                if mouse.colliderect(button7):
                    seconds.append("7")
                if mouse.colliderect(button8):
                    seconds.append("8")
                if mouse.colliderect(button9):
                    seconds.append("9")
                if mouse.colliderect(button0):
                    seconds.append("0")
                if mouse.colliderect(start):
                    start_timer()
                if mouse.colliderect(clear):
                    clear_timer()
                    sound.stop()
                if mouse.colliderect(exit_timer):
                    quit_timer()
                if mouse.colliderect(off):
                    alarm_state = "off"
                    print("Alarm", alarm_state)
                if mouse.colliderect(on):
                    alarm_state = "on"
                    print("Alarm", alarm_state)
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        gameDisplay.fill((255, 255, 255))

        # Draw the buttons

        button1 = pygame.draw.rect(gameDisplay, green, Rect((20, 100), (40, 40)))
        gameDisplay.blit(font.render("1", True, (0, 0, 200)), (31, 107.5))

        button2 = pygame.draw.rect(gameDisplay, green, Rect((100, 100), (40, 40)))
        gameDisplay.blit(font.render("2", True, (0, 0, 200)), (111, 107.5))

        button3 = pygame.draw.rect(gameDisplay, green, Rect((180, 100), (40, 40)))
        gameDisplay.blit(font.render("3", True, (0, 0, 200)), (191, 107.5))

        button4 = pygame.draw.rect(gameDisplay, green, Rect((260, 100), (40, 40)))
        gameDisplay.blit(font.render("4", True, (0, 0, 200)), (271, 107.5))

        button5 = pygame.draw.rect(gameDisplay, green, Rect((340, 100), (40, 40)))
        gameDisplay.blit(font.render("5", True, (0, 0, 200)), (351, 107.5))

        button6 = pygame.draw.rect(gameDisplay, green, Rect((20, 260), (40, 40)))
        gameDisplay.blit(font.render("6", True, (0, 0, 200)), (31, 267.5))

        button7 = pygame.draw.rect(gameDisplay, green, Rect((100, 260), (40, 40)))

        gameDisplay.blit(font.render("7", True, (0, 0, 200)), (111, 267.5))

        button8 = pygame.draw.rect(gameDisplay, green, Rect((180, 260), (40, 40)))
        gameDisplay.blit(font.render("8", True, (0, 0, 200)), (191, 267.5))

        button9 = pygame.draw.rect(gameDisplay, green, Rect((260, 260), (40, 40)))
        gameDisplay.blit(font.render("9", True, (0, 0, 200)), (271, 267.5))

        button0 = pygame.draw.rect(gameDisplay, green, Rect((340, 260), (40, 40)))
        gameDisplay.blit(font.render("0", True, (0, 0, 200)), (351, 267.5))

        start = pygame.draw.rect(
            gameDisplay, (230, 200, 0), Rect((110, 170), (180, 60))
        )
        gameDisplay.blit(font.render("Start Timer", True, (100, 50, 50)), (125, 187))

        clear = pygame.draw.rect(gameDisplay, green, Rect((60, 325), (120, 40)))
        gameDisplay.blit(font2.render("Clear Time", True, (0, 0, 200)), (65, 335))

        exit_timer = pygame.draw.rect(gameDisplay, green, Rect((220, 325), (120, 40)))
        gameDisplay.blit(font2.render("Quit Timer", True, (0, 0, 200)), (225, 335))

        display = pygame.draw.rect(
            gameDisplay, (150, 150, 150), Rect((50, 30), (300, 40))
        )

        off = pygame.draw.rect(gameDisplay, (225, 0, 0), Rect((20, 170), (70, 60)))
        gameDisplay.blit(font2.render("Alarm", True, green), (25, 180))
        gameDisplay.blit(font2.render("Off", True, green), (38, 205))

        on = pygame.draw.rect(gameDisplay, (225, 0, 0), Rect((310, 170), (70, 60)))
        gameDisplay.blit(font2.render("Alarm", True, green), (315, 180))
        gameDisplay.blit(font2.render("On", True, green), (330, 205))

        mouse = pygame.draw.rect(gameDisplay, (200, 100, 0), Rect((rectpos), (10, 10)))

        gameDisplay.blit(
            font2.render(("".join(seconds) + " (seconds)"), True, (0, 0, 0)), (60, 40)
        )
        # Tick the Clock
        clock.tick(30)
        # Update the screen
        pygame.display.update()
    except SyntaxError:
        quit()
