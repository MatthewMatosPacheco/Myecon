import numpy as np


f =lambda x: (-x**4)+2.5*x**2+x+10
critical_values=[-1.0,0.5-(1/np.sqrt(2)),0.5+(1/np.sqrt(2))]

#optimization throught discretization
def grid_search(fun,bounds=(0,1),ngrid=10):
    '''Grid search between given bounds over given number of points'''
    grid =np.linspace(*bounds,ngrid)# added a * before bounds to convert tupple to argument(** for dict-> argument)
    func=fun(grid)#lin space prodcues grid between the bounds where func evalute func in all points of the grid
    i = np.argmax(func)#index of the element attaining maximum
    return grid[i]

b0,b1=-2,2 #bounds of region search
xs= grid_search(fun=f,bounds=(b0,b1),ngrid=10)
#xs= grid_search(f,ngrid=10)
cr= critical_values[np.argmin(np.abs(critical_values-xs))]
#print(xs)
print('Grid search returned x=%1.5f (closest to critical point %1.5f, diff =%1.3e'%(xs,cr,np.abs(xs-cr)))