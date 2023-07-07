import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import random

rotation_speed = 2.0
rectangle_color = [1.0, 0.0, 0.0]  # Initial color set to red

def draw_rectangle():
    glBegin(GL_QUADS)
    glColor3f(rectangle_color[0], rectangle_color[1], rectangle_color[2])  # Set color

    # Front face
    glVertex3f(-0.5, -0.5, 0.5)  # Bottom-left vertex
    glVertex3f(0.5, -0.5, 0.5)   # Bottom-right vertex
    glVertex3f(0.5, 0.5, 0.5)    # Top-right vertex
    glVertex3f(-0.5, 0.5, 0.5)   # Top-left vertex

    # Back face
    glVertex3f(-0.5, -0.5, -0.5)  # Bottom-left vertex
    glVertex3f(0.5, -0.5, -0.5)   # Bottom-right vertex
    glVertex3f(0.5, 0.5, -0.5)    # Top-right vertex
    glVertex3f(-0.5, 0.5, -0.5)   # Top-left vertex

    # Left face
    glVertex3f(-0.5, -0.5, 0.5)  # Bottom-back vertex
    glVertex3f(-0.5, -0.5, -0.5)   # Bottom-front vertex
    glVertex3f(-0.5, 0.5, -0.5)    # Top-front vertex
    glVertex3f(-0.5, 0.5, 0.5)   # Top-back vertex

    # Right face
    glVertex3f(0.5, -0.5, 0.5)  # Bottom-back vertex
    glVertex3f(0.5, -0.5, -0.5)   # Bottom-front vertex
    glVertex3f(0.5, 0.5, -0.5)    # Top-front vertex
    glVertex3f(0.5, 0.5, 0.5)   # Top-back vertex

    # Top face
    glVertex3f(-0.5, 0.5, 0.5)  # Front-left vertex
    glVertex3f(0.5, 0.5, 0.5)   # Front-right vertex
    glVertex3f(0.5, 0.5, -0.5)    # Back-right vertex
    glVertex3f(-0.5, 0.5, -0.5)   # Back-left vertex

    # Bottom face
    glVertex3f(-0.5, -0.5, 0.5)  # Front-left vertex
    glVertex3f(0.5, -0.5, 0.5)   # Front-right vertex
    glVertex3f(0.5, -0.5, -0.5)    # Back-right vertex
    glVertex3f(-0.5, -0.5, -0.5)   # Back-left vertex

    glEnd()

def handle_key_input():
    keys = pygame.key.get_pressed()
    if keys[K_LEFT]:
        glRotatef(rotation_speed, 0, 1, 0)
    if keys[K_RIGHT]:
        glRotatef(-rotation_speed, 0, 1, 0)
    if keys[K_UP]:
        glRotatef(rotation_speed, 1, 0, 0)
    if keys[K_DOWN]:
        glRotatef(-rotation_speed, 1, 0, 0)

def handle_mouse_click():
    global rectangle_color
    rectangle_color = [random.random(), random.random(), random.random()]

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)

    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                handle_mouse_click()

        handle_key_input()

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        draw_rectangle()
        pygame.display.flip()
        clock.tick(60)

if __name__ == '__main__':
    main()
