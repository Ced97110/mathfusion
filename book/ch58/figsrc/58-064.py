import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(82)
text(ax, 44, 76, r'$\eta(\sum x_i e_i)=\sum x_i v_i$', 'encre', 'l')
items = [(58, 'sujet', '5 riz + 4 lentilles'), (40, 'varie', '5 (2, 1) + 4 (1, 3)'),
         (22, 'varie', '(10, 5) + (4, 12)'), (4, 'resultat', '(14, 17)')]
for y, role, lab in items:
    box(ax, 2, y, 56, 11, role, label=lab)
tags = ['remplacer chaque sac', 'multiplier', 'additionner']
for i, t in enumerate(tags):
    y0 = items[i][0]; y1 = items[i + 1][0] + 11
    arrow(ax, (30, y0), (30, y1), 'varie')
    text(ax, 34, (y0 + y1) / 2, t, 'varie', 's', ha='left')
text(ax, 74, 63, 'écrire avec\nla base', 'sujet', 's')
text(ax, 74, 31, 'mêmes\ncoefficients\n5 et 4', 'fixe', 's')
save(fig, '58-064')
