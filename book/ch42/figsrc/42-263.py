import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(74)
ox, oy, d = 16, 8, 8
box(ax, ox + 2 * d - 4, oy - 4, 8, 7 * d + 8, 'varie', fill=False, dash=True)
for i in range(3):
    for j in range(8):
        if i <= j: disc(ax, ox + i * d, oy + j * d, 1.6, 'sujet')
        else: disc(ax, ox + i * d, oy + j * d, 1.1, 'fixe', fill=False)
    text(ax, ox + i * d, 3, str(i), 'fixe', 's')
disc(ax, ox + 2 * d, oy + 3 * d, 2.2, 'varie'); disc(ax, ox + 2 * d, oy + 7 * d, 2.2, 'varie')
text(ax, 8, oy + 3 * d, '3', 'fixe', 's'); text(ax, 8, oy + 7 * d, '7', 'fixe', 's')
text(ax, ox + 3 * d + 6, 3, r'$x$', 'encre', 's'); text(ax, 8, oy + 7 * d + 6, r'$y$', 'encre', 's')
for j in (3, 7):
    line(ax, [(ox + 2 * d + 3, oy + j * d), (45, oy + j * d)], 'varie')
    text(ax, 47, oy + j * d, f'(2, {j})', 'varie', 's', ha='left')
text(ax, 64, 50, 'colonne de 2 :', 'varie', 's'); text(ax, 64, 46, 'plusieurs points', 'varie', 's')
disc(ax, 48, 18, 1.6, 'sujet'); text(ax, 52, 18, r'points où $x \leq y$', 'sujet', 's', ha='left')
save(fig, '42-263')
