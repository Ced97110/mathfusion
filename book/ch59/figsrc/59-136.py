import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
u, ox, oy = 9.0, 14.0, 10.0
P = lambda a, b: (ox + a * u, oy + b * u)
poly(ax, [P(0, 0), P(2, 4), P(6, 6), P(4, 2)], 'sujet', lw=0.6)
for a in range(7):
    for b in range(7):
        if (a, b) in [(2, 4), (4, 2), (6, 6)]:
            continue
        disc(ax, *P(a, b), 0.6, 'fixe')
disc(ax, *P(2, 4), 1.4, 'sujet'); disc(ax, *P(4, 2), 1.4, 'sujet'); disc(ax, *P(6, 6), 1.4, 'resultat')
arrow(ax, P(0, 0), P(2, 4), 'sujet'); arrow(ax, P(0, 0), P(4, 2), 'sujet'); arrow(ax, P(0, 0), P(6, 6), 'resultat')
text(ax, P(2, 4)[0], P(2, 4)[1] + 4.5, r'$f_1$ = (2, 4)', 'sujet', 's')
text(ax, P(4, 2)[0], P(4, 2)[1] - 4.5, r'$f_2$ = (4, 2)', 'sujet', 's')
text(ax, P(6, 6)[0] - 2, P(6, 6)[1] + 4.5, r'$f_3$ = (6, 6)', 'resultat', 's')
text(ax, 44, 79, r'$f_3=f_1+f_2$', 'resultat', 'm', weight='bold')
save(fig, '59-136')
