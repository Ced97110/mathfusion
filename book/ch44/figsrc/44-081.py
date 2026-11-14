import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
box(ax, 4, 14, 12, 12, 'sujet', label=r'$\alpha$', size='l')
text(ax, 11, 8, 'transformation', 'sujet', 's')
box(ax, 34, 12, 50, 16, 'sujet', fill=False, dash=True)
for i, l in enumerate([r'$1$', r'$\alpha$', r'$\alpha^{2}$', r'$\alpha^{3}$']):
    box(ax, 37 + i * 11, 15, 9, 10, 'resultat', label=l, size='s')
text(ax, 81, 20, '…', 'resultat', 'l')
arrow(ax, (17, 20), (33, 20), 'varie')
text(ax, 25, 24, 'répéter', 'varie', 's')
text(ax, 59, 40, r'$\langle\alpha\rangle$', 'sujet', 'xl')
text(ax, 59, 33, 'toutes les puissances', 'sujet', 's')
save(fig, '44-081')
