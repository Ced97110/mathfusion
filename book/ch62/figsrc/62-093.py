import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
text(ax, 44, 57, r'$(x+h)^3$ développé', 'encre', 'm')
cells = [(2, 16, r'$x^3$', 'fixe'), (22, 24, r'$3x^2h$', 'varie'), (50, 20, r'$3xh^2$', 'fixe'), (74, 12, r'$h^3$', 'fixe')]
for x, w, lab, role in cells:
    box(ax, x, 36, w, 10, role, label=lab)
for x in (19, 48, 72):
    text(ax, x, 41, '+', 'encre', 's')
arrow(ax, (34, 35), (34, 20), 'varie')
text(ax, 36, 28, 'coefficient de $h$', 'varie', 's', ha='left')
box(ax, 12, 8, 44, 11, 'resultat', label=r'$(x^3)^\prime=3x^2$')
save(fig, '62-093')
