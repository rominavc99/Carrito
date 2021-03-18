from OpenGL.GL import *
from glew_wish import *
import glfw

class Obstaculo:

    posicionX = 0.0
    posicionY = 0.6
    vivo = True

    def __init__(self, x, y):
        
        self.posicionX = x
        self.posicionX = y

    def dibujar(self):

        if self.vivo:
            glPushMatrix()
            glTranslate(self.posicionX, self.posicionY, 0.0)
            glBegin(GL_QUADS)
            glColor3f(0.0, 0.0, 1.0)
            glVertex(-0.15, 0.15, 0.0)
            glVertex(0.15, 0.15, 0.0)
            glVertex(0.15, -0.15, 0.0)
            glVertex(-0.15, -0.15, 0.0)
            glEnd()
            glPopMatrix()