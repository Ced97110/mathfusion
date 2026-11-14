import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(80)
text(ax, 44, 76, r'$f = x^3-2x^2+0x+4$, racine $p/q$', 'fixe', 's')
labs = [('autre', r'$1\,x^3$'), ('fixe', r'$-2x^2$'), ('fixe', r'$0x$'), ('sujet', r'$4$')]
for i, (r, l) in enumerate(labs):
    box(ax, 4 + i * 21, 56, 19, 10, r, label=l)
text(ax, 13.5, 51, 'dominant', 'autre', 's')
text(ax, 76.5, 51, 'constant', 'sujet', 's')
arrow(ax, (13.5, 49), (13.5, 40), 'autre')
arrow(ax, (76.5, 49), (76.5, 40), 'sujet')
box(ax, 3, 28, 36, 11, 'autre', label=r'$q$ divise 1')
box(ax, 49, 28, 36, 11, 'sujet', label=r'$p$ divise 4')
text(ax, 44, 20, r'6 fractions à tester, pas une infinité', 'resultat', 's')
box(ax, 8, 4, 72, 11, 'resultat', label=r'$\pm1,\ \pm2,\ \pm4$')
save(fig, '54-249')
