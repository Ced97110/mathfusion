import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
cw = 15
x0, y0 = 20, 18
text(ax, x0 + cw/2, y0 + 2*cw + 6, 'A', 'sujet', 'm'); text(ax, x0 + 1.5*cw + 1, y0 + 2*cw + 6, 'B', 'autre', 'm')
text(ax, 11, y0 + 1.5*cw + 1, 'A', 'sujet', 'm'); text(ax, 11, y0 + cw/2, 'B', 'autre', 'm')
cells = [(0, 0, r'$A^2$', 'sujet'), (1, 0, r'$AB$', 'varie'), (0, 1, r'$BA$', 'varie'), (1, 1, r'$B^2$', 'autre')]
for c, r, lab, role in cells:
    box(ax, x0 + c*(cw+1), y0 + (1-r)*(cw+1), cw, cw, role, label=lab, size='l')
text(ax, 70, 62, r'$(A+B)^2$ : 4 termes', 'encre', 's')
text(ax, 72, 52, 'tableaux', 'limite', 's')
box(ax, 58, 38, 28, 11, 'limite', label=r'$AB+BA\neq 2AB$', size='s')
text(ax, 72, 28, 'nombres 2 et 3', 'resultat', 's')
box(ax, 58, 14, 28, 11, 'resultat', label=r'$6+6=2\cdot 6$', size='s')
save(fig, '51-206')
