import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(68)
text(ax, 44, 63, r'$G\supset G^{\prime}\supset G^{\prime\prime}\supset\cdots$', 'sujet', 'l')
rows = [(48, 6, r'$G$ : 6 éléments', 'sujet'),
        (32, 3, r'$G^{\prime}$ : 3 éléments', 'sujet'),
        (16, 1, r'$G^{\prime\prime}$ : 1, l’identité', 'resultat')]
for y, n, lab, role in rows:
    for i in range(n):
        box(ax, 2 + i * 7, y, 6, 6, role)
    text(ax, 50, y + 3, lab, role, 's', ha='left')
for i in range(2):
    arrow(ax, (5, rows[i][0]), (5, rows[i + 1][0] + 6), 'varie')
    text(ax, 9, rows[i][0] - 5, 'groupe dérivé', 'varie', 's', ha='left')
save(fig, '64-066')
