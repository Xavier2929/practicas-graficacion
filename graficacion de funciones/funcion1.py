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
    
    #la propiedad arange viene de numpy , lo que quiere decir que x va a ser un numero de -5 hasta 5 incrementando cada vez en 0.1
    for x in arange(-5,5,0.1):
    #la funcion que graficaremos es de y=x^2, una parabola
     y=x*x
     glBegin(GL_POINTS)
     glVertex2f(x,y)
     glEnd() 
     #glflush sirve para mostrar lo hecho previamente en la pantalla, sin esto, simplemente tendriamos una pantalla en negro
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
    #en este caso no utilizariamos glflush ya que se borraria la funcion y se sobrepondria las lineas
    #glFlush()
    

    

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
    glutInitWindowPosition(50,50)
    glutCreateWindow("Funcion #1")
    glutDisplayFunc(plotFunc)
    
    
    init()
    glutMainLoop()
    
main()

#esto es parte de la practica del libro de Python programming in OpenGL (A graphical approach to programming) por Stan Blank
    