import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
box(ax, 8, 50, 24, 14, 'sujet', label=r'$D$', size='xl')
box(ax, 52, 50, 28, 14, 'varie', label=r'$[x]$', size='xl')
arrow(ax, (20, 50), (20, 44), 'sujet')
arrow(ax, (66, 50), (66, 44), 'varie')
text(ax, 20, 40, 'les coefficients', 'sujet', 's')
text(ax, 20, 36, 'viennent de $D$', 'sujet', 's')
text(ax, 66, 40, 'on ajoute', 'varie', 's')
text(ax, 66, 36, 'la lettre $x$', 'varie', 's')
text(ax, 44, 27, r'ici $D=\mathbb{Z}$ : un élément de $\mathbb{Z}[x]$', 'encre', 's')
y = 8
parts = [(4, 14, 'sujet', r'$3$'), (18, 12, 'varie', r'$x^2$'), (32, 6, 'encre', '+'), (38, 14, 'sujet', r'$5$'),
         (52, 8, 'varie', r'$x$'), (60, 6, 'encre', '+'), (66, 16, 'sujet', r'$7$')]
for x, w, role, lab in parts:
    if lab == '+':
        text(ax, x + w / 2, y + 4.5, '+', 'encre', 'l')
    else:
        box(ax, x, y, w, 9, role, label=lab)
save(fig, '56-140')
