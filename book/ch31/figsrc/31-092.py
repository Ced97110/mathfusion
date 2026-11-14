import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import numpy as np
fig, ax = canvas(60)
w, h, y0 = 24, 28, 18
def axes(x0):
    arrow(ax, (x0, y0), (x0 + w + 2, y0), 'fixe', lw=0.7)
    line(ax, [(x0, y0), (x0, y0 + h)], 'fixe', lw=0.7)
# 1 : droites confondues (hauteur 12)
x0 = 4; axes(x0)
line(ax, [(x0, y0 + 12), (x0 + w, y0 + 12)], 'sujet', lw=2.6)
line(ax, [(x0, y0 + 12), (x0 + w, y0 + 12)], 'encre', lw=0.8, dash=True)
text(ax, x0 + w / 2, y0 + 17, 'hauteur 12', 'sujet', 's')
# 2 : droites sécantes en x = 3
x0 = 32; axes(x0)
line(ax, [(x0, y0 + 3), (x0 + w, y0 + 3 + 2 * w * 0.9 / 1.0 * 0.5)], 'sujet', lw=1.6) if False else None
xx = np.array([0, 1]); 
line(ax, [(x0 + 0, y0 + 4), (x0 + 21, y0 + 4 + 21 * (14 / 21) * 1.0)], 'sujet', lw=1.6)
line(ax, [(x0, y0 + 14), (x0 + w, y0 + 14)], 'varie', lw=1.6)
disc(ax, x0 + 15, y0 + 14, 1.4, 'resultat')
line(ax, [(x0 + 15, y0), (x0 + 15, y0 + 14)], 'resultat', lw=0.7, dash=True)
text(ax, x0 + 15, y0 - 3.5, r'$x = 3$', 'resultat', 's')
# 3 : courbes, 4 points
x0 = 60; axes(x0)
t = np.linspace(0, 2 * math.pi, 200); X = x0 + t / (2 * math.pi) * w
ax.plot(X, y0 + 4 + np.cos(t) ** 2 * 10, color=COL['sujet'], lw=1.6, zorder=3)
ax.plot(X, y0 + 4 + (1 - np.sin(t)) * 10, color=COL['varie'], lw=1.6, zorder=3)
for a, v in ((0, 1), (math.pi / 2, 0), (math.pi, 1), (2 * math.pi, 1)):
    disc(ax, x0 + a / (2 * math.pi) * w, y0 + 4 + v * 10, 1.3, 'resultat')
text(ax, 16, 8, 'confondues', 'sujet', 's'); text(ax, 16, 3.5, 'identité', 'sujet', 's')
text(ax, 44, 8, 'un point', 'varie', 's'); text(ax, 44, 3.5, 'équation', 'varie', 's')
text(ax, 72, 8, 'quatre points', 'varie', 's'); text(ax, 72, 3.5, 'courbes', 'varie', 's')
text(ax, 44, 56, 'droites puis courbes', 'encre', 'm')
save(fig, '31-092')
