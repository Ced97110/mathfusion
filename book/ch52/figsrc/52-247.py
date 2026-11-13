import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(75)
text(ax, 2, 68, 'trois petits calculs', 'sujet', 'm', ha='left')
rows = [(54, 3, '1 × 2 = 2', 2), (40, 4, '3 × 0 = 0', 0), (26, 5, '2 × 3 = 1', 1)]
for y, m, s, r in rows:
    text(ax, 2, y, f'mod {m} : {s}', 'encre', 's', ha='left')
    for i in range(m):
        box(ax, 40 + i * 6.2, y - 2.5, 5, 5, 'resultat' if i == r else 'fixe')
    line(ax, [(40 + m * 6.2 + 0.5, y), (76, y)], 'varie')
line(ax, [(76, 54), (76, 18)], 'varie')
arrow(ax, (76, 24), (76, 18), 'varie')
box(ax, 66, 8, 20, 10, 'resultat', label='56')
text(ax, 62, 12.5, 'recoller : 56 < 60', 'resultat', 's', ha='right')
save(fig, '52-247')
