#Importing the necessary modules
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import animation, rc
%matplotlib inline

#Creating shape class to objects
class Shape():
  def __init__(self,center=[],points=[]):
    self.center = center
    self.points = points
#=================================================#

#Creating translating matrix function
def translate(dx,dy,dz):
  translated = np.array([[1,0,0,dx],[0,1,0,dy],[0,0,1,dz],[0,0,0,1]])
  return translated
#=================================================#

#Creating rotating matrix function
def rotate(axis, angle):
  radAngle = (angle/180)*np.pi

  if axis == 'x':
    rotated = np.array([[1,0,0,0],[0,np.cos(radAngle),-np.sin(radAngle),0],[0,np.sin(radAngle),np.cos(radAngle),0],[0,0,0,1]])
  elif axis == 'y':
    rotated = np.array([[np.cos(radAngle),0,np.sin(radAngle),0],[0,1,0,0],[-np.sin(radAngle),0,np.cos(radAngle),0],[0,0,0,1]])
  elif axis == 'z':
    rotated = np.array([[np.cos(radAngle),-np.sin(radAngle),0,0],[np.sin(radAngle),np.cos(radAngle),0,0],[0,0,1,0],[0,0,0,1]])
  else:
    rotated = np.eye(4,4)

  return rotated
#=================================================#

#Creating containers
fig = plt.figure(figsize=[20,10])
graph1 = fig.add_subplot(1,2,1,projection='3d')
graph2 = fig.add_subplot(1,2,2,projection='3d')
plt.close()
#=================================================#

#Setting axis limits
graph1.set_xlim(-3,3)
graph1.set_ylim(-3,3)
graph1.set_zlim(-3,3)

graph2.set_xlim(-3,3)
graph2.set_ylim(-3,3)
graph2.set_zlim(-3,3)
#================================================0=#0

#Setting containers titles
graph1.set_title("Cristal")
graph2.set_title("A definir")
#=================================================#

#Setting axis lables
graph2.set_zlabel("Eixo Z")
graph1.set_zlabel("Eixo Z")
#=================================================#


#Creating a cristal
crystalPoints = np.array([
                [0,0,0],
                [0,1,0],
                [0.5,0.5,1],
                [0,0,0],
                [0.5,0.5,-1],
                [0,1,0],
                [0.5,0.5,1],
                [1,1,0],
                [0.5,0.5,-1],
                [0,1,0],
                [1,1,0],
                [0.5,0.5,1],
                [1,0,0],
                [0.5,0.5,-1],
                [1,1,0],
                [1,0,0], 
                [0.5,0.5,1],
                [0,0,0],
                [0.5,0.5,-1],
                [1,0,0],
                [0,0,0] 
                ])

#Creating homogeneous coordinates matrix
crystalPoints = np.transpose(crystalPoints)
crystalPoints = np.vstack([crystalPoints,np.ones(np.size(crystalPoints,1))])

#Creating a new Shape with your own points and center coordinates
Crystal = Shape([0.5,0.5,0,1], crystalPoints)

#Listing objects to be drawned
obj1, = graph1.plot3D([],[],[], lw=2, color="red")
obj2, = graph1.plot3D([],[],[], "--",lw=2) 


def init():

  obj2.set_data(Crystal.points[0,:], Crystal.points[1,:])
  obj2.set_3d_properties(Crystal.points[2,:])

  return (obj2,)


def animate(i):

  #=====RED CRYSTAL=======================================#

  #Rotating around your own axis
  Tmatrix = translate(Crystal.center[0],Crystal.center[1],Crystal.center[2]) @ rotate('z',-15*i) @ translate(-Crystal.center[0],-Crystal.center[1],-Crystal.center[2])
  #Rotating around Z axis and translating 2 units in Y axis
  Tmatrix2 = rotate('z',4*i) @ translate(0,2,0) @ Tmatrix
  #Translating in sinusoid on Z axis
  Tmatrix3 = translate(0,0,0.8*np.sin(0.3*i)) @ Tmatrix2
  #Resulted matrix of operations
  Rmatrix = Tmatrix3 @ Crystal.points
  #Setting red crystal coordinates
  obj1.set_data(Rmatrix[0,:], Rmatrix[1,:])
  obj1.set_3d_properties(Rmatrix[2,:])

  #=====BLUE CRYSTAL======================================#

  #Translating blue crystal to center on X and Y axis && translating in sinusoid on Z axis
  T2matrix = translate(0,0,0.8*np.sin(-0.3*i)) @ translate(-Crystal.center[0],-Crystal.center[1],-Crystal.center[2])
  #Rotating around Z axis
  T2matrix2 = rotate('z',15*i) @ T2matrix
  #Resulted matrix of operations
  R2matrix = T2matrix2 @ Crystal.points
  #Setting blue crystal coordinates
  obj2.set_data(R2matrix[0,:],R2matrix[1,:])
  obj2.set_3d_properties(R2matrix[2,:])

  return (obj1, obj2,)


anim = animation.FuncAnimation(fig,animate, init_func= None, frames=100, interval=100, blit=True)

rc('animation', html='jshtml')
anim