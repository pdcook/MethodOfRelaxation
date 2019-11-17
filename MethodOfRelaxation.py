import numpy as np                                      # for arrays
import matplotlib.pyplot as plt                         # for plotting
from mpl_toolkits.axes_grid1 import make_axes_locatable # for colorbar on plots

ticks = 3 # number of ticks on x and y axis of plot

N          = 41   # size of domain in y direction
M          = 41   # size of domain in x direction
iterations = 1000 # number of relaxation iterations
distance   = 5    # gridpoints between parallel plates
width      = 17   # distance of each parallel plate from the boundary
V0         = 1    # absolute potential of each plate

# initalize the domain to zeros
V  = np.zeros((N,M))

# set the potential of both capacitors, one V0 and the other -V0
V[int(N/2-distance/2), width:M-width] = V0
V[int(N/2+distance/2), width:M-width] = -V0

# begin iterating
for _ in range(iterations):
    # Eq. 8
    V = 0.2*(np.roll(V, 1, axis = 0) + np.roll(V, -1, axis = 0) \
        + np.roll(V, 1, axis = 1) + np.roll(V, -1, axis = 1))   \
        + 0.05*(np.roll(V, 1, axis = (0,1)) + np.roll(V, -1, axis = (0,1)) \
        + np.roll(np.roll(V, 1, axis = 1), -1, axis = 0) \
        + np.roll(np.roll(V, -1,axis = 1), 1, axis = 0))

    # reset the boundary conditions (the parallel plates)
    V[int(N/2-distance/2), width:M-width] = V0
    V[int(N/2+distance/2), width:M-width] = -V0

# calculate the electric field with Eq. 6
E = -1*np.array(np.gradient(V))

# plot the results
fig,ax=plt.subplots(1,1,figsize=(8,8)) # make the figure

im = ax.imshow(V, cmap = plt.get_cmap("coolwarm"), rasterized = True) # plot V

ax.quiver(E[1],E[0]) # plot E

ax.invert_yaxis() # make the y axis point up

ax.set_xlabel("$x$",size=24) # set the x label
ax.set_ylabel("$y$",size=24) # set the y label

ax.set_xticks(np.linspace(0,M-1,ticks)) # set the x ticks
ax.set_yticks(np.linspace(0,N-1,ticks)) # set the y ticks

ax.tick_params(axis='both', which='major', labelsize=20) # change the font size

# make the axis for the colorbar
divider = make_axes_locatable(ax)
cax = divider.append_axes('right', size='5%', pad=0.05)
cbar=fig.colorbar(im, cax=cax)

# add the ticks and the label to the colorbar
cax.tick_params(labelsize=20)
cax.set_ylabel("$V$",size=24)

# set the figure title
ax.set_title("$V(x,y)$ and $\\vec{E}(x,y)$",size=30)

# save to file and show on screen
plt.tight_layout()
plt.savefig("V.eps",dpi=100)
plt.show()
