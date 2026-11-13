import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *
fig, ax = canvas(66)
text(ax, 44, 61, r'$u$ : l’élément de $S$ où va $x$', 'encre', 'm')
text(ax, 6, 50, r'$S=$ ℝ', 'fixe', 's', ha='left')
f = numberline(ax, 12, 70, 40, 0, 5, arrow_right=True)
disc(ax, f(3), 40, 2.2, 'varie')
text(ax, f(3), 46, r'$u=3$', 'varie', 'm')
text(ax, 6, 26, r'$S=$ ℤ/5', 'fixe', 's', ha='left')
cw = 12
for v in range(5):
    box(ax, 12 + v * cw, 9, cw - 1, 9, 'varie' if v == 2 else 'fixe', label=str(v), size='m')
text(ax, 12 + 2.5 * cw - 0.5, 22, r'$u=2$', 'varie', 'm')
save(fig, '54-105')
