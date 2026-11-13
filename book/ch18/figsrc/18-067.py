import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
x0 = 26
for i, h in enumerate([r'$x$', r'$5$']):
    text(ax, x0 + 9 + 18 * i, 58, h, 'sujet', 'm')
for j, h in enumerate([r'$x$', r'$4$']):
    text(ax, x0 - 5, 47 - 14 * j, h, 'sujet', 'm')
cells = [(0, 0, r'$x^2$', 'fixe'), (1, 0, r'$5x$', 'varie'), (0, 1, r'$4x$', 'varie'), (1, 1, r'$20$', 'resultat')]
for i, j, s, r in cells:
    box(ax, x0 + 18 * i, 40 - 14 * j, 18, 14, r, label=s, size='l')
box(ax, 14, 14, 8, 6, 'varie'); text(ax, 25, 17, r'avec $x$ : une somme', 'varie', 's', ha='left')
box(ax, 14, 4, 8, 6, 'resultat'); text(ax, 25, 7, r'sans $x$ : un produit', 'resultat', 's', ha='left')
save(fig, '18-067')
