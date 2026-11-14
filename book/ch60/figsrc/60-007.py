import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
cx, cy, R = 20, 34, 14
for h in range(12):
    a = math.radians(90 - 30 * h)
    disc(ax, cx + R * math.cos(a), cy + R * math.sin(a), 2.6, 'sujet')
for i in range(4):
    for j in range(3):
        box(ax, 56 + 8 * j + 0.3, 20 + 7 * i + 0.3, 7.4, 6.4, 'autre', r=0.5)
text(ax, 44, 34, '?', 'varie', 'xl', weight='bold')
text(ax, 20, 10, 'horloge : 12 éléments', 'sujet', 's')
text(ax, 68, 10, 'grille 4 × 3 : 12 éléments', 'autre', 's')
save(fig, '60-007')
