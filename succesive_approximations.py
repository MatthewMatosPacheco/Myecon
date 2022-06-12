import numpy as np
eq= lambda x: -np.exp(-(x-2)**2)+.5#initial equations
F = lambda x:x -np.exp(-(x-2)**2)+.5#fixed point equation
df= lambda X: 1+np.exp(-(x-2)**2)*2*(x-2)# derivative
def solve_sa(F,x0,tol=1e-6,maxiter=100,callback=None): # maximiter max number of iteration
    '''Computes the solution of fixed point equation x =F(x) with given initial value
    x0 and algorithm parameters. Method: succesive approximations'''



    for i in range(maxiter):
        x1=F(x0)#update aproximation
        err = np.amax(np.abs(x0-x1))# allow for x to be array
        if callback != None:
            callback(iter=i,err=err,x=x1,x0=x0)
        if err < tol:
            break#break if converged( found what we wanted)
        x0=x1# ready for next iter
    else:
        raise RuntimeError('failed to converge in %d iterations' % maxiter)
    return x1
#def printme(**kwargs):
    print('iter=%d,x0=%1.10f (err=%1.3e'%(kwargs['iter'],kwargs['x'],kwargs['err']))
#x= solve_sa(F,x0=1.0,tol=1e-10,callback=printme)# starting value changes maount of iter
#print('residual in the original equation %1.5e'%eq(x))
