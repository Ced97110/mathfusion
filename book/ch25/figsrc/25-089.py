import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
u = 20; r3 = math.sqrt(3); y0 = 14
A, B, C = (8, y0), (8 + u, y0), (8 + u, y0 + r3 * u)
poly(ax, [A, B, C], 'fixe')
line(ax, [B, C], 'varie', lw=1.6)
line(ax, [A, B], 'sujet', lw=1.6)
line(ax, [(B[0] - 3, y0), (B[0] - 3, y0 + 3), (B[0], y0 + 3)], 'fixe', lw=0.7)
th = [math.radians(i * 60 / 10) for i in range(11)]
line(ax, [(A[0] + 7 * math.cos(t), y0 + 7 * math.sin(t)) for t in th], 'sujet', lw=1.2)
text(ax, 17, y0 + 3.5, '60°', 'sujet', 's')
text(ax, 18, y0 - 4, 'adjacent : 1', 'sujet', 's')
text(ax, 31, y0 + 17, r'opposé : $\sqrt{3}$', 'varie', 's', ha='left')
box(ax, 52, 44, 34, 10, 'fixe', label=r'$\tan\,60^\circ$ = opposé / adjacent', size='s') if False else None
box(ax, 50, 40, 36, 10, 'sujet', label=r'$\tan\,60^\circ = \sqrt{3}/1$', size='m')
arrow(ax, (68, 40), (68, 32), 'varie')
box(ax, 50, 22, 36, 10, 'resultat', label=r'$= \sqrt{3}$', size='m')
text(ax, 68, 15, '≈ 1,732', 'resultat', 'm')
save(fig, '25-089')
