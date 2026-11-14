import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
text(ax, 44, 80, r'Un corps à $q=7$ éléments : ℤ/7', 'sujet', 's')
xs = [8 + i * 11.7 for i in range(7)]
disc(ax, xs[0], 64, 4.3, 'fixe', fill=False, label='0', size='s')
for x, a in zip(xs[1:], range(1, 7)):
    disc(ax, x, 64, 4.3, 'sujet', label=str(a), size='s')
text(ax, xs[0], 54, 'à part', 'fixe', 's')
brace(ax, xs[1] - 4.3, xs[6] + 4.3, 57, 'sujet', label=r'$q-1=6$ non nuls')
box(ax, 6, 22, 76, 12, 'resultat', label='groupe cyclique d’ordre 6', size='m')
arrow(ax, (xs[1] + (xs[6] - xs[1]) / 2, 47), (44, 35), 'resultat')
text(ax, 44, 12, r'ordre $=q-1$', 'resultat', 'm')
save(fig, '54-276')
