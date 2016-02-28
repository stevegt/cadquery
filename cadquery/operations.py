"""
	Operations that modify or create 3d solids. 
	(Put another way, things that modify the feature tree )

"""

    def rotateAboutCenter(self, axisEndPoint, angleDegrees):
	
		pass

    def rotate(self, axisStartPoint, axisEndPoint, angleDegrees):
		pass

    def mirror(self, mirrorPlane="XY", basePointVector=(0, 0, 0)):
		pass


    def translate(self, vec):
		pass


    def shell(self, thickness):
		pass

    def fillet(self, radius):
		pass

    def chamfer(self, length, length2=None):
		pass
		
    #but parameter list is different so a simple function pointer wont work
    def cboreHole(self, diameter, cboreDiameter, cboreDepth, depth=None, clean=True):
		pass

    #TODO: almost all code duplicated!
    #but parameter list is different so a simple function pointer wont work
    def cskHole(self, diameter, cskDiameter, cskAngle, depth=None, clean=True):
		pass

    #TODO: almost all code duplicated!
    #but parameter list is different so a simple function pointer wont work
    def hole(self, diameter, depth=None, clean=True):
		pass

    #TODO: duplicated code with _extrude and extrude
    def twistExtrude(self, distance, angleDegrees, combine=True, clean=True):
		pass
		
    def extrude(self, distance, combine=True, clean=True):
		pass

    def revolve(self, angleDegrees=360.0, axisStart=None, axisEnd=None, combine=True, clean=True):
		pass

    def combine(self, clean=True):
		pass

    def union(self, toUnion=None, combine=True, clean=True):
		pass

    def cut(self, toCut, combine=True, clean=True):
		pass

    def cutBlind(self, distanceToCut, clean=True):
		pass
		
    def cutThruAll(self, positive=False, clean=True):
		pass

    def loft(self, filled=True, ruled=False, combine=True):
		pass

    def box(self, length, width, height, centered=(True, True, True), combine=True, clean=True):
		pass

    def sphere(self, radius, direct=(0, 0, 1), angle1=-90, angle2=90, angle3=360,
		pass

    def split(self, keepTop=False, keepBottom=False):
		pass		