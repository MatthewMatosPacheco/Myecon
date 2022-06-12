import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt
"""NOT MY ALGORITHM!!! bELONGS TO DR fedor ISHAKOV"""
plt.rcParams['figure.figsize'] = [12, 8]

class polyline():
    '''Class that implements the linearly interpolated function'''

    def __init__(self,x,y,label='no label'):
        '''Initializer of the polyline object
        '''
        self.x,self.y = np.asarray(x,dtype=float).ravel(),np.asarray(y,dtype=float).ravel()
        if self.x.size != self.y.size:
            raise ValueError('The input arguments to polyline should be the same length')
        self.label = '{:s}'.format(label)  # string label

    def __len__(self):
        '''Length of the polyline'''
        return self.x.size # ex [1,2,6],[3,4,5] lenght =3, first[]=x, 2nd[]=y

    def __repr__(self):
        '''String representation of polyline, creates and returns a string'''
        return 'Polyline with {} points labeled "{}"\nx={}\ny={}'.format(len(self),self.label,self.x,self.y)

    def __call__(self,x):
        '''Returns the values of the polyline computed for given points x'''
        interp = interpolate.interp1d(self.x,self.y,bounds_error=False, fill_value=np.nan)# from scipy finds f(x)
        return interp(x)

    def __add__(self,other):
        '''Overload of + to concatinate two polylines'''
        if not isinstance(other,polyline):
            raise TypeError('Only polyline can be added to another polyline')
        x = np.concatenate((self.x, other.x))
        y = np.concatenate((self.y, other.y))
        label = self.label + ' + ' + other.label
        return polyline(x,y,label=label)

    def plot(self, ax=None, **kwargs):
        '''Makes a plot of polyline'''
        if not ax:
            ax = plt.axes()
        ax.plot(self.x, self.y, label=self.label, **kwargs)
        return ax

    def intersect(self, other):
        '''Return the 2-dim numpy array of intersection points between two polylines (in row)'''
        if not isinstance(other, polyline):
            raise TypeError('Only polyline can be added to another polyline')
        ub = (len(self) - 1) * (len(other) - 1)
        out = np.empty((ub, 2))  # space for the intersection point
        k = 0  # number of intersection points so far
        for x11, y11, x12, y12 in zip(self.x, self.y, self.x[1:], self.y[1:]):
            for x21, y21, x22, y22 in zip(other.x, other.y, other.x[1:], other.y[1:]):
                pp = self.__intersect_segments(x11, y11, x12, y12, x21, y21, x22, y22)
                if pp:
                    out[k, 0], out[k, 1] = pp
                    k += 1
        out = out[:k, :]
        return out

    def self_intersect(self):
        '''Return the 2-dim numpy array of self-intersection points (in row)'''
        ub = (len(self) - 1) ** 2
        out = np.empty((ub, 2))  # space for the intersection point
        k = 0  # number of intersection points so far
        for x11, y11, x12, y12 in zip(self.x, self.y, self.x[1:], self.y[1:]):
            for x21, y21, x22, y22 in zip(self.x, self.y, self.x[1:], self.y[1:]):
                pp = self.__intersect_segments(x11, y11, x12, y12, x21, y21, x22, y22)
                if pp:
                    out[k, 0], out[k, 1] = pp
                    k += 1
        out = out[:k, :]
        return out

    def __intersect_segments(self, *args):
        '''Find intersection point of a segment, or return None'''
        # unpack parameters
        x11, y11, x12, y12 = args[:4]  # first line segment
        x21, y21, x22, y22 = args[4:]  # second line segment
        # check if segmets are identical
        if np.all(np.abs(np.asarray(args[:4]) - np.asarray(args[4:])) < 1e-10):
            return None
        # check if segmets share a point
        if np.all(np.abs(np.asarray(args[:2]) - np.asarray(args[4:6])) < 1e-10):
            return None
        if np.all(np.abs(np.asarray(args[:2]) - np.asarray(args[6:])) < 1e-10):
            return None
        if np.all(np.abs(np.asarray(args[2:4]) - np.asarray(args[4:6])) < 1e-10):
            return None
        if np.all(np.abs(np.asarray(args[2:4]) - np.asarray(args[6:])) < 1e-10):
            return None
        # bounding box check: whether intersection is possible in principle
        bb = (min(x11, x12) < max(x21, x22) and min(x21, x22) < max(x11, x12) and
              min(y11, y12) < max(y21, y22) and min(y21, y22) < max(y11, y12))
        if not bb:
            return None
        # form system of equations
        A = np.array([[x12 - x11, 0, -1, 0], [0, x22 - x21, -1, 0], [y12 - y11, 0, 0, -1], [0, y22 - y21, 0, -1]])
        b = np.array([-x11, -x21, -y11, -y21])
        t1, t2, x0, y0 = np.linalg.solve(A, b)
        if 0 <= t1 <= 1 and 0 <= t2 <= 1:
            return x0, y0
        else:
            return None