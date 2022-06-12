import numpy as np
P= np.array([[.5,.3,.2],[.5,.4,.1],[.1,.1,.8]])
E= np.array([1,0,0])
def stationary_sa(P,F,tol=1e-6,maxiter=100,callback=None): # maximiter max number of iteration
    '''Compute stationary distribution for markov chain given by transprob matrix P
    , with given maximum number of iterations, and convergence tolerance.
    callback function is called at each iteration if given.
    Method: succesive approximations'''
    P=np.asarray(P)
    F=np.asarray(F)
    assert np.abs(F.sum()- 1) < 1 ** (-10)  # passed prob do not sum up to one
    assert np.all(np.abs(P.sum(axis=1)-1)<1 ** (-10))

    for i in range(100):
        E= F @ P
        print(E)
        err = np.amax(np.abs(E-F))# cuz their vectors, amax = max of abs array
        if callback != None:callback(err=err,E=E,F=F,iter=i)
        if err < tol:break
        F=E
    else:
        raise RuntimeError('failed to converge in %d iterations' % maxiter)
    return E

#print(stationary_sa(P,E))
def printiter(**kwarg):
    print('iter=%d current E=%r'%(kwarg['iter'],kwarg['E']))
sm=stationary_sa(P,E,tol=1e-10,callback=printiter)#(approximation solver
# for linear alg way of doing watch compecon 21