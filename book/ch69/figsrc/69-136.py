import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
text(ax, 44, 79, r'$x^5-4x+2$ : racines réelles', 'encre', 'm')
f = numberline(ax, 10, 70, 56, -2, 2, arrow_right=False)
vals = {-2: '−22', 0: '2', 1: '−1', 2: '26'}
for v, s in vals.items():
    disc(ax, f(v), 56, 1.8, 'sujet')
    text(ax, f(v), 64, s, 'sujet', 's')
text(ax, 44, 45, '3 changements de signe', 'varie', 's')
text(ax, 44, 38, 'valeurs : pas de preuve', 'fixe', 's')
arrow(ax, (44, 34), (44, 25), 'resultat')
box(ax, 8, 6, 72, 18, 'resultat', label=r'Sturm : $V(-2)-V(2)$' + '\n' + 'nombre exact de racines', size='s')
save(fig, '69-136')
