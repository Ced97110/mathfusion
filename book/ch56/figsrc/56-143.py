import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
y = 20
items = [(4, 26, 'fixe', r'$6x+9$', r'$f$'), (42, 12, 'sujet', r'$3$', r'$c(f)$'), (64, 20, 'resultat', r'$2x+3$', r'$f_1$ : contenu 1')]
for x, w, role, lab, name in items:
    box(ax, x, y, w, 10, role, label=lab)
    text(ax, x + w / 2, y - 5, name, role, 's')
text(ax, 36, y + 5, '=', 'encre', 'l')
text(ax, 58, y + 5, r'$\times$', 'encre', 'l')
arrow(ax, (17, y + 12), (74, y + 12), 'varie', curve=-0.28)
text(ax, 45, y + 25, r'$\div 3$ sur chaque coefficient', 'varie', 's')
save(fig, '56-143')
