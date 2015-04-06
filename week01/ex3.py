h = 800 # height in meter

g = 9.81 # gravity aaceleration

#vi = input("enter initial velocity=") #initial velocity

vmin = input("enter minimum velocity=")

vmax = input("enter maximum velocity=") 

dx = ( vmax -vmin )/9

s = (  vmin  + (( vmin )**2 + 2*g*h)**0.5 )/g

print " time for minimum velocity is+" , s
  
i= 0

while i<9:
    vmin = vmin + dx
     
    i = i + 1 
    print " velocity=" , vmin
    
    t = (  vmin  + (( vmin )**2 + 2*g*h)**0.5 )/g

    print "time of flight is=" , t

