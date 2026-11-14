import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(70)
text(ax, 41, 66, 'case G', 'sujet'); text(ax, 65, 66, 'case H', 'autre')
rows = [(54, 'couple (1, 2)', '1', '2', 'sujet', 'autre'), (36, 'inverse (1, 1)', '1', '1', 'sujet', 'autre'), (18, 'sommes', '1 + 1 = 0', '2 + 1 = 0', 'resultat', 'resultat')]
for y, lab, a, b, r1, r2 in rows:
    text(ax, 3, y + 4.5, lab, 'encre', 'm', ha='left')
    box(ax, 30, y, 22, 9, r1, label=a); box(ax, 54, y, 22, 9, r2, label=b)
for x in (41, 65): arrow(ax, (x, 54), (x, 45.5), 'varie')
for x in (41, 65): arrow(ax, (x, 18), (x, 11.5), 'varie')
box(ax, 30, 2, 46, 9, 'resultat', label='(0, 0) : le neutre')
save(fig, '45-163')
