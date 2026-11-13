import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
text(ax, 20, 60, 'sur le sol', 'fixe', 's'); text(ax, 66, 60, 'sur l’image', 'fixe', 's')
for xb in (8, 32):
    line(ax, [(xb, 18), (xb, 52)], 'sujet', lw=1.3)
text(ax, 20, 11, 'ne se touchent pas', 'fixe', 's')
P = (66, 52)
for xb in (50, 82):
    line(ax, [(xb, 18), P], 'sujet', lw=1.3)
disc(ax, P[0], P[1], 2.2, 'limite')
text(ax, 66, 57, r'$P_\infty$', 'limite', 'm')
text(ax, 66, 11, 'se touchent en $P_\\infty$', 'limite', 's')
save(fig, '80-281')
