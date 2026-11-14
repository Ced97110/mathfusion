import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(90)
ox, oy, u = 12, 38, 6.2
P = lambda a, b: (ox + a * u, oy + b * u)
for a in range(0, 8):
    for b in range(-2, 8):
        disc(ax, *P(a, b), 0.4, 'fixe')
arrow(ax, P(0, 0), P(4, 6), 'sujet', lw=1.5)
arrow(ax, P(0, 0), P(6, 4), 'sujet', lw=1.5)
arrow(ax, P(0, 0), P(2, -2), 'resultat', lw=1.5)
arrow(ax, P(4, 6), P(6, 4), 'resultat', lw=1.2)
disc(ax, *P(2, -2), 1.3, 'resultat')
text(ax, P(4, 6)[0] - 7, P(4, 6)[1] + 1.5, r'$f_1$ (4, 6)', 'sujet', 'm')
text(ax, P(6, 4)[0] + 2, P(6, 4)[1] + 1.5, r'$f_2$ (6, 4)', 'sujet', 'm', ha='left')
text(ax, P(2, -2)[0] + 2.5, P(2, -2)[1] - 3, r'$f_2-f_1$ (2, −2) $\in K$', 'resultat', 'm', ha='left')
text(ax, 44, 12, r'$f_2=(f_2-f_1)+f_1$', 'resultat', 'l')
text(ax, 44, 5, r'$T_{21}(-1)$ : ligne 2 $-$ ligne 1', 'varie', 's')
save(fig, '59-062')
