# importing all important libraries
import matplotlib.animation
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
import pandas as pd



data = pd.read_csv('data3.txt', sep="\t")
data = data.assign(g=data.index % 500).query('g==0.000000')
data = data.reset_index()

del data['g']
del data['index']
#print(data)

# plotting the graph
fig = plt.figure(figsize=(6,10))
x1 = data.loc[:,'x']
y1 = data.loc[:,'y']

#plt.scatter(x = 'x', y = 'y', data = data)
def a(i):
    fig.clear()
    plt.scatter(x=x1[i], y=y1[i], s=400, marker='v')
    plt.title('cantilever amp', fontsize=30)
    plt.ylabel('amplitude (nm)',fontsize=20)
    plt.xlim(-0.5,0.5)
    plt.ylim(-10,10)
    plt.yticks(size=20)
    plt.gca().axes.get_xaxis().set_visible(False)
    plt.hlines(-8+(i/100), -0.5, 0.5, color='gray', linestyle='solid', linewidth=5)
    plt.text(0,-8.2+(i/100),'Sample surface',va='top',ha='center',fontsize=20)
    plt.tight_layout()
    return

anima1 = FuncAnimation(fig, a, frames = len(data), interval=1)
anima1.save('animation.gif', writer = 'pillow')
plt.show()