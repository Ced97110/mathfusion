import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
ox, oy, u = 12, 10, 9.5
for i in range(8): line(ax, [(ox + i*u, oy), (ox + i*u, oy + 4*u)], 'fixe', lw=0.3)
for j in range(5): line(ax, [(ox, oy + j*u), (ox + 7*u, oy + j*u)], 'fixe', lw=0.3)
P = [(ox + 2*i*u, oy + i*u) for i in range(4)]
for i in range(3): arrow(ax, P[i], P[i+1], 'varie')
line(ax, [P[3], (ox + 7*u, oy + 3.5*u)], 'varie', dash=True)
text(ax, ox + 7.5*u, oy + 3.75*u, '…', 'varie', 'l')
disc(ax, *P[0], 1.4, 'fixe', label=None)
text(ax, P[0][0] - 2.5, P[0][1] + 3, '$O$', 'fixe', 'm')
for i, lab in enumerate(['$b$', '$2b$', '$3b$'], start=1):
    disc(ax, *P[i], 1.4, 'sujet')
    text(ax, P[i][0] - 3.5, P[i][1] + 3.2, lab, 'sujet', 'm')
text(ax, 44, 4, r'jamais de retour à $O$', 'limite', 'm')
save(fig, '74-066')
