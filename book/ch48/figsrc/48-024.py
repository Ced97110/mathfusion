import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(88)
box(ax, 14, 70, 60, 11, 'sujet', label=r'$1 = 1\cdot 1$')
arrow(ax, (44, 69), (44, 56), 'varie'); text(ax, 48, 62.5, r'on applique $f$', 'varie', 's', ha='left')
box(ax, 14, 44, 60, 11, 'autre', label=r'$f(1) = f(1)\,f(1)$')
arrow(ax, (44, 43), (44, 30), 'varie', lw=1.6); text(ax, 48, 36.5, r"on retire $f(1)$", 'varie', 's', ha='left')
box(ax, 14, 18, 60, 11, 'resultat', label=r"$f(1) = 1'$")
text(ax, 44, 8, 'comme x = x + x donne x = 0', 'fixe', 's')
save(fig, '48-024')
