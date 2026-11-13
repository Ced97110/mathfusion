import sys, os; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__)))); from figstyle import *

fig, ax = canvas(54)
text(ax, 44, 49, r'$x=4$', 'encre', 'l')
# left: cube 4 x 4 x 4 = 64 unit cubes
cubes(ax, [(i, j, k) for i in range(4) for j in range(4) for k in range(4)], (14, 8), 3.4, 'sujet')
text(ax, 14, 43, r'$x^3=4^3=64$', 'sujet')
text(ax, 35.5, 22, '=', 'encre', 'xl')
# right: 16 columns of 4 dots : 15 columns (15 x 4 = 60) + 1 column (+ 4)
x0, y0, d = 45, 19, 2.4
for c in range(16):
    for r in range(4):
        disc(ax, x0 + d * c, y0 + d * r, 0.8, 'autre' if c < 15 else 'varie', lw=0.4)
text(ax, 63, 33, r'$15x+4=15\times4+4=64$', 'encre', 'm')
brace(ax, x0 - 1, x0 + d * 14 + 1, 17, 'autre', label=r'$15\times4=60$', down=True)
brace(ax, x0 + d * 15 - 1, x0 + d * 15 + 1, 17, 'varie', label='+ 4', down=True)
save(fig, '39-005')
