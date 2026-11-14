import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
u = 20; r3 = math.sqrt(3); y0 = 12
A, B, C = (8, y0), (8 + u, y0), (8 + u, y0 + r3 * u)
poly(ax, [A, B, C], 'fixe')
line(ax, [(B[0] - 3, y0), (B[0] - 3, y0 + 3), (B[0], y0 + 3)], 'fixe', lw=0.7)
th = [math.radians(i * 60 / 10) for i in range(11)]
line(ax, [(A[0] + 7 * math.cos(t), y0 + 7 * math.sin(t)) for t in th], 'autre', lw=1.2)
text(ax, 17, y0 + 3.5, '60°', 'autre', 's')
th = [math.radians(270 - 30 + i * 30 / 10) for i in range(11)]
line(ax, [(C[0] + 9 * math.cos(t), C[1] + 9 * math.sin(t)) for t in th], 'sujet', lw=1.2)
text(ax, C[0] - 4, C[1] - 12.5, '30°', 'sujet', 's')
text(ax, 18, y0 - 4, '1', 'fixe', 's')
text(ax, 31.5, y0 + 17, r'$\sqrt{3}$', 'fixe', 's', ha='left')
text(ax, 18, 62, r'$30° + 60° = 90°$', 'varie', 'm')
box(ax, 48, 48, 38, 10, 'sujet', label=r'$\tan\,30^\circ = 1/\sqrt{3}$', size='s')
box(ax, 48, 32, 38, 10, 'autre', label=r'$\tan\,60^\circ = \sqrt{3}/1$', size='s')
text(ax, 67, 45, r'$\times$', 'varie', 'm')
arrow(ax, (67, 32), (67, 24), 'varie')
box(ax, 48, 14, 38, 10, 'resultat', label=r'$1/\sqrt{3}\times\sqrt{3} = 1$', size='s')
save(fig, '25-091')
