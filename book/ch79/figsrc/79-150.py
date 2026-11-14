import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(104)
O = (22, 22); U = 40
P = lambda i, j: (O[0] + i * U, O[1] + j * U)
text(ax, 44, 99, 'les 5 sous-espaces de $\\mathbb{F}_2^2$', 'encre', 's')
for x, lab, role in [(2, r'$\{0\}$', 'fixe'), (19, r'$D_1$', 'varie'), (36, r'$D_2$', 'varie'), (53, r'$D_3$', 'varie'), (70, r'$E$', 'sujet')]:
    box(ax, x, 82, 16, 11, role, label=lab, size='m')
line(ax, [P(1, 0), P(1, 1)], 'fixe', dash=True); line(ax, [P(0, 1), P(1, 1)], 'fixe', dash=True)
arrow(ax, P(0, 0), (P(1, 0)[0] - 3, P(1, 0)[1]), 'varie', lw=1.4)
arrow(ax, P(0, 0), (P(0, 1)[0], P(0, 1)[1] - 3), 'varie', lw=1.4)
arrow(ax, P(0, 0), (P(1, 1)[0] - 2.2, P(1, 1)[1] - 2.2), 'varie', lw=1.4)
for (i, j) in [(1, 0), (0, 1), (1, 1)]:
    disc(ax, *P(i, j), 2.4, 'sujet')
disc(ax, *P(0, 0), 2.4, 'fixe')
text(ax, P(0, 0)[0], P(0, 0)[1] - 6, '(0, 0)', 'fixe', 's')
text(ax, P(1, 0)[0], P(1, 0)[1] - 6, '(1, 0)', 'sujet', 's')
text(ax, P(0, 1)[0], P(0, 1)[1] + 6, '(0, 1)', 'sujet', 's')
text(ax, P(1, 1)[0], P(1, 1)[1] + 6, '(1, 1)', 'sujet', 's')
text(ax, 40, 26.5, r'$D_1$', 'varie', 'm'); text(ax, 17, 42, r'$D_2$', 'varie', 'm'); text(ax, 47, 38, r'$D_3$', 'varie', 'm')
text(ax, 44, 7, r'$(1,1)=(1,0)+(0,1)$' + '\nmodulo 2', 'resultat', 's')
save(fig, '79-150')
