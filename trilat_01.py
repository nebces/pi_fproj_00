#import matplotlib.pyplot as plt
from math import sqrt

def intersection(x1, y1, r1, x2, y2, r2,d,m,n) : #for non itersectin circles and touching
    x,y = (m*x2 + n *x1)/(m+n) ,(m*y2 + n *y1)/(m+n)
    return x,y


def get_values(x0, y0, r0, x1, y1, r1):
    # circle 1: (x0, y0), radius r0
    # circle 2: (x1, y1), radius r1

    d=sqrt((x1-x0)**2 + (y1-y0)**2)

    # non intersecting
    if d >= r0 + r1 :
        # print("non intersectin")
        m = r0 + (d - (r0 + r1))/2
        n = d - m
        x,y = intersection(x0, y0, r0, x1, y1, r1,d,m,n)
        if (x> 0 and  y>0):
            return (x,y)
        else :
        # print("negative",x,y,x0,y0,r0,x1,y1,r1)
            return -100
    # One circle within other
    if d < abs(r0-r1):
        m,n = r0 ,r1
        x,y = intersection(x0, y0, r0, x1, y1, r1,d,m,n)
        if x> 0 and  y>0:
            return (x,y)
        else :
            # print("negative",x,y,x0,y0,r0,x1,y1,r1)
            return -100
    # coincident circles
    if d == 0 and r0 == r1:
        # print("the impossible : coincident circle")
        return -100
    else:
        a=(r0**2-r1**2+d**2)/(2*d)
        h=sqrt(r0**2-a**2)
        x2=x0+a*(x1-x0)/d
        y2=y0+a*(y1-y0)/d
        x3=x2+h*(y1-y0)/d
        y3=y2-h*(x1-x0)/d

        x4=x2-h*(y1-y0)/d
        y4=y2+h*(x1-x0)/d
        
        if ((x3 >0 and y3> 0) and ( x4 >0 and y4>0)):
            return ((x3,y3),(x4,y4))
        elif (x4 <0 or y4 <0 )and (x3 >0 and y3 >0):
            return (x3,y3)
        elif (x3 <0 or y3 <0) and (x4>0 and y4 >0):
            return (x4, y4)
        else:
            # print("all negatives")
            return -100

#print(get_values(1,2,5,3,4,5))

def get_location(locs):   # get list of 3 x,y,distance
    tri_coor = []
    last = len(locs) -1
    
    for pres in locs:
        #print(pres)    
        prev = locs[last]
        last +=1
        if last == len(locs):
            last =0
        values = get_values(pres[0],pres[1],pres[2],prev[0],prev[1],prev[2])
        if values != -100 and type(values[0]) ==tuple:
            tri_coor.append(values[0])
            tri_coor.append(values[1])
            # print(type(values))
        elif values !=-100:
            tri_coor.append(values)
    return tri_coor

def pt_loc(locs):
    x,y = [],[]
    l =len(locs)
    for pres in locs:
        # print(pres)
        y.append(pres[1])
        x.append(pres[0])
    # print(x,y)
    x_c,y_c = sum(x)/l ,sum(y)/l
    return(x_c, y_c)
print(pt_loc(get_location([[0,0,3],[8,8,4],[4,4,6]])))
