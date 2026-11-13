import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
ox, oy, u = 9, 8, 5.2
P = lambda a, b: (ox + a * u, oy + b * u)
for a in range(11):
    for b in range(11):
        disc(ax, *P(a, b), 0.4, 'fixe')
arrow(ax, P(0, 0), P(4, 6), 'sujet', lw=1.5)
arrow(ax, P(0, 0), P(6, 4), 'fixe', lw=1.5)
arrow(ax, P(0, 0), P(10, 10), 'varie', lw=1.5)
line(ax, [P(4, 6), P(10, 10)], 'fixe', lw=1.0, dash=True)
text(ax, P(4, 6)[0] - 7, P(4, 6)[1] + 1.5, r'$f_1$ (4, 6)', 'sujet', 'm')
text(ax, P(6, 4)[0] + 2, P(6, 4)[1] - 3.5, r'$f_2$ (6, 4)', 'fixe', 'm', ha='left')
text(ax, P(10, 10)[0] - 5, P(10, 10)[1] + 5, r"$f'_2$ (10, 10)", 'varie', 'm')
text(ax, 86, 36, r"$f'_2=f_1+f_2$", 'varie', 'm', ha='right')
text(ax, 86, 28, r"$f_2=f'_2-f_1$", 'resultat', 'm', ha='right')
text(ax, 86, 18, r'$Q=(1\ 0;\ 1\ 1)$', 'varie', 'm', ha='right')
save(fig, '59-043')
