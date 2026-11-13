import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

def arc(ax, c, r, a0, a1, role, lw=0.9):
    pts = [(c[0] + r * math.cos(math.radians(a0 + (a1 - a0) * i / 120)), c[1] + r * math.sin(math.radians(a0 + (a1 - a0) * i / 120))) for i in range(121)]
    line(ax, pts, role, lw)

fig, ax = canvas(48)
A = (24, 14); e = (A[0] + 40 * math.cos(math.radians(40)), 14 + 40 * math.sin(math.radians(40)))
arrow(ax, A, (82, 14), 'sujet', lw=1.3); arrow(ax, A, e, 'sujet', lw=1.3)
arc(ax, A, 11, 0, 40, 'varie', 1.3); disc(ax, A[0], A[1], 1.4, 'sujet')
text(ax, 18.5, 11.5, r'$A$', 'sujet', 'l')
text(ax, 22, 5, 'le point A : l’endroit', 'sujet', 's')
arrow(ax, (24, 7.5), (24, 12.4), 'sujet', lw=0.8)
text(ax, 68, 30, 'l’angle A : l’ouverture', 'varie', 's')
arrow(ax, (53, 27.5), (35.5, 19), 'varie', lw=0.8)
save(fig, '25-016')
