import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
xa, xb = 8, 80
line(ax, [(xa, 44), (xb, 44)], 'sujet', lw=2.0)
disc(ax, xa, 44, 1.4, 'sujet'); disc(ax, xb, 44, 1.4, 'sujet')
brace(ax, xa, xb, 47, 'sujet', label=r'$\ell$', down=False, size='l')
box(ax, 6, 14, 34, 10, 'fixe', label=r'$\ell$ = 10,16 cm', size='m')
box(ax, 48, 14, 34, 10, 'autre', label=r'$\ell$ = 4 po', size='m')
arrow(ax, (30, 41), (23, 25.5), 'varie'); arrow(ax, (58, 41), (65, 25.5), 'varie')
text(ax, 44, 5, 'deux nombres, une seule longueur', 'resultat', 's')
save(fig, '11-011')
