import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
text(ax, 44, 64, 'facteurs : nombres de $F$', 'encre', 's')
line(ax, [(44, 12), (44, 59)], 'fixe', 0.6, dash=True)
for y, lab, dx, role in ((54, '$z$', 8, 'sujet'), (42, r'$3\times z$', 24, 'varie'), (30, r'$0{,}5\times z$', 4, 'varie'), (18, r'$-2\times z$', -16, 'varie')):
    text(ax, 2, y, lab, role, 's', ha='left')
    arrow(ax, (44, y), (44 + dx, y), role)
box(ax, 22, 2, 44, 8, 'resultat', label=r'ici $F=\mathbb{R}$', size='s')
save(fig, '77-043')
