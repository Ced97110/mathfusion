import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
text(ax, 44, 59, 'flèche : élever au carré', 'varie')
items = [(r'$z=1+i$', 'sujet'), (r'$z^2=2i$', 'varie'), (r'$z^4=2$', 'varie'), (r'$z^8=1$', 'resultat')]
xs = [3 + i * 22.6 for i in range(4)]
for x, (s, role) in zip(xs, items):
    box(ax, x, 44, 15, 10, role, label=s, size='s')
for x in xs[:3]:
    arrow(ax, (x + 15.2, 49), (x + 22.4, 49), 'varie')
cx = xs[2] + 7.5
arrow(ax, (cx, 44), (cx, 34.8), 'resultat')
text(ax, cx + 3, 39.5, 'l’ordre ne divise pas 4', 'resultat', 's', ha='left')
box(ax, 36, 24, 40, 10, 'resultat', label=r'$z^4=2\neq1$')
arrow(ax, (56, 24), (56, 16.8), 'resultat')
box(ax, 30, 6, 52, 10, 'resultat', label='ordre 8 = 8 éléments non nuls', size='s')
save(fig, '67-163')
