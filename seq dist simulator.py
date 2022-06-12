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

#ddraw([0.1, 0.4,0.5]) # cdf = .1, .5, 1, its the cum dist
print(E)
for i in range(10):
    print(i,ddraw(E),sep=' - ') # generate a sequence of discrete random variables with dist of E