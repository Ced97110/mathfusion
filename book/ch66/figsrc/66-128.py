import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import numpy as np
fig, ax = canvas(54)
base = 22
ts = np.linspace(0, 1, 60)
xs = 14 + 40 * ts
ys = base + 16 * np.sin(np.pi * ts) ** 2
pts = [(14, base)] + list(zip(xs, ys)) + [(54, base)]
poly(ax, pts, 'sujet')
line(ax, [(8, base), (60, base)], 'fixe')
line(ax, [(10, base + 24), (56, base + 24)], 'fixe', dash=True)
text(ax, 67, base + 24, '0,001', 'fixe', 's')
text(ax, 14, base - 2.5, '0', 'fixe', 's')
text(ax, 54, base - 2.5, '1', 'fixe', 's')
brace(ax, 14, 54, base - 6, 'fixe', label='longueur 1')
text(ax, 34, base + 8, r'aire $=R$', 'sujet', 's')
text(ax, 71, base + 12, r'courbe $h\,e^{-t}$', 'sujet', 's')
text(ax, 44, 4, 'courbe petite : aire petite', 'resultat', 's')
save(fig, '66-128')
