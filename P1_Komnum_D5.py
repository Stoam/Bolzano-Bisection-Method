import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

# Contoh fungsi diambil dari soal latihan nomor 3a
def func(x):
    return x**3 - 3*x + 1

# Pengecekan titik tengah
def cek(x):
    if x < 0:
        return -1
    elif x > 0:
        return 1
    else:
        return 0

# Bisection
def bisect(l, r):
    m = (l + r) / 2
    Fleft = func(l)
    Fright = func(r)
    Fmid = func(m)
    
    if cek(Fmid) == cek(Fleft):
        return m, r
    else:
        return l, m

# Metode Bolzano
def bolzano(l, r, n):
    for i in range(n):
        l, r = bisect(l, r)
        print(l, r)
    return l, r

xmin, xmax = 1, 2
yrange = func(xmin), func(xmax)
ymin, ymax = min(yrange), max(yrange)

v = np.vectorize(func)
x = np.linspace(xmin,xmax)
y = v(x)

# Initialize figure
fig = plt.figure()
ax = plt.axes(xlim=(xmin-0.1,xmax+0.1), ylim=(ymin,ymax))
curve, = ax.plot([],[], color='blue')
left, = ax.plot([],[],color='red')
right, = ax.plot([],[],color='red')

# Figure reset between frames
def init():
    left.set_data([],[])
    right.set_data([],[])
    curve.set_data([],[])
    return left, right, curve,

# Animation of bisection
def animate(i):
    l, r = bolzano(xmin, xmax, i)
    left.set_data([l,l],[ymin,ymax])
    right.set_data([r,r],[ymin,ymax])
    curve.set_data(x,y)
    return left, right, curve,

anim = animation.FuncAnimation(fig, animate, init_func=init, frames=30, interval=750, blit=True)

plt.grid()
plt.show()
