import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
y = 30
f = numberline(ax, 8, 78, y, -3, 5, labels=False, arrow_right=False)
box(ax, f(-3), 12, f(0) - f(-3) - 0.6, 7, 'autre', label='N')
box(ax, f(0) + 0.6, 12, f(5) - f(0) - 0.6, 7, 'resultat', label='P')
for v in (2.25, 4):
    poly(ax, [(f(v) - 1.5, y - 1.5), (f(v) + 1.5, y - 1.5), (f(v) + 1.5, y + 1.5), (f(v) - 1.5, y + 1.5)], 'fixe')
line(ax, [(f(-1) - 1.8, y - 1.8), (f(-1) + 1.8, y + 1.8)], 'limite', lw=1.6)
line(ax, [(f(-1) - 1.8, y + 1.8), (f(-1) + 1.8, y - 1.8)], 'limite', lw=1.6)
arrow(ax, (f(-1), 38), (f(-1), y + 3), 'limite')
text(ax, f(-1), 41, r'$i^2=-1$ devrait tomber ici', 'limite', 's')
text(ax, f(0), 25, '0', 'fixe', 's')
text(ax, f(2.25), 25, '2,25', 'fixe', 's')
text(ax, f(4), 25, '4', 'fixe', 's')
text(ax, 62, 37, 'carrés connus : à droite', 'fixe', 's')
save(fig, '69-013')
