import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
rows = [(66, 'mardi', r'$2x+y$', '8', 'autre'), (44, 'lundi', r'$x+y$', '5', 'sujet'), (20, 'reste', r'$x$', '3', 'resultat')]
for yb, nm, a, b, role in rows:
    text(ax, 3, yb + 5, nm, role, 's', ha='left')
    box(ax, 20, yb, 30, 10, role, label=a); text(ax, 56, yb + 5, '=', role, 'l'); box(ax, 62, yb, 20, 10, role, label=b)
text(ax, 11, 55, '$-$', 'varie', 'xl'); text(ax, 56, 55, '$-$', 'varie', 'xl')
line(ax, [(3, 38), (82, 38)], 'fixe')
text(ax, 44, 10, 'un café de plus : 8 $-$ 5 = 3 €', 'resultat', 's')
save(fig, '24-045')
