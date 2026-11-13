import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
cw, h, x0 = 5.5, 7, 28
text(ax, 44, 67, 'A = 0 : K = {0}', 'encre', 'm', weight='bold')
text(ax, 44, 59, 'M ≅ D³ : 3 copies de D', 'sujet', 's')
for r in range(3):
    y = 40 - r * 15
    text(ax, 4, y + h / 2, f'Dz{"₁₂₃"[r]} ≅ D', 'sujet', 's', ha='left')
    for i in range(8):
        box(ax, x0 + i * cw, y, cw, h, 'sujet', r=0.3)
    arrow(ax, (x0 + 8 * cw + 1, y + h / 2), (x0 + 8 * cw + 11, y + h / 2), 'sujet', lw=1.0)
text(ax, 44, 4, 'aucun retour à 0 : libre', 'sujet', 's')
save(fig, '59-128')
