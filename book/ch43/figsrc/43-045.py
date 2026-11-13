import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
def row(y, l, a, r, rr, lab, lr):
    box(ax, 4, y, 22, 12, 'sujet', label=l, size='s'); box(ax, 62, y, 22, 12, rr, label=r, size='s')
    arrow(ax, (27, y + 6), (61, y + 6), lr); text(ax, 44, y + 10, lab, lr, 's')
row(50, r'$A$', 0, r'$B$', 'autre', r'$P\,A\,P^{-1}$', 'varie')
row(28, r'$A$', 0, r'$A$', 'sujet', r'$P = I$', 'resultat')
box(ax, 4, 6, 22, 12, 'sujet', label=r'$I$', size='s'); box(ax, 62, 6, 22, 12, 'limite', label='(1 0 ; 0 2)', size='s')
text(ax, 44, 12, r'$\sim$', 'limite', 'l'); line(ax, [(40, 8), (48, 16)], 'limite', lw=1.2)
text(ax, 44, 3, 'pas semblables', 'limite', 's')
text(ax, 44, 23.5, 'égalité : cas particulier', 'resultat', 's')
save(fig, '43-045')
