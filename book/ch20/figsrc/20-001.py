import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(62)
text(ax, 44, 57, 'Budget : 12 €', 'encre', 'l', weight='bold')
rows = [(3, 2, '= 12 €', 'resultat', 'permis', 34), (4, 2, '= 14 €', 'limite', 'trop', 12)]
for n, g, tot, role, verdict, y in rows:
    text(ax, 2, y + 13.5, f'{n} pains + {g} gâteaux', 'encre', 'm', ha='left')
    x = 2
    for i in range(n): box(ax, x, y, 8, 8, 'sujet'); x += 9.5
    for i in range(g): box(ax, x, y, 8, 8, 'varie'); x += 9.5
    text(ax, x + 2, y + 4, tot, role, 'l', ha='left', weight='bold')
    text(ax, x + 2, y + 11, verdict, role, 's', ha='left')
box(ax, 2, 2.5, 5, 5, 'sujet'); text(ax, 9, 5, 'pain : 2 €', 'encre', 's', ha='left')
box(ax, 44, 2.5, 5, 5, 'varie'); text(ax, 51, 5, 'gâteau : 3 €', 'encre', 's', ha='left')
save(fig, '20-001')
