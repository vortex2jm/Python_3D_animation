#João Paulo Moura Clevelares

#Importing the necessary modules
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import animation, rc
%matplotlib inline


#=======================================================SETUP===============================================================#

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

graph2.set_xlim(-20,20)
graph2.set_ylim(-20,20)
graph2.set_zlim(-20,20)
#=================================================#0

#Setting containers titles
graph1.set_title("Cristal")
graph2.set_title("A definir")
#=================================================#

#Setting axis lables
graph2.set_zlabel("Eixo Z")
graph1.set_zlabel("Eixo Z")
#=================================================#

#==================================================CREATING OBJECTS AND HOMOGENEOUS COORDINATES MATRIX====================================================#

#=================================================FIRST CONTAINER====================================#

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


#==================================================SECOND CONTAINER===================================#

#Creating an airplane

#Base coordinaates
airplane1 = np.array([
                     [5,-1,0],
                     [5,1,0],
                     [-5,1,0],
                     [-5,-1,0],
                     [5,-1,0],
                     [5,-1,2],
                     [-5,-1,2],
                     [-5,-1,0],
                     [-5,1,0],
                     [-5,1,2],
                     [-5,-1,2],
                     [5,-1,2],
                     [5,1,2],
                     [-5,1,2],
                     [-5,1,0],
                     [5,1,0],
                     [5,1,2],
                     [8,0,1],
                     [5,-1,2],
                     [5,-1,0],
                     [8,0,1],
                     [5,1,0],

])

#Creating homogeneous coordinates matrix
airplane1Points = np.transpose(airplane1)
airplane1Points = np.vstack([airplane1Points,np.ones(np.size(airplane1Points,1))])

#Rear coordinates
airplane2 = np.array([
                      [-5,-1,0],
                      [-5,1,0],
                      [-5,1,2],
                      [-5,-1,2],
                      [-5,-1,0],
                      [-9,0,2],
                      [-5,1,0],
                      [-5,1,2],
                      [-9,0,2],
])

airplane2Points = np.transpose(airplane2)
airplane2Points = np.vstack([airplane2Points,np.ones(np.size(airplane2Points,1))])

#Coordinates from above
airplane3 = np.array([
                      [-5,-0.5,2],
                      [-5,0.5,2],
                      [-8,0.5,2],
                      [-8,-0.5,2],
                      [-5,-0.5,2],
                      [-8,-0.5,4],
                      [-8,-0.5,2],
                      [-8,0.5,2],
                      [-8,0.5,4],
                      [-8,-0.5,4],
                      [-5,-0.5,2],
                      [-5,0.5,2],
                      [-8,0.5,4],
])

airplane3Points = np.transpose(airplane3)
airplane3Points = np.vstack([airplane3Points,np.ones(np.size(airplane3Points,1))])

#Wings coordinates
airplane4 = np.array([
                      [2,1,2],
                      [-2,1,2],
                      [-2,1,1],
                      [2,1,1],
                      [2,1,2],
                      [2,7,2],
                      [-2,9,2],
                      [-2,1,2],
                      [-2,1,1],
                      [-2,9,1],
                      [-2,9,2],
                      [2,7,2],
                      [2,7,1],
                      [-2,9,1],
                      [2,7,1],
                      [2,1,1],
])

#Left wing homogeneous coordinates
airplane4Points = np.transpose(airplane4)
airplane4Points = np.vstack([airplane4Points,np.ones(np.size(airplane4Points,1))])

#Right wing is simetric with left wing on Y axis
airplane5Points = np.transpose(airplane4)
airplane5Points[1,:] = airplane5Points[1,:] * (-1)
airplane5Points = np.vstack([airplane5Points,np.ones(np.size(airplane5Points,1))])


#Creating a new Shape with your own points and center coordinates
AirplaneBase = Shape([0,0,0,1], airplane1Points)
AirplaneBack = Shape([0,0,0,1], airplane2Points)
AirplaneUp = Shape([0,0,0,1], airplane3Points)
AirplaneWingLeft = Shape([0,0,0,1], airplane4Points)
AirplaneWingRight = Shape([0,0,0,1], airplane5Points)

#Listing objects to be drawned
obj3, = graph2.plot3D([],[],[],lw=2, color = "orange") #base
obj4, = graph2.plot3D([],[],[],lw=2, color = "orange") #rear
obj5, = graph2.plot3D([],[],[],lw=2, color = "orange") #up
obj6, = graph2.plot3D([],[],[],lw=2, color = "orange") #left wing
obj7, = graph2.plot3D([],[],[],lw=2, color = "orange") #right wing

#===============================================================ANIMATING=====================================================#

def animate(i):

  #=====RED CRYSTAL=======================================#

  #Rotating around your own axis
  Tmatrix = translate(Crystal.center[0],Crystal.center[1],Crystal.center[2]) @ rotate('z',-15*i) @ translate(-Crystal.center[0],-Crystal.center[1],-Crystal.center[2])
  #Rotating around Z axis and translating 2 units in Y axis
  Tmatrix2 = rotate('z',4*i) @ translate(0,2,0) @ Tmatrix
  #Translating in sinusoid on Z axis
  Tmatrix3 = translate(0,0,0.8*np.sin(0.3*i)) @ Tmatrix2


  #Final matrix
  Rmatrix = Tmatrix3 @ Crystal.points
  #Setting red crystal coordinates
  obj1.set_data(Rmatrix[0,:], Rmatrix[1,:])
  obj1.set_3d_properties(Rmatrix[2,:])

  #=====BLUE CRYSTAL======================================#

  #Translating blue crystal to center on X and Y axis && translating in sinusoid on Z axis
  T2matrix = translate(0,0,0.8*np.sin(-0.3*i)) @ translate(-Crystal.center[0],-Crystal.center[1],-Crystal.center[2])
  #Rotating around Z axis
  T2matrix2 = rotate('z',15*i) @ T2matrix

  #Final matrix
  R2matrix = T2matrix2 @ Crystal.points
  #Setting blue crystal coordinates
  obj2.set_data(R2matrix[0,:],R2matrix[1,:])
  obj2.set_3d_properties(R2matrix[2,:])


  #===================================AIRPLANE==============================================#

  #Transformation matrix -> translating -15 on Y axis, rotating 30 degrees around X axis and finally, but no less important, rotating around Z axis
  TransMatrix = rotate('z', 10 * i) @ rotate('x',-30) @ translate(0,-15,0) 

  #Below we have final matrices for all airplane parts
  Base = TransMatrix @ AirplaneBase.points
  Back = TransMatrix @ AirplaneBack.points
  Up = TransMatrix @ AirplaneUp.points
  LeftWing = TransMatrix @ AirplaneWingLeft.points
  RightWing = TransMatrix @ AirplaneWingRight.points

  #and here we're setting the plotting according to the iteration
  obj3.set_data(Base[0,:], Base[1,:])
  obj3.set_3d_properties(Base[2,:])

  obj4.set_data(Back[0,:], Back[1,:])
  obj4.set_3d_properties(Back[2,:])

  obj5.set_data(Up[0,:], Up[1,:])
  obj5.set_3d_properties(Up[2,:])

  obj6.set_data(LeftWing[0,:], LeftWing[1,:])
  obj6.set_3d_properties(LeftWing[2,:])

  obj7.set_data(RightWing[0,:], RightWing[1,:])
  obj7.set_3d_properties(RightWing[2,:])

  return (obj1, obj2, obj3, obj4, obj5, obj6, obj7)

#animate function
anim = animation.FuncAnimation(fig,animate, init_func= None, frames=100, interval=100, blit=True)

rc('animation', html='jshtml')
anim