#Computation of  2D random walk via Monte Carlo Method

from Pawan_Random_Walk import Two_Dimentonal_Random_Walk

Estimated_Distance = 0
Estimated_Direction=''
Number_Southwest = 0
Percetage_Southwest= 0

for i in range(1, 20000):
	Estimated_Distance,Estimated_Direction = Two_Dimentonal_Random_Walk(25)
	if Estimated_Direction == 'Southwest':
		Number_Southwest = Number_Southwest + 1
	
Percetage_Southwest = (Number_Southwest / 20000 ) * 100

print('The percetage of stoppages in Southwest is:  '+str(Percetage_Southwest)) 