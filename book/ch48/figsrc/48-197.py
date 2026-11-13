import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(78)
text(ax, 20, 73, r'$A$ : entiers', 'sujet', 'm')
text(ax, 68, 73, 'horloge à 12', 'autre', 'm')
rows = [(58, '5 + 9 = 14', 'reste 2', 'sujet'), (40, '5 × 9 = 45', 'reste 9', 'sujet'), (22, '0, 12, 24, …', 'reste 0', 'varie')]
for y, a, b, r in rows:
    box(ax, 3, y - 5, 34, 10, r, label=a)
    box(ax, 54, y - 5, 28, 10, 'resultat', label=b)
    arrow(ax, (38, y), (53, y), 'fixe')
text(ax, 45.5, 63.5, r'$f$', 'fixe', 'm')
text(ax, 20, 12.5, 'noyau', 'varie', 's')
text(ax, 44, 4, r'$A/\ker f \cong \mathrm{im}\,f$', 'resultat', 'm')
save(fig, '48-197')
