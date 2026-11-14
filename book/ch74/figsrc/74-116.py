import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
u = 8; ox = 6; oy = 8
P = lambda x, y: (ox + x * u, oy + y * u)
arrow(ax, P(-0.2, 0), P(4.0, 0), 'fixe', lw=0.7)
line(ax, P(0, 0) and [P(0, -0.2), P(0, 4.4)], 'fixe', lw=0.7)
line(ax, [P(-0.2, 2), P(4.0, 2)], 'sujet', lw=1.3, dash=True)
text(ax, *P(1.2, 2.45), r'axe $D$ : $x_2=2$', 'sujet', 's')
arrow(ax, P(0, 0), P(3, 0), 'resultat', lw=1.5)
arrow(ax, P(3, 0), P(3, 4), 'varie', lw=1.5)
arrow(ax, P(0.05, 0.05), P(2.95, 3.95), 'fixe', lw=0.9)
text(ax, *P(1.4, -0.55), r'$b_1=(3,0)$', 'resultat', 's')
text(ax, *P(3.1, 3.0), r'$b_2=(0,4)$', 'varie', 's', ha='left')
text(ax, *P(1.0, 3.2), r'$b$', 'fixe', 'm')
line(ax, [P(-0.45, 0), P(-0.45, 2)], 'varie', lw=0.8)
text(ax, *P(-0.45, 1.0), '2', 'varie', 's', ha='right')
for i, s in enumerate(['1. couper b en b₁, b₂', '2. D à la moitié de b₂', '3. glisser de 3 le long de D']):
    box(ax, 50, 40 - i * 14, 36, 10, ['fixe', 'varie', 'resultat'][i], label=s, size='s')
save(fig, '74-116')
