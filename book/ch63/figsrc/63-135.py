import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(76)
text(ax, 44, 71, '(x² − 2)(x² − 3), séparable', 'encre', 's')
box(ax, 4, 54, 34, 10, role='fixe', label='x² − 2')
box(ax, 50, 54, 34, 10, role='fixe', label='x² − 3')
text(ax, 44, 59, '×', 'encre', 'm')
roots = [(13, '√2'), (29, '−√2'), (59, '√3'), (75, '−√3')]
for cx, t in roots:
    disc(ax, cx, 40, 5.5, role='sujet', label=t)
    arrow(ax, (21 if cx < 44 else 67, 53.2), (cx, 45.8), 'varie')
    arrow(ax, (cx, 34.2), (44 + (cx - 44) * 0.6, 27.0), 'varie')
box(ax, 8, 8, 72, 18, role='resultat', label='E = ℚ(√2, √3)\n4 racines distinctes : [E:ℚ] = 4 = |G|')
save(fig, '63-135')
