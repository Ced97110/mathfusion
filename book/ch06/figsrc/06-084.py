import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(85)
text(ax, 44, 74, r'$\frac{x+1}{x-2}$', 'sujet', 'xl')
f = numberline(ax, 8, 76, 52, 0, 6, arrow_right=False)
for v, r in ((5, 'resultat'), (2, 'limite')):
    disc(ax, f(v), 52, 1.4, r)
    text(ax, f(v), 58, rf'$x={v}$', r, 'm')
box(ax, 4, 8, 38, 16, 'limite', label='haut 3, bas 0 : interdit', size='s')
box(ax, 46, 8, 38, 16, 'resultat', label='haut 6, bas 3 : 2', size='s')
arrow(ax, (f(2), 43), (23, 26), 'limite')
arrow(ax, (f(5), 43), (65, 26), 'resultat')
save(fig, '06-084')
