import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
text(ax, 44, 62, 'deux groupes de 12 éléments', 'encre', 's')
cx, cy, R = 20, 36, 12
for k in range(12):
    a = math.radians(90 - 30 * k)
    disc(ax, cx + R * math.cos(a), cy + R * math.sin(a), 1.7, 'sujet')
text(ax, 20, 53, 'horloge de 12', 'sujet', 's')
text(ax, 20, 14, 'diviseurs : 4 ; 3', 'sujet', 's')
gx, gy, s = 56, 29, 5.2
for i in range(2):
    for j in range(6):
        disc(ax, gx + j * s, gy + i * s, 1.7, 'autre')
text(ax, 69, 45, 'grille 2 × 6', 'autre', 's')
text(ax, 69, 14, 'diviseurs : 2 ; 2 ; 3', 'autre', 's')
text(ax, 43, 36, '≠', 'limite', 'xl', weight='bold')
save(fig, '60-097')
