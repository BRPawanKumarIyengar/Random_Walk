#we import random module to generate random values
import random


#To generate one dimentional random movement (in a line)
def One_Dimentional_Random_Walk(Number_Of_Steps):
	x = 0
	Direction_Of_Walk = 'Right'
	for Ctr in range(1, (Number_Of_Steps + 1)):
		Walk = random.choice(['Right','Left'])
		if Walk == 'Right':
			x = x + 1
		else:
			x = x - 1
	if x < 0:
		Direction_Of_Walk ='Left'
	return(x,Direction_Of_Walk)

	
#To generate two dimentional random movement (in a plane)	
def Two_Dimentonal_Random_Walk(Number_Of_Steps):
	x = 0
	y = 0
	Direction_Of_Walk ='Northeast'
	for Ctr in range(1,(Number_Of_Steps + 1)):
		(Walk_X,Walk_Y) = random.choice([(0,1),(0,-1),(1,0),(-1,0)])
		x = x + Walk_X
		y = y + Walk_Y
		
	if x < 0 and y < 0:
		Direction_Of_Walk ='Southwest'
	elif x> 0 and y < 0:
		Direction_Of_Walk ='Southeast'
	elif x < 0 and y > 0:
		Direction_Of_Walk = 'Northwest'
	else:
		Direction_Of_Walk ='Northeast'
	
	Total_Distance = abs(x) + abs(y)	
	return(Total_Distance,Direction_Of_Walk)
	
	
	
#To genrate three dimentional random movement (in space)
def Three_Dimentonal_Random_Walk(Number_Of_Steps):
	x = 0
	y = 0
	z = 0
	for Ctr in range(1,(Number_Of_Steps + 1)):
		(Walk_X,Walk_Y, Walk_Z) = random.choice([(0,1,0),(0,-1,0),(1,0,0),(-1,0,0),(0,0,1),(0,0,-1)])
		x = x + Walk_X
		y = y + Walk_Y
		z = z + Walk_Z
	
	Total_Distance = abs(x) + abs(y) +abs(z)
	return(Total_Distance,x,y,z)
	


	