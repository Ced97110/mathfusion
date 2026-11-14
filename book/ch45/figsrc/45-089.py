import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(64)
text(ax, 44, 59, r'$1_L$ : $x\mapsto 1x = x$', 'sujet', 'm')
for i in range(4):
    x = 22 + i * 14
    disc(ax, x, 48, 3.8, 'fixe', label=str(i)); disc(ax, x, 26, 3.8, 'fixe', label=str(i))
    arrow(ax, (x, 44), (x, 30.5), 'fixe', lw=1.2)
text(ax, 8, 48, r'$x$', 'fixe', 'l'); text(ax, 8, 26, r'$1x$', 'fixe', 'l')
box(ax, 10, 4, 34, 10, 'sujet', label=r'$1_L\circ 2_L$')
text(ax, 49, 9, '=', 'resultat', 'l')
box(ax, 54, 4, 22, 10, 'resultat', label=r'$2_L$')
save(fig, '45-089')
