from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from numpy import *
import sys

def init():
    glClearColor(1.0, 1.0, 1.0, 1.0) 
    gluOrtho2D(-5.0, 5.0, -5.0, 5.0) 
    
    
def plotFunc():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0,0,0)
    glPointSize(3)
    drawLines()
    
    for x in arange(-5,5,0.1):
   
     y=x**3-3*x-1
     glBegin(GL_POINTS)
     glVertex2f(x,y)
     glEnd() 
     glFlush()
     drawLines()
     
def drawLines():
   #esta funcion dibuja el plano cartesiano de color negro
    
    glBegin(GL_LINES) 
    glVertex2f(-5.0, 0.0) 
    glVertex2f(5.0, 0.0) 
    glVertex2f(0.0, 5.0) 
    glVertex2f(0.0, -5.0) 
    glEnd()
   
    

    

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
    glutInitWindowPosition(50,50)
    glutCreateWindow("Inciso b)y=x^3-3x-1")
    glutDisplayFunc(plotFunc)
    
    
    init()
    glutMainLoop()
    
main()
