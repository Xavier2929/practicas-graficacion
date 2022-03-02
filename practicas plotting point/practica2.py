#Change the color of the pixel(s) in the glColor3f statement. Try plotting a 
#white pixel using (1.0, 1.0, 1.0).

from OpenGL.GL import *
from OpenGL.GLU import*
from OpenGL.GLUT import *
import sys
def init():
    #color gris :o
    glClearColor(0.50,0.50,0.50,1.0)
    gluOrtho2D(-1.0,1.0,-1.0,1.0)
    

  
def plotpoints():
    glClear(GL_COLOR_BUFFER_BIT)
    #coloreamos un punto rojo,  3f indica que usa 3 puntos decimales entre 0 y 1
    glColor3f(0.99,0.88,0.22) 
 
 #glBegin indica que vamos a empezar a dibujar
    glBegin(GL_POINTS) 
    glVertex2f(0.0, 0.0) 
    
    glEnd()
    glFlush()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
    glutInitWindowSize(500,500)
    glutCreateWindow("Coordenadas")
    glutDisplayFunc(plotpoints)
    
    init()
    glutMainLoop()
    
main()  
