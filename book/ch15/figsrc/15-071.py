import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
for cx, expr, n in [(22, r'$3x+10$', '2 termes'), (66, r'$7x$', '1 terme')]:
    box(ax, cx - 17, 46, 34, 12, 'sujet', label=expr, size='l')
    text(ax, cx, 41, n, 'fixe', 's')
    text(ax, cx, 33, r'$x^{1}$ : degré 1', 'sujet', 'm')
    arrow(ax, (cx, 29), (44, 20), 'resultat')
box(ax, 24, 6, 40, 12, 'resultat', label='linéaire', size='l')
save(fig, '15-071')
