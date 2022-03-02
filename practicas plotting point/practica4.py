#dibuja varios puntos de varios tamaños y colores
#con el gomando glVertex2f entre glBegin y glEnd
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
    glColor3f(0,0,0) 
    glPointSize(4)
 #glBegin indica que vamos a empezar a dibujar
    x=0
    y=0
    glBegin(GL_POINTS) 
    for i in range(5):
        
          glVertex2f(x, y)
          x+=0.2
          y+=0.2
  
    
    
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

