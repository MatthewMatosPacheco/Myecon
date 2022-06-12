import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline
plt.rcParams['figure.figsize'] = [12, 8]
np.seterr(all=None, divide='ignore', over=None, under=None, invalid='ignore')  # turn off sqrt(-1) warning

def supply(p):
    '''Vectorized function to compute supply'''
    const = 5*np.arange(10)  # cost thresholds
    p = np.asarray(p).reshape((1,-1))  # row vector
    s = np.kron(np.ones((const.size,1)),p)  # repeat rows
    for i,c in enumerate(const):
        s[i,:] = np.log(s[i,:]*.2-c)+c+3  # separate transform for each row
    return np.nanmax(s,axis=0)

def demand(p):
    '''Vectorized function to compute demand'''
    res = np.asarray(100/p + 1/(1+np.exp(p-75))
                           + 2/(1+np.exp(p-50))
                           + 3/(1+np.exp(p-25)))
    res[res>20] = np.nan  # avoid large numbers for plots
    return res

def plotline(fun,lbl=None,ax=None,**kwargs):
    # quick plotting function on given axis
    if ax==None:
        ax = plt.axes()
    pr = np.linspace(0,100,1000)
    ax.plot(fun(pr),pr,**kwargs)
    if lbl:
        ax.text(fun(60)+1,60,lbl,fontsize=12)
    ax.set_xlabel('Quantity')
    ax.set_ylabel('Price')
    return ax

ax = plotline(demand,lbl='Demand',c='b')
plotline(supply,lbl='Supply',c='r',ax=ax)
plt.show()
