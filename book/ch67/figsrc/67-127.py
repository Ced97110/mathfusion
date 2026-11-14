import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(76)
s = 2.7
text(ax, 44, 70, r'$u=\sqrt{2}+\sqrt{3}$', 'encre', 'm')
X0 = 24
# row 1 : u^3 = 11 sqrt2 + 9 sqrt3
text(ax, 4, 59, r'$u^3$', 'encre', 's', ha='left')
box(ax, X0, 55, 11 * s, 8, 'sujet', label=r'$11\sqrt{2}$', size='s')
box(ax, X0 + 11 * s, 55, 9 * s, 8, 'autre', label=r'$9\sqrt{3}$', size='s')
# row 2 : 9u = 9 sqrt2 + 9 sqrt3
text(ax, 4, 45, r'$-\,9u$', 'encre', 's', ha='left')
box(ax, X0, 41, 9 * s, 8, 'sujet', label=r'$9\sqrt{2}$', size='s')
box(ax, X0 + 9 * s, 41, 9 * s, 8, 'autre', label=r'$9\sqrt{3}$', size='s')
line(ax, [(4, 38), (82, 38)], 'fixe')
# row 3 : difference = 2 sqrt2
text(ax, 4, 31, r'$u^3-9u$', 'encre', 's', ha='left')
box(ax, X0, 27, 2 * s, 8, 'sujet', label='2', size='s')
text(ax, X0 + 2 * s + 2, 31, r'$=2\sqrt{2}$', 'sujet', 's', ha='left')
box(ax, 4, 9, 38, 9, 'resultat', label=r'$\sqrt{2}=(u^3-9u)/2$', size='s')
box(ax, 46, 9, 38, 9, 'resultat', label=r'$\sqrt{3}=u-\sqrt{2}$', size='s')
text(ax, 44, 3.5, r'donc $\mathbb{Q}(u)=\mathbb{Q}(\sqrt{2},\sqrt{3})$', 'resultat', 's')
save(fig, '67-127')
