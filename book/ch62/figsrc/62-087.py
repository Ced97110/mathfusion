import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(52)
for x in (6, 32):
    box(ax, x, 28, 20, 11, 'sujet', label=r'$x-1$')
text(ax, 29, 33.5, r'$\times$', 'encre', 'l')
text(ax, 55, 33.5, r'$\times$', 'encre', 'l')
box(ax, 58, 28, 20, 11, 'autre', label=r'$x+2$')
brace(ax, 6, 52, 28, 'sujet', label=r'$k_1=2$ : racine 1, 2 fois', down=True)
brace(ax, 58, 78, 28, 'autre', label=r'$k_2=1$ : racine $-2$', down=True)
text(ax, 44, 12, r'degré $3=2+1$', 'encre', 'm')
text(ax, 44, 46, r'$f=(x-1)^2\,(x+2)$', 'fixe', 's')
save(fig, '62-087')
