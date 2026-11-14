import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(82)
box(ax, 4, 44, 80, 32, 'sujet')
text(ax, 44, 72, r'$E=\mathbb{F}_2(X,Y)$', 'sujet', 'm')
text(ax, 44, 63, r'base de $E$ sur $K$ : $[E:K]=4$', 'sujet', 's')
for k, lab in enumerate([r'$1$', r'$X$', r'$Y$', r'$XY$']):
    box(ax, 8 + 19 * k, 48, 15, 10, 'autre', label=lab)
arrow(ax, (44, 43.5), (44, 34), 'varie')
text(ax, 48, 39, r'$z\mapsto z^2$, pour tout $z$', 'varie', 's', ha='left')
box(ax, 22, 22, 44, 11, 'fixe', label=r'$K$ : les carrés de $E$')
arrow(ax, (44, 21.5), (44, 15), 'limite')
box(ax, 6, 4, 76, 10, 'limite', label=r'degré de $z\leq 2$, jamais 4 : pas de $z$ primitif', size='s')
save(fig, '67-126')
