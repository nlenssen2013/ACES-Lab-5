tempsC=range(0,60,10)
print "temperatures: "
print tempsC
print "The number of items in the Temp list is %d" %len(tempsC)
print "The index of temperate 30 is %d" %tempsC.index(30)
tempsC.extend([60])
print "temperatures: "
print tempsC

tempsF = [0]*len(tempsC)

for i in range(0,len(tempsC)):
    tempsF[i]=tempsC[i]*9/5+32
          
print tempsF

