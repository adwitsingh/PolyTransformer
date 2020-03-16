# CSE 101 - IP HW4
# 2D Transformations of Geometric objects 
# Name: ADWIT SINGH KOCHAR

import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, Ellipse
from math import sin, cos, radians, sqrt
from copy import deepcopy

def matrix_Multiplication(matrix1, matrix2):
	"""
	Multiplies two matrices matrix1(r1 x c1) and matrix2(r2 x c2).

	Args:
		matrix1: First matrix of dimension (r1 x c1)
		matrix2: Second matrix of dimension (r2 x c2)

	Precondition:
		c1 = r2

	Returns:
		A matrix of dimensions (r1 x c2)

	"""
	r1 = len(matrix1)
	c1 = len(matrix1[0])

	r2 = len(matrix2)
	c2 = len(matrix2[0])

	if  c1 != r2:
		raise Exception("ERROR: Matrices cannot be multiplied")				# Matrices not multiplication compatible

	resultantMatrix = []

	for i in range(r1):
		row = []
		for j in range(c2):
			sumElements = 0
			for k in range(c1):
				sumElements += matrix1[i][k] * matrix2[k][j]
			row.append(round(sumElements, 3))
		resultantMatrix.append(row)

	return resultantMatrix

def Distance(x1, y1, x2, y2):
	"""
	Calculates distance between points (x1, y1) and (x2, y1).

	Args:
		x1, y1: coordinates of point one
		x2, y2: coordinates of point two

	Returns:
		Distance of float type

	"""
	dist = round(sqrt((x1 - x2)**2 + (y1 - y2)**2), 3)
	return dist
 

def Scaling(Sx, Sy, points):
	"""
	Performs the transformation "Scaling".

	Args:
		Sx: Scaling factor along x-axis
		Sy: Scaling factor along y-axis
		points: Matrix of points to be scaled
	
	Returns:
		Matrix of scaled points. 

	"""
	factorMatrix = [[Sx, 0, 0], [0, Sy, 0], [0, 0, 1]]					# Standard matrix for scaling
	return matrix_Multiplication(factorMatrix, points)


def Rotation(angle_degrees, points):
	"""
	Performs the transformation "Rotation".

	Args:
		angle_degrees: Angle of rotation in degrees
		points: Matrix of points to be rotated
	
	Returns:
		Matrix of rotated points. 

	"""
	angle_radians = radians(angle_degrees)
	sin_angle = round(sin(angle_radians), 3)
	cos_angle = round(cos(angle_radians), 3)

	factorMatrix = [[cos_angle, -sin_angle, 0], [sin_angle, cos_angle, 0], [0, 0, 1]]		# Standard matrix for rotation
	return matrix_Multiplication(factorMatrix, points)


def Translation(Tx, Ty, points):
	"""
	Performs the transformation "Translation".

	Args:
		Tx: Distance to move along x-axis
		Ty: Distance to move along y-axis
		points: Matrix of points to be translated
	
	Returns:
		Matrix of translated points. 

	"""
	factorMatrix = [[1, 0, Tx], [0, 1, Ty], [0, 0, 1]]						# Standard matrix for translation
	return matrix_Multiplication(factorMatrix, points)


def drawShape(points):
	"""
	Draws a polygon with the given vertices using matplotlib.pyplot

	Args:
		points: Matrix of coordinates of vertices

	"""
	vertices = []
	for i in range(len(points[0])):
		vertices.append([points[0][i],points[1][i]])				# Creates a list of coordinates of vertices as [x,y]

	plt.clf()
	polygon = Polygon(vertices)
	plt.gca().add_patch(polygon)
	plt.axis('scaled')
	plt.show()


def Transformation(points, shape):
	"""
	Takes coordinates of the polygon/disc and performs the transformations that are input
	
	"""
	
	input_command = input()

	while(input_command != "quit"):
		if input_command[0] == "S":									# Scaling the polygon/disc
			Sx = float(input_command.split()[1])
			Sy = float(input_command.split()[2])
			points = Scaling(Sx, Sy, points)
		
		elif input_command[0] == "R":								# Rotating the polygon/disc 
			angle_degrees = float(input_command.split()[1])
			points = Rotation(angle_degrees, points)

		elif input_command[0] == "T":								# Translating the polygon/disc
			Tx = float(input_command.split()[1])
			Ty = float(input_command.split()[2])
			points = Translation(Tx, Ty, points)

			
		if shape == 'polygon':
			drawShape(points)

			for i in points[0]:
				print(i, end=" ")										# Prints the new x coordinates
			print()
			for i in points[1]:
				print(i, end=" ")										# Prints the new y coordinates
			print()

		else:
			drawShape([i[:-1] for i in points])							# Plots the ellipse by removing the centre
																		# from the list of vertices

			radius1 = Distance(points[0][0], points[1][0], points[0][-1], points[1][-1])
			radius2 = Distance(points[0][90], points[1][90], points[0][-1], points[1][-1])
			print( points[0][-1], points[1][-1], radius1, radius2)							# prints centre_x, centre_y, radius1, radius2

		input_command = input()


#### Main driver code ####

while True:														# Loop runs until user enters polygon / disc											
	shape = input()
	if shape == "polygon":
		x = list(map(int, input().split()))
		y = list(map(int, input().split()))
		
		points = [x, y, []]
		for i in range(len(x)):
			points[2].append(1)										# Creates a matrix with columns as [x, y, 1]

		plt.ion()													# Makes the plot interactive
		drawShape(points)											# Plots the initial polygon
		Transformation(points, 'polygon')
		break

	elif shape == "disc":
		centre_x,centre_y,radius = map(int, input().split())

		points = [[], [], []]

		for i in range(0,360):													# Creates coordinates of disc and appends them
			points[0].append(centre_x + radius*(round(cos(radians(i)), 3)) )	# as columns [x, y, 1] in matrix points
			points[1].append(centre_y + radius*(round(sin(radians(i)), 3)) )
			points[2].append(1)

		points[0].append(centre_x)									# Attaches the coordinates of the centre of disc
		points[1].append(centre_y)
		points[2].append(1)

		plt.ion()													# Makes the plot interactive
		drawShape([i[:-1] for i in points])							# Plots the initial disc by removing the coordinates of centre
		Transformation(points, 'disc')
		break

	else:
		print("ERROR: Enter polygon or disc")
