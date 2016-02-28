"""
	A workplane in 3d space. 
	Used as a reference to create 2d geometry that will become 3d features through the use
	of an operation
"""
class Workplane(object):

    FOR_CONSTRUCTION = 'ForConstruction'

    def __init__(self, inPlane, origin=(0, 0, 0), obj=None):
		pass

    def transformed(self, rotate=(0, 0, 0), offset=(0, 0, 0)):
		pass

    def rarray(self, xSpacing, ySpacing, xCount, yCount, center=True):
		pass

    def pushPoints(self, pntList):
		pass

    def center(self, x, y):
		pass

    def lineTo(self, x, y, forConstruction=False):
		pass

    def line(self, xDist, yDist, forConstruction=False):
		pass

    def vLine(self, distance, forConstruction=False):
		pass

    def hLine(self, distance, forConstruction=False):
		pass

    def vLineTo(self, yCoord, forConstruction=False):
		pass

    def hLineTo(self, xCoord, forConstruction=False):
		pass

    def moveTo(self, x=0, y=0):
		pass

    def move(self, xDist=0, yDist=0):
		pass

    def spline(self, listOfXYTuple, forConstruction=False):
		pass

    def threePointArc(self, point1, point2, forConstruction=False):
		pass

    def rotateAndCopy(self, matrix):
		pass

    def mirrorY(self):
		pass

    def mirrorX(self):
		pass

    def each(self, callBackFunction, useLocalCoordinates=False):
		pass

    def eachpoint(self, callbackFunction, useLocalCoordinates=False):
		pass

    def rect(self, xLen, yLen, centered=True, forConstruction=False):
		pass

    #circle from current point
    def circle(self, radius, forConstruction=False):
		pass

    def polygon(self, nSides, diameter, forConstruction=False):
		pass

    def polyline(self, listOfXYTuple, forConstruction=False):
		pass

	def text(self, text ):
		pass