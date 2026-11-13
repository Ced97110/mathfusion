import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
u = 20; r3 = math.sqrt(3); y0 = 14
A, B, C = (8, y0), (8 + u, y0), (8 + u, y0 + r3 * u)
poly(ax, [A, B, C], 'fixe')
line(ax, [A, B], 'varie', lw=1.6)
line(ax, [B, C], 'sujet', lw=1.6)
line(ax, [(B[0] - 3, y0), (B[0] - 3, y0 + 3), (B[0], y0 + 3)], 'fixe', lw=0.7)
th = [math.radians(270 - 30 + i * 30 / 10) for i in range(11)]
line(ax, [(C[0] + 9 * math.cos(t), C[1] + 9 * math.sin(t)) for t in th], 'sujet', lw=1.2)
text(ax, C[0] - 4, C[1] - 12.5, '30°', 'sujet', 's')
text(ax, 18, y0 - 4, 'opposé : 1', 'varie', 's')
text(ax, 31, y0 + 17, r'adjacent : $\sqrt{3}$', 'sujet', 's', ha='left')
box(ax, 50, 46, 36, 10, 'varie', label=r'$\tan\,30^\circ = 1/\sqrt{3}$', size='m')
arrow(ax, (68, 46), (68, 38), 'varie')
text(ax, 71, 42, r'$\times\sqrt{3}$ haut et bas', 'varie', 's', ha='left') if False else None
box(ax, 50, 28, 36, 10, 'resultat', label=r'$= \sqrt{3}/3$', size='m')
text(ax, 68, 21, '≈ 0,577', 'resultat', 'm')
save(fig, '25-090')
