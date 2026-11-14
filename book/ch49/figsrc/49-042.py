import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(60)
text(ax, 22, 52, r'$X$', 'sujet', 'l'); text(ax, 66, 52, r'$X^{\prime}$', 'autre', 'l')
box(ax, 6, 32, 32, 14, 'sujet'); box(ax, 50, 32, 32, 14, 'autre')
for x, a in [(16, r'$x$'), (28, r'$y$')]: disc(ax, x, 39, 4, 'sujet', label=a)
for x, a in [(60, r'$x^{\prime}$'), (72, r'$y^{\prime}$')]: disc(ax, x, 39, 4.5, 'autre', label=a, size='s')
text(ax, 44, 39, r'$\cup$', 'encre', 'xl')
brace(ax, 6, 82, 28, 'resultat', label=r'$X\cup X^{\prime}$ : 4 lettres', down=True)
save(fig, '49-042')
