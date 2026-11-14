import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(78)
text(ax, 44, 73, 'chacun : 12 éléments', 'fixe', 'm')
cx, cy, r = 21, 50, 13
for h in range(12):
    a = math.radians(90 - 30 * h)
    disc(ax, cx + r * math.cos(a), cy + r * math.sin(a), 1.4, 'sujet')
text(ax, 21, 30, 'ℤ/12', 'sujet', 'm')
text(ax, 21, 24, 'facteurs : 12', 'sujet', 's')
for i in range(2):
    for j in range(6):
        disc(ax, 50 + 5 * j, 53 - 5 * i, 1.4, 'autre')
text(ax, 63, 30, 'ℤ/2 ⊕ ℤ/6', 'autre', 'm')
text(ax, 63, 24, 'facteurs : 2 ; 6', 'autre', 's')
text(ax, 41.5, 50, '≠', 'limite', 'xl')
text(ax, 44, 10, 'pas isomorphes', 'limite', 'm')
save(fig, '60-071')
