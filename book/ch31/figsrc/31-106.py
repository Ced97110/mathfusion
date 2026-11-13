import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import numpy as np
fig, ax = canvas(52)
u = 22; t = np.radians(35); O = (14, 8); B = (14, 8 + u); A = (14 + u, 8)
S = (14 + u / np.tan(t), 8 + u)
th = np.linspace(0, np.pi / 2, 40)
line(ax, [(14 + u * np.cos(a), 8 + u * np.sin(a)) for a in th], 'fixe')
poly(ax, [O, B, S], 'sujet')
line(ax, [O, B], 'varie', lw=1.6)
line(ax, [O, S], 'resultat', lw=1.6)
line(ax, [(B[0] + 0.0, B[1] - 2), (B[0] + 2, B[1] - 2), (B[0] + 2, B[1])], 'fixe')
text(ax, 10.5, 19, 'OB = 1', 'varie', 's', rot=90)
text(ax, 44, 17, 'OS = 1,7434', 'resultat', 's', ha='left')
text(ax, 44, 10, 'OS plus long que OB', 'resultat', 's', ha='left')
text(ax, 58, 46, 'cosec θ :', 'encre', 's', ha='left')
for i, s in enumerate(('35° : 1,7434', '30° : 2', '90° : 1')):
    text(ax, 58, 40 - i * 6, s, 'encre', 's', ha='left')
text(ax, 10.5, 6, 'O', 'encre', 's'); text(ax, 10.5, 32, 'B', 'encre', 's'); text(ax, 47.5, 33, 'S', 'encre', 's')
save(fig, '31-106')
