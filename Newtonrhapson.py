def newton(fun,grad,x0,tol=1e-6,maxiter=100,callback=None):
    '''Newton method for solving equation f(x) = 0, with given tolerance and number of
    iterations, callback function is invoked at each itertion if given'''
    for i in range(maxiter):
        x1=x0-fun(x0)/grad(x0)
        err= abs(x1-x0)
        if callback!= None:
            callback(iter=i,err=err,x0=x0,x1=x1,fun=fun)
        if err< tol: break
        x0=x1
    else:
        raise RuntimeError('Failed to converge in %d iterations'%maxiter)
    return x1

f= lambda x: -4*x**3+5*x+1
g= lambda x: -12*x**2+5
x= newton(f,g,x0=-2.5,maxiter=7)
print('Solution is x= %1.3f, f(x)=%1.12f' %(x,f(x)))
#newton fails when multiple solutions