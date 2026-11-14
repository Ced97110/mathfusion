import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(54)
c = 9
def cell(x, y, role, s=None): box(ax, x, y, c, c, role, label=s, size='m', r=0.5)
cell(6, 37, 'varie', '2'); cell(15, 37, 'varie', '0'); cell(6, 28, 'fixe'); cell(15, 28, 'fixe')
cell(30, 37, 'fixe'); cell(39, 37, 'varie', '1'); cell(30, 28, 'fixe'); cell(39, 28, 'varie', '1')
cell(56, 37, 'fixe'); cell(65, 37, 'resultat', '2'); cell(56, 28, 'fixe'); cell(65, 28, 'fixe')
text(ax, 27, 37, r'$\times$', 'encre', 'l'); text(ax, 52, 37, '=', 'encre', 'l')
text(ax, 15, 23, r'$A$', 'sujet', 'm'); text(ax, 39, 23, r'$B$', 'autre', 'm'); text(ax, 65, 23, r'$AB$', 'resultat', 'm')
text(ax, 44, 11, r'$2 \times 1 + 0 \times 1 = 2$', 'resultat', 'm')
save(fig, '43-041')
