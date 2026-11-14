import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(76)
f = numberline(ax, 8, 72, 66, 0, 4, labels=False, arrow_right=True)
for v, name, role in [(1, r'$r_1$', 'sujet'), (2, r'$r_2$', 'sujet'), (3, r'$s_1$', 'autre')]:
    disc(ax, f(v), 66, 3, role, label=str(v), size='s')
    text(ax, f(v), 73, name, role, 's')
for y, pair, diff in [(46, r'$(1;\ 3)$', '−2'), (32, r'$(2;\ 3)$', '−1')]:
    box(ax, 4, y, 22, 9, 'fixe', label=pair, size='s')
    arrow(ax, (27, y + 4.5), (33, y + 4.5), 'varie')
    box(ax, 34, y, 14, 9, 'varie', label=diff, size='m')
    arrow(ax, (49, y + 4.5), (57, 44), 'fixe')
box(ax, 58, 34, 28, 17, 'resultat', label='produit\n$(-2)(-1)=2$', size='s')
text(ax, 44, 20, r'facteur $a_n^m\,b_m^n=1$', 'fixe', 's')
text(ax, 44, 11, 'le tableau donne aussi $2$', 'resultat', 's')
save(fig, '70-047')
