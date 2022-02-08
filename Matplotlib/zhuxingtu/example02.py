"""
柱形图渐变色
"""
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(20191001)


def gradient(ax, boundary, direction=0.3, cmap_range=(0, 1), **kwargs):
    phi = direction * np.pi / 2
    v = np.array([np.cos(phi), np.sin(phi)])
    X = np.array([[v @ [1, 0], v @ [1, 1]],
                  [v @ [0, 0], v @ [0, 1]]])
    a, b = cmap_range
    X = a + (b - a) / X.max() * X
    im = ax.imshow(X, extent=boundary, interpolation='bicubic',
                   vmin=0, vmax=1, **kwargs)
    return im


def gradient_bar(ax, x, y, width=0.3, bottom=0):
    for left, top in zip(x, y):
        right = left + width
        gradient(ax, boundary=(left, right, bottom, top),
                 cmap=plt.cm.Reds, cmap_range=(0.8, 0), direction = 0.3)


length = 5
xmin, xmax  = 0, length
ymin, ymax =  0, 1

fig, ax = plt.subplots()
ax.set(xlim=(xmin, xmax), ylim=(ymin, ymax), autoscale_on=False)

x = np.arange(length) + 0.2
y = np.random.rand(length)

# bar image
gradient_bar(ax, x, y, width=0.3)
ax.set_aspect('auto')
plt.show()