#!/usr/bin/python
from PIL import Image
import pygame
from pygame import camera

pygame.camera.init()
cam = pygame.camera.Camera('/dev/video0', (1920, 1080))
cam.start()
for x in range(0, 20):
    img = cam.get_image()
pygame.image.save(img, "picture.png")
