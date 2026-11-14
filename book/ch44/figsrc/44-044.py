import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(84)
c = 3.4; x0 = (W - 16 * c) / 2; y0 = 13
for i in range(16):
    for j in range(16):
        hi = (j == 0 and i < 8)
        box(ax, x0 + i * c, y0 + j * c, 3.0, 3.0, 'autre' if hi else 'sujet', r=0.3, lw=0.3)
text(ax, 44, 78, r'$M(S)$ : toutes les transformations', 'sujet', 'm', weight='bold')
text(ax, 44, 72, r'$4 \times 4 \times 4 \times 4 = 256$', 'sujet', 'm')
brace(ax, x0, x0 + 8 * c - 0.4, y0 - 1, 'autre', '8 mouvements du carreau', down=True)
save(fig, '44-044')
