import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(62)
# horloge de 12
cx, cy, R = 15, 36, 9
for k in range(12):
    a = math.radians(90 - 30 * k)
    disc(ax, cx + R * math.cos(a), cy + R * math.sin(a), 1.4, 'sujet')
text(ax, 15, 54, r'$\mathbb{Z}/12$', 'sujet', 's')
text(ax, 15, 12, 'diviseurs : 4 ; 3', 'sujet', 's')
# grille 4 x 3
for i in range(4):
    for j in range(3):
        box(ax, 36.5 + j * 5, 26 + i * 5, 5, 5, 'sujet', r=0.2, lw=0.6)
text(ax, 44, 54, 'grille 4 × 3', 'sujet', 's')
text(ax, 44, 12, 'diviseurs : 4 ; 3', 'sujet', 's')
text(ax, 30, 36, '=', 'resultat', 'xl', weight='bold')
# grille 2 x 6
for i in range(2):
    for j in range(6):
        box(ax, 61 + j * 4.2, 31 + i * 4.2, 4.2, 4.2, 'autre', r=0.2, lw=0.6)
text(ax, 73, 54, 'grille 2 × 6', 'autre', 's')
text(ax, 73, 12, 'diviseurs : 2 ; 2 ; 3', 'autre', 's')
text(ax, 57, 36, '≠', 'limite', 'xl', weight='bold')
save(fig, '60-108')
