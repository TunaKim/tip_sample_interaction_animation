# importing all important libraries
import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
from matplotlib.animation import FuncAnimation
import numpy as np
import pandas as pd

data = pd.read_csv('data3.txt', sep="\t")
data = data.assign(g=data.index % 100).query('g==0.000000')
data = data.reset_index()
#print(rpddata)
del data['g']
del data['index']
print(data)

# plotting the graph
fig, ax = plt.subplots()
x = data.loc[:,'x']
y = data.loc[:,'y']
ax.set_title('cantilever amp', fontsize=15)
ax.set_xlabel('position')
ax.set_ylabel('amplitude')
plt.scatter(x = 'x', y = 'y', data = data)
#plt.show()
# reading the image
image = plt.imread('cantilever.png')

# OffsetBox
image_box = OffsetImage(image, zoom=0.05)

# creating annotation for each point
# on the graph
x, y = np.atleast_1d(x, y)

# for each value of (x,y), we create
# an annotation
for x0, y0 in zip(x, y):
        ab = AnnotationBbox(image_box, (x0, y0), frameon=False)
        ax.add_artist(ab)

#ax.plot(x, y, c='green')
plt.show()