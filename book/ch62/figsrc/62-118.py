import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
# x^2 - 2 = (x - r)(x + r) : the second root -r is the opposite of r, already in K
text(ax, 44, 62, r'$x^2-2=(x-r_1)(x+r_1)$', 'encre', 'm')
y = 34
g = numberline(ax, 8, 80, y, -2, 2, 1, labels=False, arrow_right=False)
text(ax, g(0), y - 5, '0', 'fixe', 's')
disc(ax, g(1.414), y, 2, 'sujet'); text(ax, g(1.414), y - 5.5, r'$r_1$', 'sujet', 'm')
disc(ax, g(-1.414), y, 2, 'resultat'); text(ax, g(-1.414), y - 5.5, r'$-r_1$', 'resultat', 'm')
arrow(ax, (g(1.414) - 2, y + 3), (g(-1.414) + 2, y + 3), 'varie', curve=0.3)
text(ax, g(0), y + 13, 'opposé', 'varie', 's')
box(ax, 4, 4, 80, 12, 'resultat', label=r'les 2 racines sont dans $K$ : degré 2', size='s')
save(fig, '62-118')
