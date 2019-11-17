from numpy import*
from matplotlib.pyplot import*
N=30
d=10
s=10
r=roll
V=zeros((N,N))
exec('V=(r(V,1,0)+r(V,-1,0)+r(V,1,1)+r(V,-1,1))/4;V[s:-s,s:s-~d:d]=1,-1;'*9*N)
E=gradient(-V)
imshow(V)
quiver(E[1],-E[0])
show()
