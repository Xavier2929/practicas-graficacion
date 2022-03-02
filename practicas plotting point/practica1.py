#cambiar el color con glClearColor
#PyPoints
#sistemas de coordenadas 

from OpenGL.GL import *
from OpenGL.GLU import*
from OpenGL.GLUT import *
import sys

#ponemos el fondo negro con glClearColor
#el comando gluOrtho2D nos permite usar el sistemas de coordenadas
#gluOrtho(x izquierda, x derecha, y abajo, y arriba)
def init():
    #color gris :o
    glClearColor(0.50,0.50,0.50,1.0)
    gluOrtho2D(-1.0,1.0,-1.0,1.0)
    

  
def plotpoints():
    glClear(GL_COLOR_BUFFER_BIT)
    #coloreamos un punto rojo,  3f indica que usa 3 puntos decimales entre 0 y 1
    glColor3f(1.0, 1.0, 0.0) 
 
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


    
    