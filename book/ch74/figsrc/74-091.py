import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
cx, cy, u = 14, 12, 10
for i in range(0, 4):
    for j in range(0, 3):
        disc(ax, cx + i*u, cy + j*u, 0.5, 'fixe')
P = lambda a, b: (cx + a*u, cy + b*u)
line(ax, [P(0, 0), P(3, 0)], 'fixe', dash=True)
line(ax, [P(3, 0), P(3, 1)], 'fixe', dash=True)
arrow(ax, P(0, 0), (P(3, 1)[0] - 1.5, P(3, 1)[1] - 0.5), 'varie', lw=1.6)
disc(ax, *P(0, 0), 1.5, 'sujet'); disc(ax, *P(3, 1), 1.5, 'resultat')
text(ax, P(1.5, 0)[0], P(1.5, 0)[1] - 3.5, '3 vers la droite', 'fixe', 's')
text(ax, P(3, 0.5)[0] + 2.5, P(3, 0.5)[1] - 2, '1 vers le haut', 'fixe', 's', ha='left')
text(ax, P(0, 0)[0] + 1, P(0, 0)[1] + 4, r'$0$ (origine)', 'sujet', 's', ha='left')
text(ax, P(3, 1)[0], P(3, 1)[1] + 4, r'$f(0)=b$', 'resultat', 's')
text(ax, 22, 40, r'$b$ : où arrive l’origine', 'varie', 's', ha='left')
save(fig, '74-091')
