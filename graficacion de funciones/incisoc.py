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
    glPointSize(2)
    drawLines()
    
    for x in arange(-2,2,0.01):
   
     y=x**4-5*x**3+x**2-3*x-1
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
    glutInitWindowPosition(100,100)
    glutInitWindowSize(500,500)
    glutCreateWindow("Inciso c)y=x^4-5x^3+x^2-3x-1")
    glutDisplayFunc(plotFunc)
    
    
    init()
    glutMainLoop()
    
main()
