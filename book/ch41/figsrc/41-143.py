import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
import math
fig, ax = canvas(50)
k = 0.6
A = (10, 18)
fx = 43.30 * k; fy = 25 * k
tip = (A[0] + fx, A[1] + fy)
foot = (tip[0], A[1])
arrow(ax, (10, 6), (80, 6), 'fixe', lw=1.2)
line(ax, [tip, foot], 'fixe', dash=True)
arrow(ax, foot, tip, 'fixe', lw=1.3)
arrow(ax, A, tip, 'sujet', lw=1.5)
arrow(ax, A, foot, 'resultat', lw=2.4)
text(ax, 20, 28, '50 N', 'sujet', 's')
text(ax, 23, 11.5, '43,30 N : avance', 'resultat', 's')
text(ax, 51, 22,'25 N : soulève', 'fixe', 's')
text(ax, 66, 2.5, 'déplacement', 'fixe', 's')
box(ax, 50, 36, 36, 9, 'resultat', label='seule cette part travaille', size='s')
arrow(ax, (58, 35.5), (30, 19.5), 'resultat')
save(fig, '41-143')
