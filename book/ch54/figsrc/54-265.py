import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(90)
text(ax, 44, 87, r'Éléments non nuls de ℤ/7 : le groupe $G$', 'sujet', 's')
xs = [12 + i * 12.8 for i in range(6)]
for x, a in zip(xs, range(1, 7)):
    disc(ax, x, 68, 4.3, 'sujet', label=str(a))
    arrow(ax, (x, 63.2), (x, 56), 'varie', lw=0.8)
brace(ax, xs[0] - 4.3, xs[-1] + 4.3, 74.5, 'sujet', label=r'$|G|=6$', down=False)
box(ax, 6, 42, 76, 13, 'varie', label=r'racines de $x^6-1$ : au plus 6', size='m')
text(ax, 44, 36, r'(théorème des racines : degré 6)', 'fixe', 's')
arrow(ax, (44, 33), (44, 27), 'resultat')
box(ax, 6, 14, 76, 12, 'resultat', label=r'$|G|\leq e=6\leq|G|$', size='m')
text(ax, 44, 7, r'donc $e=|G|$', 'resultat', 'm')
save(fig, '54-265')
