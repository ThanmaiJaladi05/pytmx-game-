import pygame

pygame.mixer.init()

# Load sound effects
jump_sound = pygame.mixer.Sound("jump.wav")
coin_sound = pygame.mixer.Sound("coin.wav")

# Load background music
pygame.mixer.music.load("background.mp3")
pygame.mixer.music.play(-1)  # Loop indefinitely
