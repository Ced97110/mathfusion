import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
text(ax, 44, 78, 'forme bilinéaire', 'sujet', 'm', weight='bold')
rows = [(62, 'sujet', '(1 ; 2) et (3 ; 4)', '1×3 + 2×4 = 11'),
        (48, 'varie', 'premier doublé : (2 ; 4)', '6 + 16 = 22 = 2 × 11'),
        (34, 'varie', 'somme : (1 ; 3) et (3 ; 4)', '3 + 12 = 15 = 11 + 4')]
def row(y, role, lab, eq):
    box(ax, 2, y, 84, 11, role)
    text(ax, 5, y + 5.5, lab, 'encre', 's', ha='left')
    text(ax, 68, y + 5.5, eq, 'encre', 'm')
for r in rows:
    row(*r)
text(ax, 44, 26, 'forme quadratique', 'autre', 'm', weight='bold')
row(10, 'autre', 'un seul vecteur : (1 ; 2)', '1×1 + 2×2 = 5')
save(fig, '57-226')
