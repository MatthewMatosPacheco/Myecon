import numpy as np
from CompEcon.compecon22.succesive_approximations import *
'''M= products,i=1,2,3...m
n= mass of n types of consumers with diff (j) pref
Pj = fractions of consumer types in pop j=1,2,3...n
Uij= Utlity function of consumer of type j 1->n, from product i 1-> m
Uij= Cij + Si
Cij = valuation of each product by each consumer type
Si = market shares of each product,( increase in U when more peopole on the platform
TOTAL Uij= TUij= Uij + E[i]
E[i]= vector of random compenent of utility(why users prefer that platform)'''
'''Pij= (exp(uij-a(alpha))/SUMof exp(uij-a(alpha) # we take of alpha so it dosent get to big
   Si= SUm of Pj* Pij= P*p # these are vectors
   PUTTING IT ALL TOGETHER:'''
'''Uij=Cij+(SUM of t(pt* (exp Uit)/SUMof exp Ukt ) # divided by k (al the choices cons could make conditional to t= types
 we have written m*n fixed point equations'''
class model:
    '''Simple platform eq model parameters'''
    def __init__(self, m=2,n=2):
        ''' Define default model parameters'''
        self.m,self.n=m,n #number of products and consumer types # stored as object attributes
        self.c= np.random.uniform(size=(m,n))#utlities random uniform
        self.p= np.random.dirichlet(np.ones(n))#population composition( from symmetric Dirichlet dist#random vector sums up to 1

    def __repr__(self):
        return 'Number of platform products= {:d}\nNumber of consumer types= {:d}\nPopulation composition={}\nUtilities:\n{}'.format(self.m,self.n,self.p,self.c)
    def ccp(self,u):
        '''Conditional choice probabilities, assuming choices in row'''
        u= np.asarray(u).reshape((self.m,self.n))#convert to matrix#double brackets to convert to tuple
        u= u- np.amax(u,axis=0)#de-max by column(avoid exp of large number
        e= np.exp(u)
        esum=e.sum(axis=0)#sums of exps
        return e/esum #vector of choice probsbilities
    def shares(self,pr):
        '''def shares from choice probabilities'''
        out= pr @ self.p#one-dim vector
        return out[:,np.newaxis]#output as column vector
    def F(self,u):
        '''FIxed point equation u = F(u)'''
        pr = self.ccp(u)#matrix of choice probabilities
        sh=self.shares(pr)# market shares
        u1= self.c+sh#updated utilities
        return u1.reshape(self.m*self.n)#return one dimensionnal array

def printiter(**kwargs):
    print('iter %d,err=%1.3e'%(kwargs['iter'],kwargs['err']))
md=model(m=3,n=2)
print(md)
print('SA from zero utilities')
x= solve_sa(md.F,x0=np.zeros(md.n*md.m),callback=printiter)# starting value changes maount of iter
print('Equilibrium found!')
ccp= md.ccp(x)
shares=md.shares(ccp).squeeze(axis=None)#make one dim array# make sure to add axis= none
print('Equilibrium choice probabilities',ccp,'Equilibrium market shares:', shares, sep='\n')
