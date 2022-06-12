#comp econ 20
import numpy as np
P= np.array([[.5,.4,.1],[.4,.5,.1],[.2,.2,.6]])
E= np.array([0.2,0.3,0.5]) #random dist of init values
#print(P,E,sep='\n\n')#sep= seperate

def ddraw(probs):
    '''draws one realization of discrete random variables
    generated from given probability dist(base 0)'''
    probs= np.array(probs)
    assert probs.ndim == 1 #expecting a one dim array of probabilities
    assert np.abs(probs.sum()-1)<1**(-10)#passed prob do not sum up to one
    cdf= np.cumsum(probs)#cumulative dist
    u= np.random.uniform()#uniform(0,1)
    # print(cdf)
    for i in range(cdf.size):
        if u<=cdf[i]:
            return i# between i-1 and i values of cdf


def simmc(P,E,T=100):
    '''Simulates Markov chain with fiven transition probabiloty matrix(P),
    inititial state distribution(E) for a given number T of steps (time periods)'''
    P= np.asarray(P)#convert to numpy array
    E= np.asarray(E)
    assert np.all(np.abs(P.sum(axis=1)-1)<1**(-10))# Passed P is not stochastic matrix( check if P is stochastic matrix
    # absolute value will be vector if sum of it < .00000000001 it is 100% else p != stoch matrix
    m=E.size#number of states in the chain,( values this chain can take
    #simulate the initial state
    X= np.empty(T, dtype=int)#allocate space for the simulated values (efficiency reasons) dtype=data type integer
    X[0]= ddraw(E)#initial values in first column
    #main loop over time
    for t in range (1,T):
        X[t]= ddraw(P[X[t-1],:])#simulate using appropriate row
    return X
# how to find stationnary distribution ( identity matrix)
E= np.array([1,0,0])
print('Transition matrix:',P,sep='\n')
for t in range(50):
    E=E@P
    print('after step %2d the distribution is %r'%(t+1,E))