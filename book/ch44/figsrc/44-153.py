import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(56)
def grid(cx, rows, cols, role):
    for r in range(rows):
        for c in range(cols):
            disc(ax, cx + (c - (cols - 1) / 2) * 5, 34 + ((rows - 1) / 2 - r) * 5, 1.8, role)
grid(22, 3, 4, 'sujet'); grid(66, 4, 3, 'autre')
text(ax, 22, 48, '3 × 4', 'sujet', 'l'); text(ax, 66, 48, '4 × 3', 'autre', 'l')
text(ax, 44, 34, '=', 'encre', 'xl')
text(ax, 22, 20, '12 points', 'sujet', 'm'); text(ax, 66, 20, '12 points', 'autre', 'm')
text(ax, 44, 8, '12 → reste 2 (mod 5)', 'resultat', 'l')
save(fig, '44-153')
