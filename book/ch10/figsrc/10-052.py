import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(72)
sp = 4.6; gx = 8; gy = 22; r = 1.7
for i in range(4):
    for j in range(7):
        disc(ax, gx + j * sp, gy + i * sp, r, 'sujet' if j < 2 else 'varie')
brace(ax, gx - r, gx + 1 * sp + r, gy + 3 * sp + 3, 'sujet', label=None, down=False)
brace(ax, gx + 2 * sp - r, gx + 6 * sp + r, gy + 3 * sp + 3, 'varie', label=None, down=False)
text(ax, gx + 0.5 * sp, gy + 3 * sp + 9, '2', 'sujet', 'm'); text(ax, gx + 4 * sp, gy + 3 * sp + 9, '5', 'varie', 'm')
text(ax, 2.6, gy + 1.5 * sp, '4', 'encre', 'm')
text(ax, gx + 3 * sp, 12, r'$4 \times (2 + 5) = 28$', 'encre', 'm')
text(ax, 66, 50, r'$4 \times 2 = 8$', 'sujet', 'm')
text(ax, 66, 38, r'$4 \times 5 = 20$', 'varie', 'm')
text(ax, 66, 26, r'$8 + 20 = 28$', 'resultat', 'm')
save(fig, '10-052')
